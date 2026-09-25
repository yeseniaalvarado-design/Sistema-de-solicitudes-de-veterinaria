# Validacion de numeros Enteros, garantizando que si ingresan texto no se genere error.
def ValidarEntero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Debe ingresar un numero entero, no aceptamos Caracteres!!!")


# Validacion de numeros Flotantes (decimales), garantizando que si ingresan texto no se genere error.
def ValidarFlotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print(
                "Debe ingresar un numero decimal o entero, no aceptamos Caracteres!!!"
            )


# Validacion de texto no vacio, garantizando que el usuario no presione Enter sin escribir nada.
def ValidarTexto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("El campo no puede estar vacio. Por favor ingrese el texto!")


# Validacion de un numero Entero dentro de un rango especifico (Util para los Menus)
def ValidarEnteroRango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(
                    f"Opcion fuera de rango. Debe ingresar un numero entre {minimo} y {maximo}!"
                )
        except ValueError:
            print("Debe ingresar un numero entero, no aceptamos Caracteres!!!")


# Validacion de texto restringido a opciones especificas (Util para Roles o Tipos de PQRS)
def ValidarOpcionTexto(mensaje, opciones_validas):
    while True:
        texto = input(mensaje).strip().upper()
        if texto in [opc.upper() for opc in opciones_validas]:
            return texto
        else:
            print(
                f"Opcion no valida. Las opciones permitidas son: {', '.join(opciones_validas)}"
            )