from dispositivos import (
    agregar_dispositivo,
    listar_dispositivos,
    buscar_por_nombre,
    eliminar_dispositivo
)
from automatizaciones import (
    activar_modo_fiesta,
    apagar_modo_fiesta,
    activar_modo_noche,
    apagar_modo_noche
)
from funciones_auxiliares import input_int, input_confirmacion

from usuarios import (
    consultar_datos_personales,
    iniciar_sesion,
    registrar_usuario
)
1
from roles import Rol

cuentas = {
    "juan.perez@email.com": {
        "nombre": "Juan",
        "apellido": "Perez",
        "contraseña": "1234",
        "rol": Rol.ADMIN.value
    },
    "ana.lopez@email.com": {
        "nombre": "Ana",
        "apellido": "Lopez",
        "contraseña": "5678",
        "rol": Rol.USUARIO.value
    },
    "carlos.gomez@email.com": {
        "nombre": "Carlos",
        "apellido": "Gomez",
        "contraseña": "abcd",
        "rol": Rol.USUARIO.value
    }
}

lista_dispositivos = [
    {"nombre": 'Luces', "tipo": 2, "estado": True},
    {"nombre": 'Camara seguridad', "tipo": 1, "estado": False},
    {"nombre": 'Equipo musica', "tipo": 3, "estado": True},
    {"nombre": 'Luces 2', "tipo": 2, "estado": True}
]

def menu_usuario(nombre_usuario):
    while True:
        print(f"--- Menu Usuario Estandar de {nombre_usuario} ---")
        print("1. Consultar los datos personales")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Modificar Modo Fiesta")
        print("5. Modificar Modo Noche")
        print("6. Salir")

        opcion = input_int("Seleccione una opcion 1-6: ", 1, 6)
        print("-------------------------------------------")

        if opcion == 1:
            consultar_datos_personales(nombre_usuario, cuentas)

        elif opcion == 2:
            listar_dispositivos(lista_dispositivos)

        elif opcion == 3:
            nombre = input("Ingrese el nombre del dispositivo a buscar: ").strip()
            if buscar_por_nombre(nombre, lista_dispositivos):
                print(f"El dispositivo ingresado como '{nombre}' si existe.")
            else:
                print(f"No existe ningun dispositivo llamado '{nombre}'.")

        elif opcion == 4:
            accion = input_int("Ingrese 1 para activar Modo Fiesta o 2 para apagarlo: ", 1, 2)
            if accion == 1:
                print(activar_modo_fiesta(lista_dispositivos))
            else:
                print(apagar_modo_fiesta(lista_dispositivos))

        elif opcion == 5:
            accion = input_int("Ingrese 1 para activar Modo Noche o 2 para apagarlo: ", 1, 2)
            if accion == 1:
                print(activar_modo_noche(lista_dispositivos))
            else:
                print(apagar_modo_noche(lista_dispositivos))
        
        elif opcion == 6:
            print("Saliendo de la Cuenta")
            break

def menu_admin(nombre_usuario):
    while True:
        print(f"--- Menu Administrador de {nombre_usuario} ---")
        print("1. Consultar automatizaciones activas")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Modificar el rol de un usuario")
        print("6. Salir")

        opcion = input_int("Seleccione una opcio 1-6: ", 1, 6)
        print("-------------------------------------------")

        if opcion == 1:
            print("Modo Noche y Modo Fiesta habilitar estados")
        
        elif opcion == 2:
            listar_dispositivos(lista_dispositivos)
        
        elif opcion == 3:
            nombre = input("Ingrese el nombre del dispositivo a buscar: ").strip()
            if buscar_por_nombre(nombre, lista_dispositivos):
                print(f"El dispositivo ingresado como '{nombre}' si existe.")
            else:
                print(f"No existe ningUn dispositivo llamado '{nombre}'.")
        
        elif opcion == 4:
            dispositivo = input("Ingrese el dispositivo que quiere eliminar: ").strip()
            confirmar = input_confirmacion(f"¿Esta seguro que desea eliminar el dispositivo '{dispositivo}'? (si/no): ")
            resultado = eliminar_dispositivo(dispositivo, confirmar, lista_dispositivos)
            print(resultado)
        
        elif opcion == 5:
            print("Modificar rol de usuario")
        
        elif opcion == 6:
            print("Saliendo de la cuenta...")
            break


def crear_cuenta():
    print("Crear Cuenta")

def menu():
    while True:
        print("Menu Principal:")
        print("1. Iniciar sesion")
        print("2. Crear cuenta")
        print("3. Salir")

        opcion = input_int("Seleccione una opcion 1-3: ", 1, 3)

        if opcion == 1:
            usuario = input("Ingrese su nombre de usuario: ").strip()
            contraseña = input("Ingrese su contraseña: ").strip()
            nombre_usuario, rol = iniciar_sesion(cuentas, usuario, contraseña)
            if nombre_usuario and rol:
                if rol == Rol.ADMIN:
                    menu_admin(nombre_usuario)
                elif rol == Rol.USUARIO:
                    menu_usuario(nombre_usuario)
            
        elif opcion == 2:
            nombre = input("Ingrese su nombre: ").strip()
            apellido = input("Ingrese su apellido: ").strip()
            email = input("ingrese su emial: ").strip()
            contraseña = input("Ingrese una contraseña: ").strip()
            
            nuevoUsuario = registrar_usuario(cuentas,nombre,apellido,email,contraseña)
            if nuevoUsuario:
                print("Cuenta creada exitosamente. Iniciando sesión automáticamente...")
                menu_usuario(email)
            else:
                print("Ya existe un usuario con ese email. Intente con otro.")
        elif opcion == 3:
            print("Saliendo del sistema...")
            break
if __name__ == "__main__":    
    menu()