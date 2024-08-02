import pymysql
import psycopg2
from abc import ABC, abstractmethod
# pattern Abstract Factory


class DBFactory(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def cursor(self, connection):
        pass


class MySQLFactory(DBFactory):
    def connect(self):
        print('Соединение с БД MySQL')
        return pymysql.connect(user='my_user', password='my_password', host='localhost', database="my_db")

    def cursor(self, connection):
        return connection.cursor()


class PostgresQLFactory(DBFactory):
    def connect(self):
        print('Соединение с БД PostgresQL')
        return psycopg2.connect(user='my_user', password='my_password', host='localhost', database="my_db")

    def cursor(self, connection):
        return connection.cursor()


class QueryBuilder:
    def __init__(self):
        self._query = {
            'select': "",
            'from': "",
            'where': "",
            'order_by': "",
        }

    def select(self, *columns):
        self._query['select'] = ", ".join(columns)
        return self

    def from_table(self, table):
        self._query['from'] = table
        return self

    def where(self, condition):
        self._query['where'] = condition
        return self

    def order_by(self, column, order='ASC'):
        self._query['order_by'] = f'{column} {order} '
        return self

    def get_query(self):
        query = f'SELECT {self._query['select']} FROM {self._query['from']}'
        if self._query['where']:
            query += f" WHERE {self._query['where']}"
        if self._query['order_by']:
            query += f" ORDER BY {self._query['order_by']}"
        return query + ';'


class User:
    def __init__(self, id, name: str, contact: str):
        self.id = id
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"{self.id} пользователь: {self.name}, {self.contact}"


class UserMapper:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_by_id(self, id):
        self.cursor.execute('SELECT id, name, email FROM users WHERE id = %s', (id,))
        result = self.cursor.fetchone()
        if result:
            return User(id=result[0], name=result[1], contact=result[2])
        return None

    def insert(self, user: User):
        self.cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.contact))



class DBConnectionManager:
    def __init__(self, factory: DBFactory):
        self._factory = factory
        self.connection = None
        self.cursor = None

    def connect(self):
        if not self.connection:
            self.connection = self._factory.connect()
            self.cursor = self._factory.cursor(self.connection)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        self.connection = None
        self.cursor = None

    def get_cursor(self):
        if not self.cursor:
            self.connect()
        return self.cursor

if __name__ == '__main__':
    mysql_factory = MySQLFactory()
    postgresql_factory = PostgresQLFactory()

    mysql_manager = DBConnectionManager(mysql_factory)
    postgresql_manager = DBConnectionManager(postgresql_factory)

    sql_builder = QueryBuilder()
    query = sql_builder.select('id', 'name', 'contact').from_table('users').where('id = %s').get_query()

    mysql_cursor = mysql_manager.get_cursor()
    mysql_cursor.execute(query, (1,))
    user_mapper = UserMapper(mysql_cursor)
    user = user_mapper.get_by_id(1)
    print(user.name, user.contact)

    mysql_manager.close()
    postgresql_manager.close()