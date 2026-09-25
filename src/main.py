from autenticacion import logeo
from menus.menuadmin import Menuadmin
from menus.menudocente import MenuDocente
from menus.menuestudiante import MenuEstudiante
from usuarios import RegistrarUsuario


def Main():
    # El proyecto inicia sin usuarios precargados
    usuarios = []

    print("==========================================")
    print("   SISTEMA DE GESTIÓN INSTITUCIONAL Y PQRS ")
    print("==========================================")

    while True:
        # Si la lista está vacía, se solicita crear el primer usuario del sistema
        if not usuarios:
            print(
                "\n⚠️ No hay usuarios registrados en el sistema. Debe registrar el primer usuario."
            )
            usuarios = RegistrarUsuario(usuarios)
            continue

        # Proceso normal de login cuando ya existen usuarios
        UsuarioLogueado, Estado = logeo(usuarios)

        if Estado == 1:
            # Redirección según el rol del usuario que inició sesión
            if UsuarioLogueado["Rol"] == "ADMIN":
                usuarios = Menuadmin(usuarios)
            elif UsuarioLogueado["Rol"] == "ESTUDIANTE":
                MenuEstudiante(UsuarioLogueado)
            elif UsuarioLogueado["Rol"] == "DOCENTE":
                MenuDocente()

        elif Estado == 2:
            print("El usuario no existe.")

        elif Estado == 3:
            print("Contraseña invalida. :()")

        print("\n----------------------------------")
        continuar = (
            input("¿Desea volver al menú de inicio de sesión? (S/N): ")
            .strip()
            .upper()
        )
        if continuar != "S":
            print("¡Saliendo del programa!")
            break


if __name__ == "__main__":
    Main()