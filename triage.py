def validateForm (form : dict) -> bool:
   keys = ["pain_level","head_trauma","allergies","runny_nose","sore_throat","shortness_of_breath","inflammation","fever","cough","chest_pain","breathing_difficulty"]
   for key in keys:
      if key not in form:
        return False
   return True