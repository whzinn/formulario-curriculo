from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from random import randint as rt
#nome+contato+tipofoto.jpg


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
        file1 = request.files["frenterg"]
        file2 = request.files["versorg"]
        file3 = request.files["selfierg"]

        path1 = os.path.join(app.config["UPLOAD_FOLDER"], id+"frente.jpg")
        path2 = os.path.join(app.config["UPLOAD_FOLDER"], id+"verso.jpg")
        path3 = os.path.join(app.config["UPLOAD_FOLDER"], id+"selfie.jpg")
        file1.save(path1)
        file2.save(path2)
        file3.save(path3)
        return render_template("sucesso.html")
app.run(host='0.0.0.0', port=8080)
