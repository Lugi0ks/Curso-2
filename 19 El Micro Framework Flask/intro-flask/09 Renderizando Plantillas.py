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
    return render_template("lele.html")

# if __name__== '__main__':
#     app.run(debug=True,
#             port=5000)
    