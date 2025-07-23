from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "banben one!"

@app.route('/info')
def info():
    return "wuuwuwuw!"

@app.route('/hello')
def hello():
    return "hello2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)