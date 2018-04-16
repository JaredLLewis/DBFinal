from flask import Flask, g, render_template, url_for
import sqlite3
import pymysql

conn = pymysql.connect(host="us-cdbr-iron-east-05.cleardb.net", user="b07f9bd28a1df0", password="68ccaea4",
                        database="heroku_bafe54ca91a5de3")
cursor = conn.cursor()


app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')



@app.route('/about')
def about():
    sql = 'select * FROM Student'
    cur = cursor.execute(sql)
    students = [dict(StudentMUNumber=row[0], StaffNumber=row[1], StudentFirstName=row[2], StudentLastName=row[3]) for row in cursor.fetchall()]
    return render_template('about.html', students=students)
@app.route('/diagram')
def diagram():
    return render_template('diagram.html')

if __name__ == '__main__':
    app.run()



