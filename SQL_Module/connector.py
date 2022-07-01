import pymysql
import logging

from SQL_Module.reader import Reader

class Singletone(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singletone, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Connector(metaclass=Singletone):
    config = Reader.read_config()
    logger = logging.getLogger("SQL Logger")
    logger.setLevel(logging.DEBUG)
    
    def __init__(self, database_name=None):
        if database_name is None:
            pass
        else:
            try:
                self.connection = self.connect_to_database(database_name)
                self.logger.warning("connected")
            except Exception as ex:
                self.logger.error(f"Connection is refused:\n{ex}")

    def __del__(self):
        if self.connection:
            self.connection.close()
            self.logger.warning("Connection is closed")

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        del self

    def connect_to_database(self, database_name: str):
        """Connect to database. It is needed to read attributes from config.json"""

        connection = pymysql.connect(
            host=self.config["host"],
            port=self.config["port"],
            user=self.config["username"],
            passwd=self.config["paswd"],
            database=database_name
        )
        self.logger.info("Connection is accepted")
        return connection

    def create_table(self, table_name: str, values: str) -> None:
        """
        create a table in database you have connected.

        :param table_name: name of table you want to create
        :param values: columns your table need to have, example: id INT NOT NULL
        """

        try:
            with self.connection.cursor() as cursor:
                query = f"CREATE TABLE IF NOT EXISTS {table_name} ({values});"
                cursor.execute(query)
                self.connection.commit()
                self.logger.warning(f"Creation of table {table_name} is successful")
        except Exception as ex:
            self.logger.error(f"Problem with creation of table:\n{ex}")

    def select_all(self, table_name: str) -> tuple:
        """
        choose all columns from table and receive all rows.

        :parameter table_name: name of table from that you want to receive a data
        :return: tuple of tuples
        """

        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT * FROM {table_name}"
                cursor.execute(query)
                rows = cursor.fetchall()
                self.logger.info("Selection is successful")
                return rows
        except Exception as ex:
            self.logger.error(f"Problem with select all query:\n{ex}")

    def custom_select_query(self, query: str) -> tuple:
        """
        send a custom selection query to database.

        :param query: you need to define the whole MySQL query including table_name
        :return: tuple of tuples
        """

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                self.logger.info("Selection is successful")
                return rows
        except Exception as ex:
            self.logger.error(f"Problem with selection query:\n{ex}")

    def custom_insert_query(self, query: str) -> None:
        """
        send a custom insertion query to database.

        :param query: you need to define the whole MySQL query including table_name
        """

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
                self.logger.info("Insertion is successful")
        except Exception as ex:
            self.logger.error(f"Problem with insertion query:\n{ex}")

    def update_table(self, table_name: str, key_val_pairs: str, condition: str) -> None:
        """
        Change values under specific conditions.

        :param table_name:
        :param key_val_pairs: column1 = value1, column2 = value2
        :param condition: special conditions on what position values should be changed
        """

        try:
            with self.connection.cursor() as cursor:
                query = f"UPDATE {table_name} SET {key_val_pairs} WHERE {condition}"
                cursor.execute(query)
                self.connection.commit()
                self.logger.info(f"Table {table_name} is successfully updated")
        except Exception as ex:
            self.logger.error(f"Problem with update of table:\n{ex}")

    def delete_table(self, table_name: str) -> None:
        """
        drop query for table in database.

        :param table_name: name of table you want to delete
        """

        try:
            with self.connection.cursor() as cursor:
                query = f"DROP TABLE {table_name}"
                cursor.execute(query)
                self.connection.commit()
                self.logger.info(f"Table {table_name} is successfully deleted")
        except Exception as ex:
            self.logger.error(f"Problem with drop of table:\n{ex}")