lista_invitados= ["luis","wilter","mia","gisela"]
edad= float(input("ingrese su edad: "))
nombre= input("ingrese su nombre: ")
if edad >=18 and nombre in lista_invitados:
    print(f"pase usted {nombre}")
else:
    print(f"lárguese {nombre}")