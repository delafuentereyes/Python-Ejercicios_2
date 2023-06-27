#Hamburguesas

canti_ham = 0

canti_ham = int(input("Digite la cantidad de hamburguesas que adquirió: "))

hamburguesa = input("Digite el tipo de hamburguesa que adquirió: ")

if hamburguesa == "sencilla":

    costo = canti_ham*20
    
elif hamburguesa == "doble":

    costo = canti_ham*25
    
else:

    costo = canti_ham*28

metodo_pago = input("Digite el método de pago: ")

if metodo_pago == "tarjeta":

    total = costo*0,5
    
else:

    total = costo

print ("El total de su compra es de: ",total) 

