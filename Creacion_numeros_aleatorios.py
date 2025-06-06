import random #Libreria para llamar numeros random

numeros =[]

for i in range(100): #Ciclo para repetir 100 veces las iteraciones
    n=random.randint(1,100) #Crea el numero entre 1 y 100
    numeros.append(random.randint(1,100)) #Guardamos en la lista el numero

print(numeros) #Visualizamos lista