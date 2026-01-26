user_name = input("Please enter your name:")
user_yob = input("Please enter the year of birth:")
current_year = 2026
age = current_year - int(user_yob)
print("Hello " + user_name + ", you are " + str(age))