import random

tips = {
   "syntax": [
      "Check for any missing colons in your code.",
      "Are all your brackets and parentheses properly closed?",
      "Check for inconsistent indentation in your code.",
      "Verify that your function definitions are correctly formatted.",
      "Ensure that your strings have matching quotes (' or \")."
   ],
   "runtime": [
      "Check if all your variables are declared before using them.",
      "Make sure list indices are within a valid range.",
      "Are you trying to divide by 0? This will cause an error.",
      "Double-check that you have the correct data types in operations.",
      "Use print statements to find where the error occurs."
   ],
   "logic": [
      "Walk through your code manually to find where the error is.",
      "Print values inside any loops you have.",
      "Make sure any arithmetic calculations are correct.",
      "Check for off-by-one errors in any loops or variables.",
      "Make sure that your data types are correctly used."
   ]
}

def debug_tip(error_type):
   error_type = error_type.lower()

   if error_type in tips:
      return random.choice(tips[error_type])
   return "Unknown error type. Enter 'syntax', 'runtime', or 'logic'."