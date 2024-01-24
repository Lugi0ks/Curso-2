from flask import Flask, request
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
    
@app.route('/lele', methods=["POST"])
def lele():
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'lele'

if __name__== '__main__':
    app.run(debug=True,
            port=5000)
    