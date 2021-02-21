import sqlite3

connect = sqlite3.connect("Personas.db")

cursor= connect.cursor()
cursor.execute('''CREATE TABLE Personas(
                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       NOMBRE VARCHAR(50),
                       SECCION VARCHAR(50)
                     )''')



personas = [
          ('Leche', 'Lacteo'),
          ('Tomate', 'Agro'),
          ('Carne', 'Carniceria')
]

cursor.executemany("INSERT INTO Personas VALUES(NULL,?,?)", personas)




connect.commit()
connect.close()