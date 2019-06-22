import os
import datetime
import urllib
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'flask-secrets'

    JWT_SECRET_KEY = 'jwt-secrets'
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
    server_name = "adlabeling"
    database_name = "adlabelingdevdb"
    db_username = "my_sql_server_username"
    db_password = "my_sql_server_password"
    connection_string = r'Driver={ODBC Driver 13 for SQL Server};' +  "Server=tcp:{0}.database.windows.net,1433;Database={1};Uid={2}@{0};Pwd={3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;".format(server_name, database_name, db_username, db_password)
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(urllib.parse.quote_plus(connection_string))
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    server_name = "adlabeling"
    database_name = "adlabelingtestdb"
    db_username = "my_sql_server_username"
    db_password = "my_sql_server_password"
    connection_string = r'Driver={ODBC Driver 13 for SQL Server};' +  "Server=tcp:{0}.database.windows.net,1433;Database={1};Uid={2}@{0};Pwd={3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;".format(server_name, database_name, db_username, db_password)
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(urllib.parse.quote_plus(connection_string))

    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'test'


class ProductionConfig(Config):
    server_name = "adlabeling"
    database_name = "adlabelingdb"
    db_username = "my_sql_server_username"
    db_password = "my_sql_server_password"
    connection_string = r'Driver={ODBC Driver 13 for SQL Server};' + "Server=tcp:{0}.database.windows.net,1433;Database={1};Uid={2}@{0};Pwd={3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;".format(server_name, database_name, db_username, db_password)
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(urllib.parse.quote_plus(connection_string))

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
