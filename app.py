from datetime import timedelta
from flask import Flask,redirect,url_for,render_template,request,session,flash
import urllib.request
import os
from werkzeug.utils import secure_filename
app =Flask(__name__)
app.secret_key="Hello"
app.permanent_session_lifetime=timedelta(minutes=5)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/")
def index():
    if "email" in session:
        email =session["email"]
        return render_template("index.html")
    else:
        return redirect(url_for("login"))
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent=True
        email = request.form["email"]
        password = request.form["pass"]
        if email == "xeyal95281@naluzotan.com" and password =="123" :
           session["email"] =request.form["email"]
           return redirect(url_for("index"))
        else:
            return redirect(url_for("login"))
    else:
        if "email" in session:
                return redirect(url_for("index"))
        return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("email",None)
    return redirect(url_for("login"))
@app.route('/form')
def form():
    return render_template('form.html')
@app.route("/upload-image",methods=["POST"])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/uploads/', filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('form.html',filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
@app.route("/table")
def table():
    imageList = os.listdir('static/uploads')
    imagelist = ['uploads/' + image for image in imageList]
    return render_template("table.html", imagelist=imagelist)
   
if __name__ == "__main__":
    app.run()