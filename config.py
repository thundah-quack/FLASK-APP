# Config against CSRF attacks
# secret key used in token for logins


import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
