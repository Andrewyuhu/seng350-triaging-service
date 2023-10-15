import os,json

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/triage', methods=["POST"])
def triageSymptoms():
   
   symptomInput = request.json # JSON Body
   result = "Please visit ER for further triage." # Default Triage Result

  # Pain Level 
   if symptomInput["pain_level"] >= 7:
        result = "Please visit the ER for treatment."
   else:
      
      # Head Trauma
      if symptomInput["head_trauma"]:
          result = "Please visit the ER for evaluation."

      # inflammation
      elif symptomInput["inflammation"] in ["moderate", "severe"]:
          result = "Please visit the ER for further triage."

      # Chest Pain
      elif symptomInput["chest_pain"]:
        result = "Please visit the ER due to chest pain."

      # Breathing
      elif symptomInput["breathing_difficulty"]:
        result = "Please visit the ER due to breathing difficulty."

      # Allergy Symptoms
      elif symptomInput["allergies"]:
          if symptomInput["runny_nose"] and symptomInput["sore_throat"]:
              result = "You may have seasonal allergies. Consider antihistamines."
          elif symptomInput["shortness_of_breath"]:
              result = "Please visit the ER due to allergies and shortness of breath."
          else:
              result = "Visit a drug store for allergy medication."
      
      # Generic Cold Symptoms
      else:
          if symptomInput["fever"]:
            if symptomInput["cough"]:
                result = "You may have the flu. Consult a healthcare provider."
            else:
                if symptomInput["runny_nose"]:
                    result = "You may have a common cold. Rest and fluids."
                else:
                    result = "You may have an infection. Consult a healthcare provider."

   return {"result":result}




if __name__ == '__main__':
   app.run()