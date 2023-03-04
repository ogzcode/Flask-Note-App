import sqlite3

connection = sqlite3.connect("database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO notes (title, content) VALUES (?,?)",
            ("First Post",
             """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse 
            sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque"""
             )
            )

cur.execute("INSERT INTO notes (title, content) VALUES (?,?)",
            ("Second Post",
             """Lorem ipsum dolor, sit amet consectetur adipisicing elit.Esse 
            sapiente ullam consectetur placeat ex amet maxime non accusamus saepe eaque"""
             )
            )

connection.commit()
connection.close()