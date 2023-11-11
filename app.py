#openapi: 3.0.0
#info:
# version: "1.0.0"
#  title: TraigeMS
#description: The API to determine Triage results based on a form

import os,json
from os import environ
from triage import primaryHandler
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/triage')
def triageSymptoms():
    
    # Processes the form answers in JSON format and returns traige result
    #     ---
    #     post:
    #       description: sends the form answers in json format to the flask server to determine triage result

    #     responses:
    #       200:
    #         description: return triage  in the form of a 3 key dictionary
   #symptomInput = request.json # JSON Body

   symptomInput = {
      "username":"randomUser1",
     "token":"106600925603790991061627252300948002515041739375360403758811620986295048214325",
     "pain_level":0,
     "head_trauma":False,
     "allergies":True,
     "runny_nose":True,
     "sore_throat":True,
     "shortness_of_breath":False,
     "inflammation":"mild",
     "fever":False,
     "cough":False,
     "chest_pain":False,
     "breathing_difficulty":False
  }

   response = primaryHandler(symptomInput)
   return response


@app.route('/heartbeat')
def heartbeart():
   return "End point reachable",200

if __name__ == '__main__':
   app.debug = True
   app.run()