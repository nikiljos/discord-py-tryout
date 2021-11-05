import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  port=3000,
  user="root",
  password=os.getenv('mysql_pass'),
  database='mutask'
)

