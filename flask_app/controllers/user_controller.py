from flask_app import app
from flask_app.model.user_model import User
from flask import render_template, redirect, session, request


@app.route('/')
def Home():
    all_users = User.get_all()
    print(all_users)
    return render_template('read.html', all_users = all_users)


@app.route('/add_user')
def add_user():
    
    return render_template('create.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    user = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.add_user(user)
    
    return redirect('/')

# @app.route('/show', methods=['POST'])
# def show():

#     return render_template('read.html')