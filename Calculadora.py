numero1=int(input("Ingresa un numero:"))   #int es para que pueda ingresar un numero entero
numero2=int(input("Ingresa otro numero:"))  #imput es para que el usuario pueda escribir


elección = 0  # creamos una variable con igual cero para seleccionar lo que queremos hacer con los numeros que introducimos

while elección != 6: #while sirve para hacer que sea en bucle, osea que nunca se acabe 
    print("""      
    indique la operacion a relizar:    
     1) Suma
     2) Resta
     3) Multiplicacion
     4) Division
     5) Cambio de valores
     6) Salir
     """)
 # las 3 """ en print es para realizar un texto multilinea
          
    elección = int(input())     #Lo hacemos todo adentro de while para que toda la funcion este en el mismo bloque
    
    if elección ==1:
        print(" ")
        print("Resultado: ", numero1, "+" , numero2, "=", numero1+numero2)
        
    if elección ==2:
        print(" ")
        print("Resultado: ", numero1, "-" , numero2, "=", numero1-numero2)

    if elección ==3:
        print(" ")
        print("Resultado: ", numero1, "*" , numero2, "=", numero1*numero2)

    if elección ==4:
        print(" ")
        print("Resultado: ", numero1, "/" , numero2, "=", numero1/numero2)

    if elección ==5:
        numero1=int(input("Ingresa un numero:"))
        numero2=int(input("Ingresa otro numero:"))

    if elección ==6:
        print("Gracias por usar esta calculadora de mierda! Un saludo grande! ")
