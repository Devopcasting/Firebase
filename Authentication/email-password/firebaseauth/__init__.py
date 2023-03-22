from flask import Flask
import pyrebase

# App Config
app = Flask(__name__)
app.config['SECRET_KEY'] = '878436c0a462c4145fa59eec2c43a66a'

# Firebase config
firebaseConfig = {
  "apiKey": "AIzaSyDS8xeTRcUkgrLmrM2f2JmIdquikLUy88I",
  "authDomain": "flask-c152f.firebaseapp.com",
  "projectId": "flask-c152f",
  "storageBucket": "flask-c152f.appspot.com",
  "messagingSenderId": "865282175598",
  "appId": "1:865282175598:web:605bad1c954c1b63286c7f",
  "measurementId": "G-LEXGZ278E3",
  "databaseURL": ""
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


from firebaseauth.user_registration.routes import userRegistration
from firebaseauth.user_login.routes import userLogin

app.register_blueprint(user_login.routes.userLogin,url_prefix='/')
app.register_blueprint(user_registration.routes.userRegistration,url_prefix='/register')

