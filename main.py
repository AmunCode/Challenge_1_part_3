#Below is a function about a person biography#
def biography():
  print("Let's get acquainted!!")
  user_surname = input("What's your surname?\n")
  user_height = int(input ("How tall are you in centimeter?\n"))
  user_age = int(input("How old are you?\n"))
  user_weight = float(input("How much do you weight in pounds?\n "))
  user_eyes_color = input("What color are your eyes?\n ")
  user_fav_color = input("What is your favorite color?\n ")
  user_race = input("What race are you?\n ")
  user_languages = input("How many languages do you speak?\n ")
  user_residing_state = input("What state are you currently residing?\n ")
  user_birth_month = input("What is your birth month?\n ")
  user_ethnicity = input("What is your ethnicity?\n ")
  user_denomination = input("What is your religious background?\n ")
  print(f"Well, this is what I've learned about you thus far. Your last name is {user_surname}. You are a {user_denomination} residing in {user_residing_state}. You are {user_age} years old. you are about {user_height} centimeters tall and weight about {user_weight} pounds. You have {user_eyes_color} eyes. Furthermore, you are from a {user_race} race and speak about {user_languages} languages. Oh, yeah, you was born in the month of {user_birth_month} and your favorite color is {user_fav_color}.")

biography()