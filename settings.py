from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret, URL

config = Config(".env")
DEBUG = config('DEBUG', cast=bool, default=True)
SECRET_KEY = config('SECRET_KEY', cast=Secret, default=None )
EMAIL = config("EMAIL_ADDRESS", default=None)
PASSWORD = config("EMAIL_PASSWORD", cast=Secret, default=None)
DATABASE_URL = config('DATABASE_URL',  default=None)

# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings, default=None)
