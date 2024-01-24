from flask import Flask, request, url_for, redirect, abort
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo'

@app.route('/pues/<post_id>' , methods=['GET','POST'])
def pues(post_id):
    if request.method == 'GET':
        return 'el id del post por el metodo get es: ' + post_id
    else:
        return 'Estas usando otro metodo distinto al get'
    
@app.route('/lele', methods=['POST','GET'])
def lele():
    abort(401)
    return redirect(url_for('pues', post_id=2))
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    return 'lele'

if __name__== '__main__':
    app.run(debug=True,
            port=5000)
    