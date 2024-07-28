import sqlite3
import pymysql
import psycopg2
from abc import ABC, abstractmethod
# pattern Abstract Factory


class DBFactory(ABC):
    @abstractmethod
    def connect(self, path, user='root', password='', host='localhost'):
        pass


class SQLiteFactory(DBFactory):
    try:
        def connect(self, path, user='root', password='', host='localhost'):
            return sqlite3.connect(database=path)
    except:
        print("Не получилось установить соединения с базой данных")


class MySQLFactory(DBFactory):
    try:
        def connect(self, path, user='root', password='', host='localhost'):
            return pymysql.connect(database=path)
    except:
        print("Не получилось установить соединения с базой данных")


class PostgresQLFactory(DBFactory):
    try:
        def connect(self, path, user='root', password='', host='localhost'):
            return psycopg2.connect(database=path)
    except:
        print("Не получилось установить соединения с базой данных")


class QueryBuilder:
    def __init__(self):
        self._query = {
            'select': None,
            'from': None,
            'where': None,
            'order_by': None,
            'insert_into': None,
            'values': None
        }
        self._params = []

    def select(self, table, columns='*'):
        self._query['select'] = f'SELECT {columns} '
        self._query['from'] = f' FROM {table} '
        return self

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
        placeholders = ','.join(['?'] * len(columns))
        self._query['insert_into'] = f'INSERT INTO {table} ({cols})'
        self._query['values'] = f'VALUES ({placeholders})'
        return self

    def values(self, *values):
        self._params.extend(values)
        return self

    def get_query(self):
        query = ''
        if self._query['select']:
            query = f"{self._query['select']} {self._query['from']}"
        if self._query['where']:
            query += f" {self._query['where']}"
        if self._query['order_by']:
            query += f" {self._query['order_by']}"
        if self._query['insert_into']:
            query = f" {self._query['insert_into']} {self._query['values']}"
        return query

    def get_params(self):
        return self._params


class User:
    def __init__(self, id, name: str, contact: str, comments: str):
        self.id = id
        self.name = name
        self.contact = contact
        self.comments = comments

    def __str__(self):
        return f"{self.id} пользователь: {self.name}, {self.contact}, ({self.comments})"


class UserMapper:
    def __init__(self, connection):
        self.connection = connection

    def get_user(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM tbl_users WHERE id={id}')
        result = cursor.fetchone()
        if result:
            user = User(
                id=result[0],
                name=result[1],
                contact=result[2],
                comments=result[3]
            )
            return str(user)
        return "Ничего не найдено..."

    def add_user(self, user: User):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO tbl_users VALUES(?, ?, ?, ?)",(
            user.id,
            user.name,
            user.contact,
            user.comments
            )
        )

