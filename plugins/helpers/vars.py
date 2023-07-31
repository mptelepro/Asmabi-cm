import os


ADMINS = int(os.environ.get("ADMINS"))
DATABASE_URL = os.environ.get("DATABASE_URL")
DEFAULT_LANGUAGE = os.environ.get("DEFAULT_LANGUAGE", "en")
