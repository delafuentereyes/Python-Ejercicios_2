#Sala de juegos

edad = int(input("Por favor digite su edad: "))
print ("\n")

if edad < 4:

    print ("Puede entrar de forma gratuita!")

elif edad >= 4 and edad < 18:

    print ("Su precio de entrada es de $5")

else:

    print ("Su precio de entrada es de $10")

print ("Bienvenido!!")