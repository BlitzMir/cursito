import random
import pyperclip as pc

def GeneratePassword(x):
    max_char = 0 #define la cantidad de caracteres que va a tener la contraseña.
    if x == "low":
        max_char = 8
    elif x == "middle":
        max_char = 12
    else:
        max_char = 16
    lst_pass = [] #Agrega la contraseña generada de forma aleatoria a un lista.
    lst_char = [] #Va a contener los caracteres posibles para la contraseña.
    for i in range(1, max_char+1):
        lst_char = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","(",")","[","]","$",".","_"]
        character = random.choice(lst_char) #Elije caracteres aleatorios.
        lst_pass.append(character) #Agrega los caracteres a la lista.
    a = "".join(lst_pass) #Hace que la lista pase de verse: ("B","9","Z") a verse: ("B9Z").
    return a

level_security = input("Seleccione el nivel de seguridad (low/middle/high): ")
pw = GeneratePassword(level_security)
print(pw)
pc.copy(pw)