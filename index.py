from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hola'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hola, {name}'


if __name__ == "__main__":
    app.run()