#Consultorio

num_cita = int(input("Digite cual es su numero de sesion de cita: "))

if num_cita <= 3:

    costo = 200

elif num_cita > 3 and num_cita <= 5:

    costo = 150

elif num_cita > 5 and num_cita <= 8: 

    costo = 100

else: 

    costo = 50

tratamiento = int(input("Digite lo que ha pagado por el tratamiento: "))

total = costo
total_tratamiento = tratamiento

print ("El total de la sesion es ",total,
"\nMientras que el monto del tratamiento es de",total_tratamiento)