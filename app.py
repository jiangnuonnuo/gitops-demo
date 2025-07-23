from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return ("banben1545865!")

@app.route('/info')
def info():
    return "sdf asdf!"

@app.route('/hello')
def hello():
    return "hello3"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)