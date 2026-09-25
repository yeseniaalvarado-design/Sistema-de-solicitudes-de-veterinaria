from usuarios import RegistrarUsuario


def logeo(usuarios):
    # Diferentes Escenarios al momento de ingresar a un sistema:
    # 1. Login Exitoso (Estado 1)
    # 2. Usuario No existe / Opción de registrarse (Estado 2)
    # 3. Contraseña Inválida (Estado 3)

    nombre = input("Ingrese usuario: ").strip()
    clave = input("Ingrese clave: ").strip()
    usuario_encontrado = {}
    existe_usuario = False

    for usuario in usuarios:
        if usuario["Nombre"] == nombre:
            existe_usuario = True
            usuario_encontrado = usuario
            break

    if existe_usuario == False:
        print("El usuario no existe.")
        opcion = input("¿Desea registrarse? (si/no): ").strip().lower()
        if opcion == "si":
            RegistrarUsuario(usuarios)
        return usuario_encontrado, 2

    elif usuario_encontrado["Clave"] != clave:
        print("Contraseña invalada.")
        return usuario_encontrado, 3

    else:
        print(f"Bienvenido al sistema {nombre}.")
        return usuario_encontrado, 1