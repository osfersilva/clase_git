

while True: 
    print(f"\n\n{'-'*40} La trifecta {'-'*40}")
    print("\n        Bienvenido debe ingresar un número. ¡¡Ingresando 0 cerrará el programa!!\n")
    num = (input(f"\nPor favor ingresa un número entero: "))    
    if num.isdigit():
        num = int(num)

        if num == 0:
            print("\nSe ingresó 0. Fin del programa.")
            break

    else:
        print("\n!!Dato Inválido, recuerde ingresar un número entero!!")
        continue

    while True:
        word = input("\nPor favor ingrese una palabra o frase: ")
        word_clean = word.replace(" " , "")
        num_word = len(word_clean)
        num_factorial = 1
        
        if word_clean.isalpha():
            print(f"\nTu palabra o frase ({word}) tiene *{num_word}* letras")

        else:
            print("\n¡¡Dato Invalido, intente de nuevo. Recuerde ingresar una frase o palabra")
            continue

        for i in range(1 , num_word + 1) :
            num_factorial *= i

        if num_factorial % 2 == 0:
            paridad = "Par"

        else:
            paridad = "Impar"
        
        print(f"\nEl factorial de *{num_word}* es *{num_factorial}*")

        print(f"\nLa cifra *{num_factorial}* es ({paridad})")
        break