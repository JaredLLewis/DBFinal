import pymysql
import MySQLdb




conn = pymysql.connect(host="us-cdbr-iron-east-05.cleardb.net", user="b07f9bd28a1df0", password="68ccaea4", port=3306, database="heroku_bafe54ca91a5de3")
cursor = conn.cursor()

sql = 'select * FROM Student'
cursor.execute(sql)

datos = cursor.fetchall()
print(datos)
