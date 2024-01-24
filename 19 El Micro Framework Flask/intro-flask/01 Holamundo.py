from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/lala')
def lala():
    return 'lala'

@app.route('/lele')
def lele():
    return 'lele'

@app.route('/cosa')
def cosa():
    return 'cosa'

if __name__== '__main__':
    app.run(debug=True,
            port=5000)
    