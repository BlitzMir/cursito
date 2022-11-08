import random
f= open("Puntaje.txt","a",encoding="utf8")
while True:
    user_action = input("Seleccione (piedra-papel-tijera)")
    possible_action = ["piedra","papel","tijera"]
    computer_action = random.choice(possible_action)
     #print(computer_action)
    print("\nTu elegiste",user_action, " , la computadora eligio",computer_action,"\n")
    if user_action == computer_action:
        print("Empate!",user_action,"Ambos ganaron!")
        f.write("Empate. \n")
    elif user_action=="piedra" and computer_action == "papel":
        print("Gano la Computadora . \n")
        f.write("Gano la Computadora. \n")
    elif user_action=="piedra" and computer_action=="tijera":
        print("Ganaste! . \n")
        f.write("Gano el usuario. \n")
    elif user_action=="papel" and computer_action=="piedra":
        print("Ganaste! . \n")
        f.write("Gano el usuario. \n")
    elif user_action=="papel" and computer_action=="tijera":
        print("Gano la Computadora . \n")
        f.write("Gano la Computadora. \n")
    elif user_action=="tijera" and computer_action=="piedra":
        print("Gano la Computadora . \n")
        f.write("Gano la computadora. \n")
    elif user_action=="tijera" and computer_action=="papel":
        print("Ganaste! . \n")
        f.write("Gano el usuario. \n")
    else:
        print("Error, seleccione bien!")
    play_again = input("Desea jugar nuevamente? (s/n): ")
    if play_again.lower() == 'n':
        break

