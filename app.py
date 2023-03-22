# Reference: https://www.yan-holtz.com/index.html
# - Top part uses <canvas> and 'particles'

from flask import Flask, render_template

app = Flask(__name__)

# home page
@app.route("/")
def home():
    return render_template('home.html')

# 404-redirect logic
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
