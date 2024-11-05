# Database initialization


import sqlite3
connection = sqlite3.connect('database.db')




# Initializing table for student tasks
with open('students.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()




# Generic students
cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (1,'Bobby','Drake'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (2,'Ororo','Monroe'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (3,'Jean','Grey'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (4,'Scott','Summers'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (5,'Hank','McCoy'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (6,'Kurt','Wagner'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (7,'Alex','Summers'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (8,'Kitty','Pryde'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (9,'Remy','LeBeau'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (10,'Emma','Frost'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (11,'Cain','Marko'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (12,'Raven','Darkholm'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (13,'Victor','Creed'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (14,'Simon','Lasker'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (15,'James','Howlett'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (16,'Warren','Worthington'))

cur.execute("INSERT INTO students (id, firstName, lastName) VALUES (?,?,?)",
            (17,'Wade','Wilson'))


f.close()




# Initializing table for attendance
with open('attendance.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()
f.close()

connection.commit()
connection.close()
