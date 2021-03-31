import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("1720136461:AAFhafZf65a-uKRXQGe59IKdcHut2Jl5YsE", "")

    APP_ID = int(os.environ.get("3454845", 12345))

    API_HASH = os.environ.get("a205de875f47541dfa6b213bdfe56d36", "")
