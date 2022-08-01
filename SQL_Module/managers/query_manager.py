import logging

from SQL_Module.utils.query_utils import QueryUtils

class QueryManager:
    logger = logging.getLogger("SQL Logger")
    TABLE_CREATION = "CREATE TABLE IF NOT EXISTS {} ({});"
    DELETE_TABLE = "DROP TABLE {}"
    SELECT_ALL = "SELECT * FROM {}"
    SELECT_ALL_WHERE = "SELECT * FROM {} WHERE {}"
    INSERT_DATA = "INSERT INTO {} {} VALUES {}"
    UPDATE_DATA = "UPDATE {} SET {} WHERE {}"
    DELETE_DATA = "DELETE FROM {} WHERE {}"


    def __init__(self, connection):
        self.connection = connection

        def connection_decorator(pattern):
            def wrapper(*args, **kwargs):
                try:
                    with self.connection.cursor() as cursor:
                        data = pattern(cursor, *args, **kwargs)
                        return data
                except Exception as ex:
                    self.logger.error(f"{pattern.__name__} is not executable: {ex}")
            return wrapper
        self._decorator = connection_decorator

    def _committable_pattern(self, cursor, query):
        cursor.execute(query)
        self.connection.commit()
        self.logger.info("committable pattern is executed")

    def _fetch_data_pattern(self, cursor, query):
        cursor.execute(query)
        rows = cursor.fetchall()
        self.logger.info("fetch data pattern is executed")
        return rows

    def create_table(self, table_name, columns):
        """
        create a table in database you have connected.

        :param table_name: name of table you want to create
        :param columns: columns your table need to have, example: id INT NOT NULL
        """

        if not QueryUtils.check_table_name(table_name):
            raise IOError("Not allowed name for table", table_name)
        create_table_wrapper = self._decorator(self._committable_pattern)
        create_table_wrapper(query=self.TABLE_CREATION.format(table_name, columns))
        self.logger.warning(f"table {table_name} is created")

    def delete_table(self, table_name: str):
        """
        drop table query in the database.

        :param table_name: name of table you want to delete
        """

        delete_table_wrapper = self._decorator(self._committable_pattern)
        delete_table_wrapper(self.DELETE_TABLE.format(table_name))
        self.logger.warning(f"Table {table_name} is deleted")

    def _custom_select_query(self, query: str) -> tuple:
        selection_wrapper = self._decorator(self._fetch_data_pattern)
        data = selection_wrapper(query)
        return data

    def select_all(self, table_name: str) -> tuple:
        """
        choose all columns from table and receive all rows.

        :parameter table_name: name of table from that you want to receive a data
        :return: tuple of tuples
        """

        if not QueryUtils.check_table_name(table_name):
            raise IOError("Not allowed name for table", table_name)
        data = self._custom_select_query(self.SELECT_ALL.format(table_name))
        self.logger.info(f"data from {table_name} is received")
        return data

    def select_all_where(self, table_name: str, condition: str) -> tuple:
        """
        select all columns with conditions WHERE.

        :param table_name: name of table from where you receive data
        :param condition: conditions after WHERE, do not use other key words!,
        all operators should be separated by space.
        """

        # if QueryUtils.check_functional_words(condition):
        #     raise IOError("Unavailable input by using prohibited key words", condition)
        if not QueryUtils.check_table_name(table_name):
            raise IOError("Not allowed name for table", table_name)
        data = self._custom_select_query(self.SELECT_ALL_WHERE.format(table_name, condition))
        self.logger.info(f"data from {table_name} where {condition} is received")
        return data

    def insert_data(self, table_name: str, columns: str, values: str):
        """
        send a custom insertion query to database.

        :param table_name: name of table you want to insert new data
        :param columns: names of columns in the table in form of (col1, col2, ...)
        :param values: the data in form of (val11, val12, ... ), (val22, val22, ...)
        """

        if not QueryUtils.check_table_name(table_name):
            raise IOError("Not allowed name for table", table_name)
        insert_data_wrapper = self._decorator(self._committable_pattern)
        insert_data_wrapper(self.INSERT_DATA.format(table_name, columns, values))
        self.logger.info("data is inserted")
        
    def insert_all_data(self, table_name: str, values: str):
        """
        send an insertion query with data for all columns of a table to database.

        :param table_name: name of table you want to insert new data
        :param values: the data in form of (val11, val12, ... ), (val22, val22, ...),
        here should be inserted data for all! columns
        """

        self.insert_data(table_name, "", values)

    def update_table(self, table_name: str, new_col_val_pair: str, condition: str):
        """
        Change values under specific conditions.

        :param table_name: name of table you want ot update
        :param new_col_val_pair: column1 = value1, column2 = value2
        :param condition: special conditions on what position values should be changed,
        all operators should be separated by space.
        """

        update_data_wrapper = self._decorator(self._committable_pattern)
        update_data_wrapper(self.UPDATE_DATA.format(table_name, new_col_val_pair, condition))
        self.logger.info(f"Table {table_name} is updated with {new_col_val_pair}")

    def delete_data(self, table_name, condition):
        """
        delete rows of data from a table.

        :param table_name: name of table where you want to delete some data
        :param condition: rows to be deleted, all operators should be separated by space.
        """

        delete_data_wrapper = self._decorator(self._committable_pattern)
        delete_data_wrapper(self.DELETE_DATA.format(table_name, condition))
        self.logger.info(f"Rows from {table_name} where {condition} were deleted")