# Elaborar un programa que me haga adivinar un numero entre 1 y 100 y consuma intentos
import random
print("\nBienvenido a 'Adivina el Numero Secreto'")
print("He selecionado un numero entre 1 y 100. ¡Adivina cual es!\n")

numero = random.randint(1, 100)
intentos = 0

while intentos < 10:

    print(f"Intento {intentos+1}/10")
    try:
        num = int(input("Ingresa tu adivinanza: "))
        if num > numero:
            print(f"El numeo es menor\n")
            intentos +=1
        elif num < numero:
            print("El numero es mayor\n")
            intentos +=1
        elif num == num:
            print(f"¡Felicidades! ¡Has adivinado el numero secreto ({numero}) en {intentos+1} intentos")
            break
    except ValueError:
        print("Debes ingresar un valor numerico!\n")
        intentos +=1
    
    if intentos == 10:
        print(f"Lo siento, el numero secreto era {numero}. ¡Mejor suerte a la proxima vez
