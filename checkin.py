from flask import Flask, render_template, redirect, request, flash, url_for, g
from flask import session as fsession
import model
import datetime

app = Flask(__name__)


# @app.before_request
# def set_up_db():
#     g.db = model.connect_db()

# @app.teardown_request
# def disconnect_db(e):
#     g.db.close()


@app.route("/authenticate", methods=["POST"])
def authenticate():
    print "AUTHEN STARTING"
    email = request.form["email"]
    password = request.form["password"]
    """ HERE'S THE PROBLEM IT'S NOT GETTING ANYTHING FROM REQUEST"""
    print email, password
    user_id = model.authenticate(email, password) #(g.db, email, password)?
    if user_id:
    	fsession["user_id"] = user_id
    	fsession["email"] = email
    	return redirect("/")
    else:
    	flash("I'm sorry, either that password or email is not in our database.")
    	return redirect("/sign_up")


@app.route('/logout', methods=["POST"])
def logout():
    # remove the username from the session if it's there
    fsession.pop('user_id', None)
    fsession.pop('email', None)
	# flash('You have logged out.')
    return redirect(url_for('index'))


@app.route("/")
def index():
	# do sign up stuff here
	instructors = model.session.query(model.User).limit(5).all()
	print "INSTRUCTOHHHHHHHHHHHHHH", instructors[0].id
	return render_template("index.html", instructors=instructors)

@app.route("/fullsched")
def fullsched():
	return render_template("fullsched.html")

@app.route("/sign_up")
def sign_up():
	return render_template("sign_up.html")

@app.route("/sign_in")
def sign_in():
	return render_template("sign_in.html")


@app.route("/change_checkin", methods=["POST"])
def change_checkin():
	in_office = request.form["christian-checkin-office"]
	print in_office
	if in_office:
		# change christian's status to 2
		pass
	return redirect("/")

# def email_exists(email):
# 	email_exists = model.session.query(model.User).filter_by(email = email).first()
# 	if email_exists:
# 		return True
# 	else:
# 		return False


# @app.route("/new_user", methods=["POST", 'GET'])
# def new_user():
# 	error = None
# 	#retrieves form information
# 	new_name = request.form["name"]
# 	new_email = request.form["email"]
# 	new_password = request.form["password"]
# 	new_role = request.form["role"]

# 	#test if new_email exists
# 	if email_exists(new_email) == True:
# 		error = "Sorry, that email was already used. Please use another."
# 		return render_template("sign_up.html", error = error)

# 	else:
# 		#enters info into database
# 		new_user = model.User(Name=new_name, email=new_email, password=new_password, )
# 		model.session.add(new_user)
# 		model.session.commit()

# 		#getting user id
# 		users = model.session.query(model.User).filter_by(email=new_email).all()
# 		return redirect("/index/")

if __name__ == "__main__":
	app.run(debug = True)