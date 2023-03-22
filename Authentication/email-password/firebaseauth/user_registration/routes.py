from flask import Blueprint,render_template,url_for, flash, redirect, request, abort, session
from firebaseauth import app, auth
from firebaseauth.user_registration.forms import RegistrationForm


# Blueprint Object
userRegistration = Blueprint('user_registraiton', __name__, template_folder='templates')


# User Registration
@userRegistration.route('/', methods=['POST', 'GET'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = auth.create_user_with_email_and_password(form.email.data, form.password.data)
            flash("User Registration successful", 'success')
            return redirect(url_for('user_login.login'))
        except:
            flash(f"Invalid Email address or Password",'danger')
    return render_template('user_registration/register.html', title="Firebase | Registration", form=form)
