import random

def guessing_game():
    answer = random.randint(0,100)
    while True:
            user_guess = int(input("Cual es el mumero? "))
            if answer == user_guess:
                print("Adivinaste !!!!")
                break
            elif answer<user_guess:
                print(" El numero suyo es mayor !!!!")
            else:
                print("El numero suyo es menor !!!!")
        

    
guessing_game()