from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import pyrebase
from random import randint as rt
#nome+contato+tipofoto.jpg


app = Flask(__name__)


Config = {
  "apiKey": "AIzaSyAXal4EpjRrRwbw3ZbOgCp37SwZhntDs6w",
  "authDomain": "relacionamento-d2f2a.firebaseapp.com",
  "projectId": "relacionamento-d2f2a",
  "storageBucket": "relacionamento-d2f2a.appspot.com",
  "databaseURL":"https://relacionamento-d2f2a-default-rtdb.firebaseio.com/",
  "messagingSenderId": "315669792394",
  "appId": "1:315669792394:web:ec4d1689f1e9ea682a4f73",
  "measurementId": "G-1K5LLKBJNM"
}

firebase = pyrebase.initialize_app(Config)

auth = firebase.auth()
storage = firebase.storage()


UPLOAD_FOLDER="geral"

app = Flask(__name__, template_folder="templates")
app.debug=True
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
ALLOWED = set(['png', 'jpg', 'jpeg', 'gif'])


@app.route('/curriculo')
def curriculo():
   return render_template('curriculo.html')
   
   
   
 
@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == "POST":
        id = rt(1,100)
        id = str(id)
        if "frenterg" not in request.files:
            return "there is no file1 in form!"
        nome = request.form["nome"]
        file1 = request.files["frenterg"]
        file2 = request.files["versorg"]
        file3 = request.files["selfierg"]
        file1.save("geral/frente.png")
        storage.child(f"{nome}/frente.jpg").put(file1)
        storage.child(f"{nome}/verso.jpg").put(file2)
        storage.child(f"{nome}/selfie.jpg").put(file3)
        return render_template("sucesso.html")
app.run(host='0.0.0.0', port=8080)
