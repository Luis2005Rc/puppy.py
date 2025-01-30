def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo =="hombre"):
        adjetivo = "titán"
    else:
        adjetivo = "amor"
    print(f"hola {nombre}, mi {adjetivo}, ¿cómo estás?")

saludar("camilo","hombre")