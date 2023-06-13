from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attend/<course>')
def attend(course):
    date = readatbycourse(course)
    return render_template('course.html', course=course, date=date)

@app.route('/attend/<date>')
def attendees(date):
    attendee = readatbydate(date)
    return render_template('date.html', date=date, attendee=attendee )    

if __name__ == '__main__':
    app.run(debug=True)
