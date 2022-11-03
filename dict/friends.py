dict_friends={
    "1":"Mario",
    "2":"Diego",
    "3":"Ana Maria",
    "4":"Sofia"
}

dict_friends["5"]="Juanchi"

print(dict_friends)

if ("Diego Armando" in dict_friends.values()):
    print("Es un amigo!")
else:
    print("No es un amigo. :(")
