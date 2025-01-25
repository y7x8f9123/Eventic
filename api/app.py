from flask import Flask
import auth

app = Flask(__name__)
app.secret_key = b'dev'
app.register_blueprint(auth.bp)

