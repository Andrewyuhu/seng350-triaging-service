def validateForm (form : dict) -> bool:
   keys = ["pain_level","head_trauma","allergies","runny_nose","sore_throat","shortness_of_breath","inflammation","fever","cough","chest_pain","breathing_difficulty"]
   if (keys not in form):
     print("invalid form")
     return False;
   print("valid form")
   return True