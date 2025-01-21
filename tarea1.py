print("Hola mundo")

nombre= input("ingrese su nombre: ")
print(f"Hola, {nombre}")

edad= float(input("ingrese su edad: "))
if edad >=18:
    print("usted es mayor de edad")
else:
    print("usted es menor de edad")

número= int(float(input("ingrese el número: ")))
if número % 2 == 0:
    print(f"el {número} es par")
else:
    print(f"el {número} es impar")

n= int(float(input("ingrese su número entero: ")))
suma= n*(n+1)/2
print(f"la suma de los {n} primeros números es {suma}")