class QueryUtils:

    @staticmethod
    def check_table_name(table_name: str) -> bool:
        names = list(table_name.split(' '))
        if len(names) == 1:
            return True
        return False