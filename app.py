from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return ("1856375723")

@app.route('/info')
def info():
    return "sdf asdf!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)