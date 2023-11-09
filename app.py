#openapi: 3.0.0
#info:
# version: "1.0.0"
#  title: TraigeMS
#description: The API to determine Triage results based on a form

import os,json
from decouple import config
from os import environ
from triage import validateForm
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


API_KEY = config('API_KEY')

formInput = {
    "pain_level":9,
    "allergies":True,
    "runny_nose":True,
    "sore_throat":True,
    "shortness_of_breath":True,
    "inflammation":"mild",
    "fever":True,
    "cough":True,
    "chest_pain":True,
    "breathing_difficulty":True
}



@app.route('/')
def index():
   return render_template('index.html')


@app.route('/triage')
def triageSymptoms():
  if (not validateForm(formInput)):
     return "Invalid Form"
  else:
     return "Continue Triage"


if __name__ == '__main__':
   app.debug=True;
   app.run()
