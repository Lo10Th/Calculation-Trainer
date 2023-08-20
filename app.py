from flask import Flask, render_template
from flask import request, jsonify
from random import randint
import sqlite3
from pathlib import Path

app = Flask(__name__)

db_path = Path("points_data.db")

conn=sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS points_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        points INTEGER
    )
''')

conn.commit()
conn.close()

def add_points(points):
    conn=sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO points_data (points)
        VALUES (?)
    ''', (points,))

    conn.commit()
    conn.close()

def get_points():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(points) FROM points_data")
    total_points = cursor.fetchone()[0]
    conn.close()
    return total_points

def getQuestion(howbig, difference, html):
    qn1 = randint(1, howbig)
    qn2 = randint(1, howbig)
    questionint = qn1 * qn2
    question = str(qn1) + "x" + str(qn2)
    smramount = randint(1, 3)

    a1 = questionint
    a2 = questionint
    a3 = questionint

    if smramount == 1:
        correctAnswer = "a1"
        if randint(1, 2) == 1:
            a2 = questionint + randint(1, difference)
        else:
            a2 = questionint - randint(1, difference)
        if randint(1, 2) == 1:
            a3 = questionint + randint(1, difference)
        else:
            a3 = questionint - randint(1, difference)

    elif smramount == 2:
        correctAnswer = "a2"
        if randint(1, 2) == 1:
            a1 = questionint + randint(1, difference)
        else:
            a1 = questionint - randint(1, difference)
        if randint(1, 2) == 1:
            a3 = questionint + randint(1, difference)
        else:
            a3 = questionint - randint(1, difference)

    else:
        correctAnswer = "a3"
        if randint(1, 2) == 1:
            a1 = questionint + randint(1, difference)
        else:
            a1 = questionint - randint(1, difference)
        if randint(1, 2) == 1:
            a2 = questionint + randint(1, difference)
        else:
            a2 = questionint - randint(1, difference)

    return render_template(html, question=question, answer=correctAnswer, a1=a1, a2=a2, a3=a3)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add_1point", methods=["POST"])
def add_1point():
    add_points(1)
    return jsonify({"message": "Point added successfully"})

@app.route("/add_3points", methods=["POST"])
def add_3points():
    add_points(3)
    return jsonify({"message": "Point added successfully"})

@app.route("/add_10points", methods=["POST"])
def add_10points():
    add_points(10)
    return jsonify({"message": "Point added successfully"})

@app.route("/add_20points", methods=["POST"])
def add_20points():
    add_points(20)
    return jsonify({"message": "Point added successfully"})

@app.route("/small1x1")
def small1x1():
    return getQuestion(10, 5, 'small1x1.html')

@app.route("/1x1upto20")
def upto20():
    return getQuestion(20, 12, '1x1upto20.html')


@app.route("/1x1upto50")
def upto50():
    return getQuestion(50, 15, '1x1upto50.html')


@app.route("/1x1upto100")
def upto100():
    return getQuestion(100, 25, '1x1upto100.html')


if __name__ == '__main__':
    app.run(debug=True, port=5500, host='0.0.0.0')