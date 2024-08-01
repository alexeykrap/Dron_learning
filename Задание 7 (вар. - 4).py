from abc import ABC, abstractmethod

# Абстрактная фабрика
class AbstractDBFactory(ABC):
    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def create_cursor(self, connection):
        pass

class MySQLDatabaseFactory(AbstractDBFactory):
    def create_connection(self):
        import mysql.connector
        return mysql.connector.connect(user='mysql_user', password='mysql_pass', host='localhost', database='mysql_db')

    def create_cursor(self, connection):
        return connection.cursor(dictionary=True)  # Используем dictionary для возврата данных как словаря

class PostgreSQLDatabaseFactory(AbstractDBFactory):
    def create_connection(self):
        import psycopg2
        return psycopg2.connect(user='postgres_user', password='postgres_pass', host='localhost', database='postgres_db')

    def create_cursor(self, connection):
        return connection.cursor()

# Паттерн Строитель
class SQLQueryBuilder:
    def __init__(self):
        self._select = ""
        self._from = ""
        self._where = ""
        self._order_by = ""

    def select(self, *columns):
        self._select = ", ".join(columns)
        return self

    def from_table(self, table):
        self._from = table
        return self

    def where(self, condition):
        self._where = condition
        return self

    def order_by(self, column, order="ASC"):
        self._order_by = f"{column} {order}"
        return self

    def build(self):
        query = f"SELECT {self._select} FROM {self._from}"
        if self._where:
            query += f" WHERE {self._where}"
        if self._order_by:
            query += f" ORDER BY {self._order_by}"
        return query + ";"

# ORM (Отображение объектно-реляционное)
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class UserMapper:
    def __init__(self, cursor):
        self.cursor = cursor

    def find_by_id(self, user_id):
        self.cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return User(**result)
        return None

    def insert(self, user):
        self.cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email))

# Паттерн Хранитель
class DatabaseConnectionManager:
    def __init__(self, factory):
        self.factory = factory
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.connection is None:
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
mysql_factory = MySQLDatabaseFactory()
postgresql_factory = PostgreSQLDatabaseFactory()

mysql_manager = DatabaseConnectionManager(mysql_factory)
postgresql_manager = DatabaseConnectionManager(postgresql_factory)

sql_builder = SQLQueryBuilder()
query = sql_builder.select("id", "name", "email").from_table("users").where("id = %s").build()

mysql_cursor = mysql_manager.get_cursor()
mysql_cursor.execute(query, (1,))
user_mapper = UserMapper(mysql_cursor)
user = user_mapper.find_by_id(1)
if user:
    print(user.name, user.email)

mysql_manager.disconnect()
postgresql_manager.disconnect()
