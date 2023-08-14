import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MTA_API_KEY = os.environ.get('MTA_API_KEY')
