import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("1948597074:AAEeHZB87RHgVlvvwkVDSJw9J6wOwmoxcfk", "")

    APP_ID = int(os.environ.get("7116032", 12345))

    API_HASH = os.environ.get("b52c92ca8a424f260c884d3f742dee7e", "")
