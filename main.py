import config
from flask import Flask, render_template, redirect, request, send_file, redirect, abort, session, url_for, make_response, jsonify
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from datetime import timedelta


app = Flask(__name__)
app.config.update(SECRET_KEY=config.SECRET_KEY)
app.permanent_session_lifetime = timedelta(days=365)





from api.login import *











if __name__ == "__main__":
    app.run(debug=True, port=7809)