from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Variables en las rutas'

@app.route('/post/<post_id>')
def lala(post_id):
    return 'el id del post es: ' + post_id

@app.route('/lele')
def lele():
    return 'lele'


if __name__== '__main__':
    app.run(debug=True,
            port=5000)
    