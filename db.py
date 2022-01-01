# import mysql.connector
import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


# mydb = mysql.connector.connect(
#   host=os.getenv('mysql_host'),
#   port=os.getenv('mysql_port'),
#   user=os.getenv('mysql_user'),
#   password=os.getenv('mysql_pass'),
#   database=os.getenv('mysql_db')
# )

host=os.getenv('mysql_host')
port=os.getenv('mysql_port')
user=os.getenv('mysql_user')
pwd=os.getenv('mysql_pass')
database=os.getenv('mysql_db')

connection_uri=f"mysql://{user}:{pwd}@{host}:{port}/{database}"
# print(con)
engine = create_engine(connection_uri,echo=False)
print(connection_uri)
meta=MetaData()

conn=engine.connect()


users = Table('users', meta, Column('id', Integer, primary_key=True),
Column('name', String),)

# s = users.select()
# result=conn.execute(s).fetchall()

# print(result)
