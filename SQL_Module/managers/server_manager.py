from SQL_Module.server_connection.connector import Connector
from SQL_Module.managers.query_manager import QueryManager

class ServerManager:

    def __init__(self, database_name):
        self.connector = Connector(database_name=database_name)
        self._query_manager = QueryManager(connection=self.connector.connection)

    def __del__(self):
        if self.connector:
            del self.connector

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        del self

    def create_table(self,  table_name, columns):
        self._query_manager.create_table(table_name, columns)

    def delete_table(self, table_name):
        self._query_manager.delete_table(table_name)

    def select_all(self, table_name):
        return self._query_manager.select_all(table_name)

    def select_all_data_where(self, table_name, condition):
        return self._query_manager.select_all_where(table_name, condition)

    def insert_data(self, table_name, columns, values):
        self._query_manager.insert_data(table_name, columns, values)

    def insert_all_data(self, table_name, values):
        self._query_manager.insert_all_data(table_name, values)

    def update_table(self, table_name, col_val_pairs, condition):
        self._query_manager.update_table(table_name, col_val_pairs, condition)

    def delete_data(self, table_name, condition):
        self._query_manager.delete_data(table_name, condition)