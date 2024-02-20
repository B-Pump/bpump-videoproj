from main import Exercices

user_input = input("Quel exercice veux-tu faire ?\n1 - Curl\n2 - Squats\n3 - Pompes\n4 - Burpees\n\nRéponse : ")

if user_input == "1":
    Exercices().start("curl")
elif user_input == "2":
    Exercices().start("squat")
elif user_input == "3":
    Exercices().start("pushup")
elif user_input == "4":
    Exercices().start("burpees")