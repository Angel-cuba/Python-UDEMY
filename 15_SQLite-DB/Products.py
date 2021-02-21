import sqlite3

connect = sqlite3.connect("Product.db")

cursor = connect.cursor()
cursor.execute('''CREATE TABLE PRODUCTS(
                                        CODIGO_P VARCHAR(10)PRIMARY KEY,
                                        NOMBRE_P VARCHAR(20),
                                        SECCION_P VARCHAR(20)
)''')

product=[
          ('ar1', 'Milk','Lacteo'),
          ('ar2', 'Planta', 'Jardín'),
          ('ar3', 'Pizza', 'Panaderia')
]

cursor.executemany("INSERT INTO PRODUCTS VALUES(?,?,?)", product)

connect.commit()
connect.close()