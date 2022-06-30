import json

class Reader:

    @staticmethod
    def read_config():
        with open("SQL_Module\\config.json", "r") as f:
            data = json.load(f)
            return data