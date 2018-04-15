from flask import Flask, g, render_template, url_for

from os import path
import os
import sqlite3

print("current %s" % path.curdir)


app = Flask(__name__)
rel = os.path.join(app.root_path, 'sample.db')
app.database = "C:\\Users\\leeja\\PycharmProjects\\DBFinal\\sample.db"

@app.route('/')
def index():

    g.db = sqlite3.connect(rel)
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()

    return render_template('index.html', posts=posts)



@app.route('/about')
def about():
    return render_template('about.html')
def connect_db():

    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run()



