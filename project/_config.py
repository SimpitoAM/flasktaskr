import os

#grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = '(\xb6O\xbaDV)\xae\xdfN\x00\xfd\xd7\xb1\x96>t\x9b3\xffo\xae\xc6~'

#define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)
