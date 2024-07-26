from abc import ABC, abstractmethod
import sqlite3


# pattern Abstract Factory
class DBFactory(ABC):
    @abstractmethod
    def connect(self):
        pass


class SQLiteDBFactory(DBFactory):
    def __init__(self, database_path: str):
        self.database_path = database_path
    def connect(self):
        return sqlite3.connect(f'{self.database_path}')
        # ':memory:' вместо пути к файлу означает, что база данных создаётся в оперативной памяти


# pattern Builder

class QueryBuilder:
    def __init__(self):
        self._query = {
            'select': None,
            'from': None,
            'where': None,
            'order_by': None,
            'insert_into': None,
            'values': None,
        }
        self._params = []

    def select(self, table, columns='*'):
        self._query['select'] = f'SELECT {columns} '
        self._query['from'] = f' FROM {table} '
        return self

        # tbl_drone -> id, model, manufacturer
        # SELECT * FROM tbl_drones
        # SELECT manufacturer FROM tbl_drones

    def where(self, condition, parameters=None):
        self._query['where'] = f'WHERE {condition} '

        if parameters:
            self._params.extend(parameters)
        return self

    def order_by(self, order):
        self._query['order_by'] = f'ORDER BY {order} '
        return self

    def add_params(self, *parameters):
        self._params.extend(parameters)
        return self

    def insert_into(self, table, columns):
        cols = ','.join(columns)
        # columns = ['model', 'manufacturer']
        # cols = ','.join(columns)
        # columns >>>> 'model,manufacturer'
        placeholders = ",".join(["?"] * len(columns))
        self._query['insert_into'] = f"INSERT INTO {table} ({cols})"
        self._query['values'] = f"VALUES ({placeholders})"
        return self

        # INSERT INTO название_таблицы (список_столбцов) VALUES (значение_столбцов):
        # INSERT INTO tbl_drones (model,manufacturer) VALUES ('model x','FlyCorp')
        # execute("INSERT INTO tbl_drones (models, manufacturer) VALUES (?,?)", ("model x", "FlyCorp"))

    def values(self, *values):
        self._params.extend(values)
        return self

    def get_query(self):
        query = ""
        if self._query["select"]:
            query = f"{self._query['select']} {self._query['from']}"
        if self._query["where"]:
            query += f" {self._query['where']}"
        if self._query['order_by']:
            query += f" {self._query['order_by']}"
        if self._query['insert_into']:
            query = f" {self._query['insert_into']} {self._query['values']}"
        return query

    def get_params(self):
        return self._params


# Pattern ORM
class User:
    def __init__(self, id, operator_name: str, contact: str, comments: str):
        self.id = id
        self.operator_name = operator_name
        self.contact = contact
        self.comments = comments

    def __str__(self):
        return f"{self.id} пользователь: {self.operator_name}, {self.contact}, ({self.comments})"


class UserMapper:
    def __init__(self, connection):
        self.connection = connection

    def get_user(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM tbl_operators WHERE id={id}')
        result = cursor.fetchone()
        if result:
            user = User(
                id=result[0],
                operator_name=result[1],
                contact=result[2],
                comments=result[3]
            )
            return str(user)
        return None

    def add_user(self, user: User):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO tbl_operators VALUES(?, ?, ?, ?)",(
                        user.id,
                        user.operator_name,
                        user.contact, user.
                        comments)
                       )


class Drone:
    def __init__(self, model, manufacturer, purchase_date, max_altitude, max_speed, max_flight_time, serial_number):
        self._model = model
        self._manufacturer = manufacturer
        self._purchase_date = purchase_date
        self._max_altitude = max_altitude
        self._max_speed = max_speed
        self._max_flight_time = max_flight_time
        self._serial_number = serial_number

    def get_model(self):
        return self._model

    def get_manufacturer(self):
        return self._manufacturer

    def get_purchase_date(self):
        return self._purchase_date

    def get_max_altitude(self):
        return self._max_altitude

    def get_max_speed(self):
        return self._max_speed

    def get_max_flight_time(self):
        return self._max_flight_time

    def get_serial_number(self):
        return self._serial_number


if __name__ == "__main__":
    new_user = User(
        3,
        'Коля',
        'vasya@mail.ru',
        'Наш лучший оператор'
    )

    sql = SQLiteDBFactory('test.db')
    connection = sql.connect()

    user_mapper = UserMapper(connection)
    user_mapper.add_user(new_user)

    connection.commit()
    print(user_mapper.get_user(1))

    # sql = SQLiteDBFactory()
    # connection = sql.connect()
    # cursor = connection.cursor()
    #
    # my_drone = Drone(
    #     'Model X',
    #     'FlyCorp',
    #     '2024',
    #     200,
    #     70,
    #     51,
    #     'DJFAK4591236DJFK',
    #     )
    #
    # query_builder = QueryBuilder()
    # insert_into = query_builder.insert_into("tbl_drones", [
    #     'model', 'manufacturer', 'purchase_date', 'max_altitude', 'max_speed',
    #     'max_flight_time', 'serial_number'
    #     ]).values(
    #     my_drone.get_model(), my_drone.get_manufacturer(), my_drone.get_purchase_date(),
    #     my_drone.get_max_altitude(), my_drone.get_max_speed(), my_drone.get_max_flight_time(),
    #     my_drone.get_serial_number()
    # ).get_query()
    # print(insert_into)
    #
    # # Вывод сформированного запроса
    # params = query_builder.get_params()
    # cursor.execute(insert_into, params)
    # connection.commit()
    #
    # # Создание SELECT-запроса с использованием нового экземпляра QueryBuilder
    # select_query = QueryBuilder()
    # select_query = select_query.select('tbl_drones').get_query()
    # cursor.execute(select_query)
    # results = cursor.fetchall()
    #
    # # Вывод всех записей из таблицы
    # for row in results:
    #     print(row)
    #
    connection.close()  # Закрытие подключения к базе данных
