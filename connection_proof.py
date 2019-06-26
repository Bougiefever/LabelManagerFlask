import pyodbc
from dotenv import load_dotenv, dotenv_values
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
#labelingserver.database.windows.net
# server_name = 'labelingserver'
server_name = os.getenv('SQL_SERVER_NAME')
server = '{}.database.windows.net'.format(server_name)
database = 'labelingdb'
username = 'labelingadmin@{}'.format(server_name)
password = 'Achievement2019'

values = dotenv_values()

conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password
#conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=adlabeling.database.windows.net;PORT=1433;DATABASE=adlabelingdb;UID=sqladmin@adlabeling;PWD=Volunteer2018"
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()

print(conn_str)
print('Using the following SQL Server version:')
tsql = "SELECT @@version;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    print(str(row[0]))

tsql = "SELECT jobs.name AS jobs_name FROM jobs"
with cursor.execute(tsql):
    row = cursor.fetchone()
    print(str(row[0]))