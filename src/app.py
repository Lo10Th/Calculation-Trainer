from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/small1x1")
def small1x1():
    return render_template('small1x1.html', correctAnswer="a1", question="1+1", answer="a1", a1=2, a2=3, a3=4, )

if __name__ == '__main__':
    app.run(debug=True, port=5500, host='0.0.0.0')