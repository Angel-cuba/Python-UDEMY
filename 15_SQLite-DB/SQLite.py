import sqlite3

connect = sqlite3.connect("PrimeraDB.db")#Se establece la conexión



cursor = connect.cursor()
# cursor.execute("CREATE TABLE USERS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(10))")

# cursor.execute("INSERT INTO USERS VALUES('Vera', 2, 'femenino')")

# cursor.execute("SELECT * FROM USERS")
# USER = cursor.fetchall()
# print(USER)

# user = [
#           ('Maria', 39, 'femenino'),
#           ('John', 40, 'femenino'),
#           ('Luis', 32, 'masculino')
# ]
# cursor.executemany("INSERT INTO USERS VALUES(?,?,?)", user)

cursor.execute("SELECT * FROM USERS")
users = cursor.fetchall()
# print(users)
for user in users:
          print("-->",user)

connect.commit()

connect.close()