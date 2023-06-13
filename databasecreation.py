import sqlite3


connection=sqlite3.connect("Users.db")
cursor = connection.cursor()


cursor.execute("create table Users(name text,email text,password text)")


connection.close()
