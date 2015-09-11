"""
Django local settings template for core project
"""

DEBUG = True

SECRET_KEY = "+XF0N/6vwRU(3KKjOA^g4+ZNAFO~Sv?F;/V|eR6=z8YZ20`O:y5qacB9BJo."

DATABASES = {"default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": "core.db.sqlite3",
}}

ALLOWED_HOSTS = []
