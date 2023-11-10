import requests

VALIDATE_URL = "https://fr1gi6xdtc.execute-api.us-west-2.amazonaws.com/prod/validate"

def validateForm (form : dict) -> bool:
   keys = ["pain_level","head_trauma","allergies","runny_nose","sore_throat","shortness_of_breath","inflammation","fever","cough","chest_pain","breathing_difficulty"]
   for key in keys:
      if key not in form:
        return False
   return True

def validateRequest (username : str, token: str, api_key : str):
   response = requests.get(VALIDATE_URL,
                           params={"username":username,"token":token},
                           headers={"X-Api-Key":api_key})
   return response.status_code == 200
   