from flask import Flask, render_template, request, redirect	
app = Flask(__name__)
@app.route('/')
def hello():
	return "<p>Welcome to my Landing Page!!</p> <p> Enter localhost:5000/ninjas to see ninja page</p><p>Enter localhost:5000/dojos/new to see the dojo page</p>"

@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
	return render_template('dojos.html')

@app.route('/newUser', methods=['POST'])
def new():
	name = request.form['name'],
	email = request.form['email'],
	contact = request.form['phone'],
	return redirect('/dojos/new')
app.run(debug=True)

