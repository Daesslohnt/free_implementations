import platform
import json

class Reader:
    SLASH = '/' if platform.system() == 'Linux' else '\\'
    CONFIG_PATH = "SQL_Module{}src{}config.json".format(SLASH, SLASH)

    @staticmethod
    def read_config():
        with open(Reader.CONFIG_PATH, "r") as f:
            data = json.load(f)
            return data
