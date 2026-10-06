from main import *
from flask import  Flask, render_template, redirect, request, send_file, redirect, abort, session, url_for, make_response, jsonify




# Fronnded #
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/help")
def help_page():
    return render_template("help.html")

@app.route("/apps")
def apps_page():
    return render_template("apps.html")

@app.route("/apps-pc")
def apps_page_pc():
    return render_template("apps-pc.html")