import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')
  
@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
	if "firstName" not in session:
		session["firstName"]=request.form['firstName']
		session["lastName"]=request.form['lastName']
	return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
	if "birthCity" not in session:
		session["birthCity"]=request.form['birthCity']
	return render_template('page3.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
	if "birthYear" not in session:
		session["birthYear"]=request.form['birthYear']
	return render_template('page4.html')

@app.route('/page5',methods=['GET','POST'])
def renderPage5():
	if "favSeason" not in session:
		session["favSeason"]=request.form['favSeason']
	return render_template('page5.html')

@app.route('/page6',methods=['GET','POST'])
def renderPage6():
	if "luckyNumber" not in session:
		session["luckyNumber"]=request.form['luckyNumber']
	return render_template('page6.html')

@app.route('/page7',methods=['GET','POST'])
def renderPage7():
	if "food" not in session:
		session["food"]=request.form['food']
	return render_template('page7.html')

@app.route('/page8',methods=['GET','POST'])
def renderPage8():
	if "animal" not in session:
		session["animal"]=request.form['animal']
	return render_template('page8.html')

@app.route('/page9',methods=['GET','POST'])
def renderPage9():
	if "verb" not in session:
		session["verb"]=request.form['verb']
	return render_template('page9.html')

@app.route('/page10',methods=['GET','POST'])
def renderPage10():
	if "adjective" not in session:
		session["adjective"]=request.form['adjective']
	return render_template('page10.html')

@app.route('/page11',methods=['GET','POST'])
def renderFinal():
	if "timeOfDay" not in session:
		session["timeOfday"]=request.form['timeOfday']
	return render_template('final.html')

    
if __name__=="__main__":
    app.run(debug=True)
