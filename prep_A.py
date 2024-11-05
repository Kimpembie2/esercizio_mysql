import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")
mycursor.execute("Use Animali")
mycursor.execute("CREATE TABLE IF NOT EXISTS Mammiferi (id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(255), razza VARCHAR(255), peso INT, eta INT)")