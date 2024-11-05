import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)
mycursor = mydb.cursor()
sql = "INSERT INTO Mammiferi (id, nome, razza, peso, eta) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('1', 'Leo', 'Leone Africano', 190, 8),
    ('2', 'Bella', 'Golden Retriever', 30, 5),
    ('3', 'Max', 'Elefante africano', 5000, 25),
    ('4', 'Mia', 'Cavallo Purosangue', 500, 7),
    ('5', 'Oliver', 'Koala', 8, 4)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "i record sono stati inseriti")
