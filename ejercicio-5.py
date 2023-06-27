#Contraseña

intentos = 1

while intentos <= 3:
    contra = input("Digite la contraseña: ")

    intentos += 1
    
    if contra == "1234":

        print ("Acceso permitido, bienvenido")
        intentos = 4
        break
    
    else:

        print ("Contraseña incorrecta")
        
