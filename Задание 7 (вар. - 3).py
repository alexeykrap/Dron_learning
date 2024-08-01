from abc import ABC, abstractmethod

# Абстрактная фабрика
class DBFactory(ABC):
    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def create_cursor(self, connection):
        pass

class MySQLFactory(DBFactory):
    def create_connection(self):
        import mysql.connector
        return mysql.connector.connect(user='mysql_user', password='mysql_pass', host='localhost', database='mysql_db')

    def create_cursor(self, connection):
        return connection.cursor()

class PostgreSQLFactory(DBFactory):
    def create_connection(self):
        import psycopg2
        return psycopg2.connect(user='postgres_user', password='postgres_pass', host='localhost', database='postgres_db')

    def create_cursor(self, connection):
        return connection.cursor()

# Паттерн Строитель
class SQLQueryBuilder:
    def __init__(self):
        self._query_parts = {
            "select": "",
            "from": "",
            "where": "",
            "order_by": ""
        }

    def select(self, *columns):
        self._query_parts["select"] = ", ".join(columns)
        return self

    def from_table(self, table):
        self._query_parts["from"] = table
        return self

    def where(self, condition):
        self._query_parts["where"] = condition
        return self

    def order_by(self, column, order="ASC"):
        self._query_parts["order_by"] = f"{column} {order}"
        return self

    def build(self):
        query = f"SELECT {self._query_parts['select']} FROM {self._query_parts['from']}"
        if self._query_parts["where"]:
            query += f" WHERE {self._query_parts['where']}"
        if self._query_parts["order_by"]:
            query += f" ORDER BY {self._query_parts['order_by']}"
        return query + ";"

# Объектно-реляционное отображение
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class UserMapper:
    def __init__(self, cursor):
        self.cursor = cursor

    def find_by_id(self, user_id):
        self.cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return User(user_id=result[0], name=result[1], email=result[2])
        return None

    def insert(self, user):
        self.cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email))

# Паттерн Хранитель
class DBConnectionManager:
    def __init__(self, factory):
        self.factory = factory
        self.connection = None
        self.cursor = None

    def connect(self):
        if not self.connection:
            self.connection = self.factory.create_connection()
            self.cursor = self.factory.create_cursor(self.connection)

    def disconnect(self):
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

# Тестирование
mysql_factory = MySQLFactory()
postgresql_factory = PostgreSQLFactory()

mysql_manager = DBConnectionManager(mysql_factory)
postgresql_manager = DBConnectionManager(postgresql_factory)

sql_builder = SQLQueryBuilder()
query = sql_builder.select("id", "name", "email").from_table("users").where("id = %s").build()

mysql_cursor = mysql_manager.get_cursor()
mysql_cursor.execute(query, (1,))
user_mapper = UserMapper(mysql_cursor)
user = user_mapper.find_by_id(1)
print(user.name, user.email)

mysql_manager.disconnect()
postgresql_manager.disconnect()
