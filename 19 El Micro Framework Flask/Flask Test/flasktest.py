from flask import Flask

app = Flask(__name__)

@app.route("/D/Documentos/Curso 2/Curso-2/19 El Micro Framework Flask/Flask Test")
def hello_world():
    return "<p>Hello, World!</p>"