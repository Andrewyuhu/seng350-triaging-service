import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/triage')
def triageSymptoms():
   return "successful loading page"




if __name__ == '__main__':
   app.run()