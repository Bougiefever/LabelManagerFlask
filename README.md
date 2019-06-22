# Label Manager Reference Architecture

## Set up
Create a python environment and install all the packages from the requirements.txt file that you will need into your environment.

```
pip install -r requirements.txt
```

## Database
This example uses an Azure SQL Server database with Flask-SQLAlchemy. You should create a SQL Server in Azure and two databases. One is for production and the other is for testing.

### Database initialization
To create db tables, open a flask shell and run db.create_all().

To drop all db tables:

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