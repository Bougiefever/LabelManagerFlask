import os
import datetime
from dotenv import load_dotenv
from urllib.parse import quote_plus
import urllib
basedir = os.path.abspath(os.path.dirname(__file__))

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY') or 'flask-secrets'

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)

    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev'
    server_name = os.getenv('DEV_SQL_SERVER_NAME')
    database_name = os.getenv('DEV_DATABASE_NAME')
    db_username = os.getenv('DEV_SQL_SERVER_USERNAME')
    db_password = os.getenv('DEV_SQL_SERVER_PASSWORD')

    # connection to SQLExpress
    connection_string = r'DRIVER={ODBC Driver 17 for SQL Server};' + "SERVER={0};DATABASE={1};UID={2};PWD={3}".format(server_name, database_name, db_username, db_password)

    # connection to Azure SQL Server
    #connection_string = r'Driver={ODBC Driver 13 for SQL Server};' +  "Server=tcp:{0}.database.windows.net,1433;Database={1};Uid={2}@{0};Pwd={3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;".format(server_name, database_name, db_username, db_password)
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(quote_plus(connection_string))
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    cs = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=adlabeling.database.windows.net;PORT=1433;DATABASE=adlabelingdb;UID=sqladmin@adlabeling;PWD=Volunteer2018")
    pyodbc_cs = "mssql+pyodbc:///?odbc_connect=%s" % cs
    SQLALCHEMY_DATABASE_URI =  pyodbc_cs


class TestingConfig(Config):
    DEBUG = True
    TESTING = True

    # Include testing values here so pytest can use them
    # Connecting to a local sql server
    server_name = '.\SQLEXPRESS'
    database_name = 'labelmanagertestdb'
    db_username = 'testuser'
    db_password = 'Volunteer2019'

    # connection to SQLExpress
    connection_string = r'DRIVER={ODBC Driver 17 for SQL Server};' + "SERVER={0};DATABASE={1};UID={2};PWD={3}".format(server_name, database_name, db_username, db_password)

    # connection to Azure SQL Server
    #connection_string = r'Driver={ODBC Driver 13 for SQL Server};' +  "Server=tcp:{0}.database.windows.net,1433;Database={1};Uid={2}@{0};Pwd={3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;".format(server_name, database_name, db_username, db_password)
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(quote_plus(connection_string))

    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'test'


class ProductionConfig(Config):
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    DEBUG = True

    server_name = os.getenv('SQL_SERVER_NAME')
    server = '{}.database.windows.net'.format(server_name)
    database = os.getenv('DATABASE_NAME')
    username = '{}@{}'.format(os.getenv('SQL_SERVER_USERNAME'), server_name)
    password = os.getenv('SQL_SERVER_PASSWORD')

    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(quote_plus(connection_string))

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging


config_list = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,

    'default': DevelopmentConfig
}
