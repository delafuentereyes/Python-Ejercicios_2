#Viaje en autobus

costo_autobus = 4000
total = 0
canti_alum = int(input("Digite la cantidad de alumnos que viajarán: "))

if canti_alum >= 100:

    costo = canti_alum*65

elif canti_alum >= 50 and canti_alum < 99:

    costo = canti_alum*70

elif canti_alum >= 30 and canti_alum < 49:

    costo = canti_alum*95

else:
    
    costo = canti_alum*100

total = costo
total2 = costo+costo_autobus

print ("El total que deberá cobrarle a los alumnos es de:",costo,
"\nMientras que el total de servcio de autobus es de:",total2)