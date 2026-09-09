from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World from Kavin Seralathan. I am a student.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)