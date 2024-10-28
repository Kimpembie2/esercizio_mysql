#creare una tabella in MySql

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="biello_database"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE compagnibresso (nome VARCHAR(255), cognome VARCHAR(255))")