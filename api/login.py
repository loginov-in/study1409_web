from main import *
from flask import  Flask, render_template, redirect, request, send_file, redirect, abort, session, url_for, make_response, jsonify




# Fronnded #
@app.route("/")
def login():
    return render_template("login.html")