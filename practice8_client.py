import jwt
import time
import practice8_server

SECRET_KEY = 'mySUPERsecretKEY-123'


class SomeObject:
    def connect(self):
        print("Соединение с базой данных")

    def get_all_data(self):
        print("Все данные из базы данных")

    def get_data_by_id(self, id: int):
        print(f"Данные из базы по ID: {id}")


class SomeObjectProxy:
    def __init__(self, some_object: SomeObject):
        self._some_object = some_object

    def connect(self):
        if self._some_object:
            self._some_object.connect()

    def get_all_data(self):
        if self._some_object:
            self._some_object.get_all_data()

    def get_data_by_id(self, id: int):
        if self._some_object:
            self._some_object.get_data_by_id(id)


class SomeObjectSecureProxy:
    def __init__(self, some_object: SomeObject, token):
        self._some_object = some_object
        self._token = token

    def verify_token(self):
        try:
            payload = jwt.decode(self._token, SECRET_KEY, algorithms=['HS256'])
            return payload['object_id']
        except jwt.ExpiredSignatureError:
            print('Токен истёк')
            return None
        except jwt.InvalidTokenError:
            print('Токен не валиден')
            return None

    def connect(self):
        if self.verify_token():
            self._some_object.connect()
        else:
            print('Доступ запрещён: ошибка авторизации')

    def get_all_data(self):
        if self.verify_token():
            self._some_object.get_all_data()
        else:
            print('Доступ запрещён: ошибка авторизации')

    def get_data_by_id(self, id: int):
        if self.verify_token():
            self._some_object.get_data_by_id(id)
        else:
            print('Доступ запрещён: ошибка авторизации')


def request_token(object_id):
    return practice8_server.generate_token(object_id)


object_id = '23434'
token = request_token(object_id)
print(f'Объект ID{object_id} получил токен:\n{token}')

object1 = SomeObject()
secure_proxy = SomeObjectSecureProxy(object1, token)
secure_proxy.connect()

time.sleep(7)

secure_proxy.get_all_data()
