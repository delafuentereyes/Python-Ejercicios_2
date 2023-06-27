#Trabajo y sueldo

sueldo = 0
sueldo2 = 0
empleados = int(input("Digite la cantidad de empleados que trabajan en su empresa: "))


for i in range (empleados):
    
    dato = int(input("Digite cuanto gana el empleado: "))

    if dato > 1500:

        sueldo += 1
    
    else:

        sueldo2 += 1
    
print ("La cantidad de empleados que cobran más de 1500 es:",sueldo,
    "\nMientras que los que cobran menos de 1500 es:",sueldo2)

total= empleados*dato

print ("El total que paga su empresa por estos sueldos es de: ",total)




