#insert into MySql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="biello_database"
)

mycursor = mydb.cursor()

sql = "INSERT INTO compagnibresso (nome, cognome) VALUES (%s, %s)"
val = ("Christian", "Testa")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")