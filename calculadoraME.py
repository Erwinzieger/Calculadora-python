numero1=int(input("Ingrese el primer numero:"))
numero2=int(input("Ingrese el segundo numero:"))

eleccion = 0

while eleccion != 6:
    print("""
    Ingrese la operacion a realizar
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Cambiar de digito
    6) Salir          
    """)
          
    eleccion = int(input())

    if eleccion ==1:
     print (" ")
     print("Resultado:", numero1, "+", numero2, "=" , numero1+numero2)

          
        