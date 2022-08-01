class QueryUtils:
    TWO_PLACE_OPERATORS = [
        "=", "AND", "OR", ">", "<", 
        ">=", "<=", "<>", "BETWEEN", "LIKE",
        "IN"
    ]
    DANGEROUS_NAMES = [
        "drop", "table",
        "select", "update",
        "limit", "insert",
        "create", "join", "order"
    ]

    @staticmethod
    def check_table_name(table_name: str) -> bool:
        names = list(table_name.split(' '))
        if len(names) == 1:
            return True
        return False

    @staticmethod
    def check_functional_words(string):
        atoms = list(string.split(" "))
        for atom in atoms:
            if atom.lower() in QueryUtils.DANGEROUS_NAMES:
                return True
        return False