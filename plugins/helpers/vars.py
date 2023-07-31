import os


ADMINS = int(os.environ.get("ADMINS"))
DATABASE = os.environ.get("DATABASE_URL")
DEFAULT_LANGUAGE = os.environ.get("DEFAULT_LANGUAGE", "en")
