from flask import Blueprint,render_template,url_for, flash, redirect, request, abort, session
from firebaseauth import app, auth
from firebaseauth.user_login.forms import LoginForm


# Blueprint Object
userLogin = Blueprint('user_login', __name__, template_folder='templates')

# Login Page
@userLogin.route('/', methods=['POST','GET'])
def login():
    form = LoginForm()
    return render_template('user_login/login.html', title="Firebase | Login", form=form)