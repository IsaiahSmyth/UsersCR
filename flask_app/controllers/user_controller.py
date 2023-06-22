from flask_app import app
from flask_app.model.user_model import User
from flask import render_template, redirect, session, request


@app.route('/')
def Home():
    all_users = User.get_all()
    print(all_users)
    return render_template('read(all).html', all_users = all_users)


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

# =================================================
#       Update Routes
#       Show Updae Form Route,
#           Submit Update Form Route
# =================================================

@app.route('/update/<int:id>')
def update(id):
    one_user = User.get_one({'id' : id})
    return render_template ('edit.html', one_user = one_user)

@app.route('/edit', methods=['POST'])
def edit_form():
    User.update_user(request.form)
    return redirect ('/')

@app.route('/read(one)/<int:id>')
def show_edit_form(id):
    # Use id from the parameter of the route, to inform our get_one method!
    
    one_user = User.get_one({'id' : id})
    return render_template('read(one).html', one_user = one_user)



# ==================================================
#           Delete
# ==================================================

@app.route('/delete/<int:id>')
def delete(id):
    User.delete_user({'id' : id})
    return redirect('/')