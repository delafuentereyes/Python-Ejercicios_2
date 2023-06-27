#Introducir números

canti_digi = int(input("Digite la cantidad de datos que va a ingresar: "))

if canti_digi > 0:

    negativos = 0
    positivos = 0

    for i in range (canti_digi):

        dato = int(input("Ingrese un numero natural: "))

        if dato < 0: 
            
            negativos += 1
        
        else:

            positivos += 1
    
    print ("La cantidad de números negativos es de:",negativos,
    "\nMientras que la cantidad de los positivos es de:",positivos)

else:
    print ("El número ingresado es incorrecto. Intente de nuevo")



