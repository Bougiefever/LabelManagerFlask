# Label Manager Reference Architecture

## Set up
Create a python environment and install all the packages from the requirements.txt file that you will need into your environment.

```
pip install -r requirements.txt
```

## Database
This example uses an Azure SQL Server database with Flask-SQLAlchemy. You should create a SQL Server in Azure and two databases. One is for production and the other is for testing.

Your connection string should be created as follows in your config.py file
```
    server_name = "your_server_name"
    database_name = "your_database_name"
    db_username = "my_sql_server_username"
    db_password = "my_sql_server_password"
    connection_string = r'Driver={ODBC Driver 13 for SQL Server};' +  "Server=tcp:{0}.database.windows.net,1433;Database={1};Uid={2}@{0};Pwd={3};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;".format(server_name, database_name, db_username, db_password)
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(urllib.parse.quote_plus(connection_string))
```

For local development, you can use a SQLExpress database too. Set your SQLExpress up to use Sql Server passwords instead of Windows Authentication, and set up a user that has sufficient privileges. That connection can be created as shown below:
```
    server_name = ".\SQLEXPRESS"
    database_name = "your_database_name"
    db_username = "username"
    db_password = "password"
    connection_string = r'DRIVER={ODBC Driver 13 for SQL Server};' + "SERVER={0};DATABASE={1};UID={2};PWD={3}".format(server_name, database_name, db_username, db_password)
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(urllib.parse.quote_plus(connection_string))

```


### Database initialization
To create db tables, open a flask shell and run db.create_all().

To drop all db tables, open a flask shell and run db.drop_all()

To create db migrations:

## Configuration
The configuration settings need to be stored in a file named "config.py" in the root of the project. This file is not checked into source contral since it contains your keys and passwords. To set up your config.py correctly, copy the file example.config.py to config.py and update the values with your info.

## Testing
To set up testing, you need to install the Label Manager package locally with the following command.
```
pip install -e .
```

Run the tests with the pytest command at the command prompt.
```
pytest
```

Some tests are marked with a custom marker 'smoke'. These are very basic tests to ensure that the site is functional. You can run this subset of tests with the following command:
```
pytest -v -m 'smoke'
```