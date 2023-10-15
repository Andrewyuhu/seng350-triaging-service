import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/triage', methods=["POST"])
def triageSymptoms(symptomInput):
   
   result = "Please visit ER for further triage."

   if (symptomInput["head_trauma"] == True):
      result = "Please visit ER for treatment"
   elif (symptomInput["allergies"] == True):
      result = "Visit drug store for allergy medicene"
   elif (symptomInput["inflamation"] == "moderate" or symptomInput["inflamation"] == "moderate"):
        result = "Please visit ER for further triage."

   return {"result":result}




if __name__ == '__main__':
   app.run()