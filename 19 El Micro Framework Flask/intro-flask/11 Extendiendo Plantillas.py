from flask import Flask, request, url_for, redirect, abort, render_template
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
    return {
        "username":'chanquito feliz',
        "Email":'chanchito@feliz.com'
    }

@app.route ('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola Mundo')

# if __name__== '__main__':
#     app.run(debug=True,
#             port=5000)
    