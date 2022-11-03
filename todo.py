print("Version 1.1")
tasks=[]
count=int(input('La cantidad de enventos que quiero agendar : '))
file=open("ToDo.txt","w",encoding="utf8")#El UTF8 sirve para utilizar caracterres especiales Ej: "ñ", Tildes, Simbolos Monetarios, etc
aux=0
for i in range(count):  
    aux=aux+1
    new_element=input("¿Que queres agendar? : ") #Se repite las caunt veces
    priority=input("Prioridad del Evento (Rojo: Importante; Amarillo: Intermedia; Verde: Baja Prioridad) : ")
    task_starttime= input("Hora de comienzo del evento : ")
    task_endtime= input("Hora de finalizacion del evento : ")    
    tasks.append(str(aux) + " " + new_element)
    file.write(new_element + "/" + priority + "/" + task_starttime + "hs" + "-" + task_endtime + "hs" +"\n")
print(tasks)
file.close()