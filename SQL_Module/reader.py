import json

class Reader:

    @staticmethod
    def read_config_win():
        with open("SQL_Module\\config.json", "r") as f:
            data = json.load(f)
            return data

    @staticmethod
    def read_config_linux():
        with open("SQL_Module/config.json", "r") as f:
            data = json.load(f)
            return data