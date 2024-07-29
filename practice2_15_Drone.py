import jwt
import practice2_15_Server
import time

SECRET_KEY = 'MYkey-111'

def request_token(user_id):
    return practice2_15_Server.generate_token(user_id)

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS512', 'HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        print('Срок годности токена истёк')
        return None
    except jwt.InvalidTokenError:
        print('Токен не валиден')
        return None

user_id = 'Alex1'
token = request_token(user_id)
print(f'{user_id} получили токен:\n{token}')

time.sleep(7)

user_id_from_token = verify_token(token)
if user_id_from_token:
    print(f'Пользователь {user_id_from_token} авторизован')
else:
    print('Ошибка авторизации')