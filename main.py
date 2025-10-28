suma = 0

print("El programa se detendra cuando ingrese un 0 \n")

while True:
    n = input("Ingrese un numero: ")

    if n.isdigit():
        n = int(n)
        if not n == 0:
            suma += (n**2) 
        else:
            break
    else:
        print(f"\nTe dije que ingreses un numero.")
        
print(f"\nLa suma del cuadrado de los numeros ingresados es: {suma}")