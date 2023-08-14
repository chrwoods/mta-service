import os


class Config:
    MTA_API_KEY = os.environ.get('MTA_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    PORT = os.environ.get("PORT", 5000)
