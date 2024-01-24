from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Variables en las rutas'

#Listado de metodos GET, POST, PUT, PATCH, DELETE
@app.route('/post/<post_id>' , methods=['GET'])
def lala(post_id):
    return 'el id del post es: ' + post_id

#
@app.route('/post/<post_id>' , methods=['POST'])
def lili(post_id):
    return 'el id del post es: ' + post_id

@app.route('/pues/<post_id>' , methods=['GET','POST'])
def pues(post_id):
    if request.method == 'GET':
        return 'el id del post por el metodo get es: ' + post_id
    else:
        return 'Estas usando otro metodo distinto al get'

if __name__== '__main__':
    app.run(debug=True,
            port=5000)
    