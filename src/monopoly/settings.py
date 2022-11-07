import configparser

_config = configparser.ConfigParser()
_config.read("./src/monopoly/config.ini")

MIN_PRICE = int(_config["properties"]["MinPrice"])
MAX_PRICE = int(_config["properties"]["MaxPrice"])

MIN_RENT = int(_config["properties"]["MinRent"])
MAX_RENT = int(_config["properties"]["MaxRent"])
