#select from MySql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="biello_database"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM compagnibresso")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)