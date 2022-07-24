import pymysql
import logging

from SQL_Module.utils.reader import Reader

class Singletone(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singletone, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Connector(metaclass=Singletone):
    logger = logging.getLogger("SQL Logger")
    logger.setLevel(logging.DEBUG)
    config = None
    
    def __init__(self, database_name=None):
        self.config = Reader.read_config()
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