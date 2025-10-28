# Se importa math (de libreria pyton) para poder usar el módulo y sacar el factorial

#Es posible obtener el factorial con otros métodos pero son más avanzados y además más difícil de implementar para este ejercicio.

import math

print(f"\n{'-'*40} La trifecta {'-'*40}")

while True: 

    print("\nBienvenido debe ingresar un número. ¡¡Si ingresa 0 se cerrará el programa!!\n")
    num = (input(f"Por favor ingresa un número entero: "))    
    if num.isdigit():
        num = int(num)

        if num == 0:
            print("\nSe ingresó 0. Fin del programa.")
            break

    else:
        print("\n!!Dato Inválido, recuerde ingresar un número entero!!\n\n")
        continue

    while True:
        word = input("\nPor favor ingrese una palabra o frase: ")
        word_clean = word.replace(" " , "")
        num_word = len(word_clean)
        num_factorial = math.factorial(num_word)

        if word_clean.isalpha():
            print(f"\nTu palabra o frase ({word}) tiene *{num_word}* letras")

        else:
            print("\n¡¡Dato Invalido, intente de nuevo. Recuerde ingresar una frase o palabra")
            continue

        if num_factorial % 2 == 0:
            par = "Par"

        else:
            par = "Impar"

        print(f"\nEl factorial de *{num_word}* es *{num_factorial}*")

        print(f"\nLa cifra *{num_factorial}* es ({par})")

        print(f"\n{'-'*40} La trifecta {'-'*40}")
        break