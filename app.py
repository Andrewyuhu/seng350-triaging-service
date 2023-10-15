import os,json

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')



# example = {
#     "pain_level":0,
#     "head_trauma":False,
#     "allergies":True,
#     "runny_nose":True,
#     "sore_throat":True,
#     "shortness_breathe":True,
#     "inflammation":"mild",
#     "fever":True,
#     "cough":True,
#     "chest_pain":True,
#     "difficult_breathing":True
# }

@app.route('/triage', methods=["POST"])
def triageSymptoms():
   symptomInput = request.json # JSON Body
   result = "Please visit ER for further triage." # Default Triage Result
  # Check the answers to determine the appropriate result
   if symptomInput["pain_level"] >= 8:
        result = "Please visit the ER for treatment."
   else:
      if symptomInput["head_trauma"]:
          result = "Please visit the ER for evaluation."
      elif symptomInput["inflammation"] in ["moderate", "severe"]:
          result = "Please visit the ER for further triage."
      elif symptomInput["allergies"]:
          if symptomInput["runny_nose"] and symptomInput["sore_throat"]:
              result = "You may have seasonal allergies. Consider antihistamines."
          elif symptomInput["shortness_of_breath"]:
              result = "Please visit the ER due to allergies and shortness of breath."
          else:
              result = "Visit a drug store for allergy medication."
      elif symptomInput["chest_pain"]:
        result = "Please visit the ER due to chest pain."
      elif symptomInput["breathing_difficulty"]:
        result = "Please visit the ER due to breathing difficulty."
      else:
          if symptomInput["fever"]:
            if symptomInput["cough"]:
                result = "You may have the flu. Consult a healthcare provider."
            else:
                if symptomInput["runny_nose"]:
                    result = "You may have a common cold. Rest and fluids."
                else:
                    result = "You may have an infection. Consult a healthcare provider."

   

  #  if (symptomInput["head_trauma"] == True):
  #     result = "Please visit ER for treatment"
  #  elif (symptomInput["allergies"] == True):
  #     result = "Visit drug store for allergy medicene"
  #  elif (symptomInput["inflamation"] == "moderate" or symptomInput["inflamation"] == "moderate"):
  #       result = "Please visit ER for further triage."

   return {"result":result}




if __name__ == '__main__':
   app.run()