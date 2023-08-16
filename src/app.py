from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/small1x1")
def small1x1():
    qn1 = randint(1, 10)
    qn2 = randint(1, 10)
    questionint = qn1 * qn2
    question = str(qn1) + "x" + str(qn2)
    smramount = randint(1, 3)

    a1 = questionint
    a2 = questionint
    a3 = questionint

    if smramount == 1:
        correctAnswer = "a1"
        if randint(1, 2) == 1:
            a2 = questionint + randint(1, 5)
        else:
            a2 = questionint - randint(1, 5)
        if randint(1, 2) == 1:
            a3 = questionint + randint(1, 5)
        else:
            a3 = questionint - randint(1, 5)

    elif smramount == 2:
        correctAnswer = "a2"
        if randint(1, 2) == 1:
            a1 = questionint + randint(1, 5)
        else:
            a1 = questionint - randint(1, 5)
        if randint(1, 2) == 1:
            a3 = questionint + randint(1, 5)
        else:
            a3 = questionint - randint(1, 5)

    else:
        correctAnswer = "a3"
        if randint(1, 2) == 1:
            a1 = questionint + randint(1, 5)
        else:
            a1 = questionint - randint(1, 5)
        if randint(1, 2) == 1:
            a2 = questionint + randint(1, 5)
        else:
            a2 = questionint - randint(1, 5)

    return render_template('small1x1.html', question=question, answer=correctAnswer, a1=a1, a2=a2, a3=a3)


@app.route("/1x1upto20")
def upto20():
    return render_template('1x1upto20.html')


@app.route("/1x1upto50")
def upto50():
    return render_template('1x1upto50.html')


@app.route("/1x1upto100")
def upto100():
    return render_template('1x1upto100.html')


if __name__ == '__main__':
    app.run(debug=True, port=5500, host='0.0.0.0')