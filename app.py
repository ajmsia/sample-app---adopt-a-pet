from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attendance/<Subject>')
def lisub(Subject):
    Datec = readatbysub(Subject)
    return render_template('subjects.html',Subject=Subject, attendance=Datec)

@app.route('/attendance/<Date>')
def ddate(Date):
    Namec = readatbydate(Date)
    return render_template('dates.html', Namec=Namec, attendance=Namec)

if __name__ == '__main__':
    app.run(debug=True)