import pymysql

with pymysql.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("""DROP TABLE posts""")
    c.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
    c.execute('INSERT INTO posts VALUES("GOOD", "PLEASE WORK")')
    c.execute('INSERT INTO posts VALUES("GOODdee", "yesdee")')


