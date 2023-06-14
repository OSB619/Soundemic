from flask import Flask, render_template, request, flash, redirect
import sqlite3
import cv2
from deepface import DeepFace
import subprocess


connection=sqlite3.connect("Users.db", check_same_thread=False)
cursor = connection.cursor()




app=Flask(__name__)
app.secret_key="akhfkadjfkwehfkadj234cw9e!@#$(#"

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/register")
def register():
	return render_template("regis.html")


@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/terms")
def terms():
	return render_template("terms.html")


@app.route("/regiscom", methods=["POST","GET"])
def regiscom():
        
        em=str(request.form['email'])
        print(em)
        cursor.execute("select password from Users where email=?",[em])
        pswd=cursor.fetchone()
        
        if pswd is None:
                if str(request.form['password']) == str(request.form['confirm-password']) :
                        cursor.execute("insert into Users values(?,?,?)", [str(request.form['name']),str(request.form['email']),str(request.form['password'])])
                        cursor.execute("select * from Users")
                        usrs=cursor.fetchall()
                        connection.commit()
                        print(usrs)
                        return render_template("regiscom.html")

                else:
                        flash('Password do not match')
                        return render_template("regis.html")
        else:
                flash('User Already Exists!!!')
                return render_template("regis.html")

@app.route("/loginSuccesswithcam", methods=["POST","GET"])
def loginSuccesswithcam():
	em=str(request.form['email'])
	print(em)
	cursor.execute("select password from Users where email=?",[em])
	pswd=cursor.fetchone()

	if pswd is None:
		flash('User not found!!')
		return render_template("login.html")

	else:
		
		if pswd[0]== str(request.form['password']):

			return render_template("loginSuccesswithcam.html")

		else:
			flash('Wrong username or password')
			return render_template("login.html")




@app.route("/result")
def result():

        import webbrowser
        
        returned_text = subprocess.check_output('dir /b /o:-d /tw "C:\\Users\\IDZ\\Downloads"', shell=True, universal_newlines=True)
        filename=returned_text.splitlines()[0]
        print(filename)

        user=subprocess.check_output('whoami', shell=True, universal_newlines=True)
        user=user.split('\\')[1].upper().strip()
        

        img=cv2.imread(f"C:\\Users\\{user}\\Downloads\\{filename}")
    
        result =DeepFace.analyze(img,actions=['emotion'],enforce_detection=False)

        emo=result[0]['dominant_emotion']
        print(emo)

        webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={emo}+hindi+songs")



        return render_template("loginSuccesswithcam.html")
