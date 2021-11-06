import mysql.connector
import os

mydb = mysql.connector.connect(
  host=os.getenv('mysql_host'),
  port=os.getenv('mysql_port'),
  user=os.getenv('mysql_user'),
  password=os.getenv('mysql_pass'),
  database=os.getenv('mysql_db')
)

