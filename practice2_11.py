from abc import ABC, abstractmethod
import sqlite3


# pattern Abstract Factory
class DBFactory(ABC):
    @abstractmethod
    def connect(self):
        pass


class SQLiteDBFactory(DBFactory):
    def connect(self):
        return sqlite3.connect(':memory:')
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


class Drone:
    def __init__(self, model, manufacturer, year):
        self._model = model
        self._manufacturer = manufacturer
        self._year = year

    def get_model(self):
        return self._model

    def get_manufacturer(self):
        return self._manufacturer

    def get_year(self):
        return self._year


if __name__ == "__main__":
    sql = SQLiteDBFactory()
    connection = sql.connect()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE tbl_drones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        manufacturer TEXT,
        year INTEGER
        )
    """)

    # drone = {
    #     "model": "model x",
    #     "manufacturer": "SkyCorp",
    #     "year": "2024",
    # }  # в качестве домашнего задания сделать таблицу в базе данных

    my_drone = Drone('Model X', 'FlyCorp', '2024')
    my_drone2 = Drone("Model Y", "NewCorp", "2025")

    query_builder = QueryBuilder()
    insert_into = query_builder.insert_into("tbl_drones", ['model', 'manufacturer', 'year'])\
        .values(my_drone.get_model(), my_drone.get_manufacturer(), my_drone.get_year()).get_query()
    print(insert_into)

    query_builder2 = QueryBuilder()
    insert_into2 = query_builder2.insert_into("tbl_drones", ["model", "manufacturer", "year"])\
        .values(my_drone2.get_model(), my_drone2.get_manufacturer(), my_drone2.get_year()).get_query()
    print(insert_into2)

    params = query_builder.get_params()
    cursor.execute(insert_into, params)
    connection.commit()

    # Вывод сформированного запроса
    params2 = query_builder2.get_params()  # Получение параметров для запроса WHERE
    cursor.execute(insert_into2, params2)  # Выполнение запроса с параметрами
    connection.commit()

    # Создание SELECT-запроса с использованием нового экземпляра QueryBuilder
    select_query = QueryBuilder()
    select_query = select_query.select('tbl_drones').get_query()
    cursor.execute(select_query)
    results = cursor.fetchall()

    # Вывод всех записей из таблицы
    for row in results:
        print(row)

    connection.close()  # Закрытие подключения к базе данных



