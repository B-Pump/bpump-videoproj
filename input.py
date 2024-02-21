from main import Exercises  # Importing the Exercises class from main.py

# Asking for user input
user_input = input("Which exercise do you want to do?\n1 - Curl\n2 - Squats\n3 - Pushups\n4 - Burpees\n\nResponse: ")

# Starting the exercise based on user input
if user_input == "1":
    Exercises().start("curl")
elif user_input == "2":
    Exercises().start("squat")
elif user_input == "3":
    Exercises().start("pushup")
elif user_input == "4":
    Exercises().start("burpees")