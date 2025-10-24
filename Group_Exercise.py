# Juego  para  adivinar  un  numero  generado  de  manera random.

"""
Dato de color, al dejar secret_num fuera del bucle, una vez comienza nuevamente el programa, el número aleatorio 
es el mismo ya que no se vuelve a ejecutar. (Me sirvió para ir probando ya que sabía cual erá el número secreto xD)

"""
import random # Se importa de la librería de python

while True:
    secret_num = random.randint(1,15) # módulo random, se llama text random.randint(se coloca rango númerico)
    print(f"\n{'-'*40} Juego Adivina Un Número {'-'*40}")
    print("\nDebes escoger un número del 1 al 15")
    round = 1 # variable contador
    round_total = 5 # número máximo de rondas
    reiniciar = "si"
    salir = "no"

    while round < round_total:

        while True:

            num = (input(f"\nPor favor ingresa un número, intento ({(round)}): "))
        
            if num.isdigit():
                num = int(num)
                break
            else:
                print("\n!!Dato Inválido!!")
            
        if num == secret_num:
            print(f"\nAcertaste el número secreto es: ({secret_num}), en el intento: ({(round)})")
            print ("\nGracias por participar")
            break
        
        elif num < secret_num:
            print("\nEl número ingresado es !Menor! al número secreto, intenta de nuevo")
        
        else:
            print("\nEl número ingresado es !Mayor! al número secreto")
            
        round += 1
    
    else:
        print(f"\nNo posees más intentos, el número secreto es **{secret_num}**")
    
    while True:
        question = input(f"\n¿Deseas volver a jugar (si) o (no)?: ").lower()
            
        if question == reiniciar:
            break
        elif question == salir:
            print("\nGracias por participar, hasta la próxima")
            exit()
        else:
            print("Opción no reconocida, por favor ingresa 'si' o 'no'.")