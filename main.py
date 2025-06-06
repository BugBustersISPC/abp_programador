from dispositivos import (
    agregar_dispositivo,
    listar_dispositivos,
    buscar_por_nombre,
    eliminar_dispositivo
)
from automatizaciones import (
    consultar_automatizaciones,
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

from roles import Rol

from viviendas import (
    agregar_vivienda,
    buscar_vivienda_por_nombre,
    eliminar_vivienda,
    listar_viviendas,
    agregar_ubicacion_a_vivienda
)

cuentas = {
    "JuanPerez": {
        "nombre": "Juan",
        "apellido": "Perez",
        "contraseña": "1234",
        "rol": Rol.ADMIN.value,
        "email": "juan.perez@email.com"
    },
    "AnaLopez": {
        "nombre": "Ana",
        "apellido": "Lopez",
        "contraseña": "5678",
        "rol": Rol.USUARIO.value,
        "email": "ana.lopez@email.com"
    },
    "CarlosGomez": {
        "nombre": "Carlos",
        "apellido": "Gomez",
        "contraseña": "abcd",
        "rol": Rol.USUARIO.value,
        "email": "carlos.gomez@email.com"
    },
    "MariaGarcia": {
        "nombre": "Maria",
        "apellido": "Garcia",
        "contraseña": "abcd",
        "rol": Rol.DUENO.value,
        "email": "maria.garcia@email.com"
    }
}

lista_dispositivos = [
    {"nombre": 'Luces', "tipo": 2, "estado": True, "ambiente": "Comedor"},
    {"nombre": 'Camara seguridad', "tipo": 1, "estado": False, "ambiente": "Entrada"},
    {"nombre": 'Camara trasera', "tipo": 1, "estado": True, "ambiente": "Patio"},
    {"nombre": 'Luz', "tipo": 2, "estado": False, "ambiente": "Sala"},
    {"nombre": 'Luz RGB', "tipo": 2, "estado": True, "ambiente": "Dormitorio"},
    {"nombre": 'Parlantes TV', "tipo": 3, "estado": True, "ambiente": "Living"},
    {"nombre": 'Alarma', "tipo": 1, "estado": False, "ambiente": "Comedor"},
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

def menu_viviendas(nombre_usuario):
    viviendas = [
        {
            "nombre": "Casa Central",
            "direccion": "Av. Libertador 1234",
            "ambientes": ["Comedor", "Baño"]
        },
        {
            "nombre": "Casa de Verano",
            "direccion": "Calle del Sol 789",
            "ambientes": ["Dormitorio", "Cocina"]
        },
        {
            "nombre": "Departamento Centro",
            "direccion": "Mitre 456",
            "ambientes": []
        }
    ]

    while True:
        print(f"--- Menu Usuario Dueño de {nombre_usuario} ---")
        print("1. Agregar vivienda")
        print("2. Buscar vivienda por nombre")
        print("3. Eliminar vivienda")
        print("4. Listar viviendas")
        print("5. Agregar ubicación a una vivienda")
        print("6. Agregar dispositivo a un ambiente") # Falta agregar esta funcionalidad
        print("7. Salir")

        opcion = input_int("Seleccione una opción: " , 1, 7)
        

        if opcion == 1:
            nombre = input("Nombre de la vivienda: ").strip()
            direccion = input("Dirección de la vivienda: ").strip()
            if not nombre or not direccion: 
                print("El nombre y la dirección no pueden estar vacíos.")
                continue
            if agregar_vivienda(viviendas, nombre, direccion):
                print("Vivienda agregada correctamente.")
            else:
                print("Ya existe una vivienda con ese nombre.")

        elif opcion == 2:
            nombre = input("Nombre de la vivienda a buscar: ").strip()
            if not nombre:
                print("El nombre a buscar no puede estar vacío.")
                continue
            vivienda = buscar_vivienda_por_nombre(nombre, viviendas)
            if vivienda:
                print(f"\n--- DETALLES DE LA VIVIENDA ---")
                print(f"Nombre: {vivienda['nombre']}")
                print(f"Dirección: {vivienda['direccion']}")
                print(f"Ubicaciones ({len(vivienda['dispositivos'])}): {', '.join(vivienda['dispositivos']) if vivienda['dispositivos'] else 'Ninguna'}")
            else:
                print("No se encontró la vivienda.")

        elif opcion == 3:
            nombre = input("Nombre de la vivienda a eliminar: ").strip()
            if not nombre:
                print("El nombre a eliminar no puede estar vacío.")
                continue
            
            vivienda_existente = buscar_vivienda_por_nombre(nombre, viviendas)
            if not vivienda_existente:
                print(f"No se encontró ninguna vivienda llamada '{nombre}'.")
                continue

            confirmar = input(f"¿Está seguro que desea eliminar la vivienda '{nombre}'? (si/no): ").strip()
            print(eliminar_vivienda(nombre, confirmar, viviendas))

        elif opcion == 4:
            resultado = listar_viviendas(viviendas)
            if resultado: 
                print(resultado)

        elif opcion == 5:
            nombre_vivienda = input("Nombre de la vivienda: ").strip()
            if not nombre_vivienda:
                print("El nombre de la vivienda no puede estar vacío.")
                continue
            
            vivienda_obj = buscar_vivienda_por_nombre(nombre_vivienda, viviendas)
            if not vivienda_obj:
                print("No se encontró la vivienda para agregarle una ubicación.")
                continue

            ubicacion = input("Nombre del ambiente/ubicación a agregar: ").strip()
            if not ubicacion:
                print("El nombre de la ubicación no puede estar vacío.")
                continue
            
            resultado = agregar_ubicacion_a_vivienda(nombre_vivienda, ubicacion, viviendas)
            if resultado is True:
                print("Ubicación agregada correctamente.")
            elif resultado is False: 
                if ubicacion in vivienda_obj["dispositivos"]:
                    print("La ubicación ya existe en esa vivienda.")
                else:
                    print("No se pudo agregar la ubicación (posiblemente estaba vacía o ya existía).")

        elif opcion == 6: # Falta implementar esta funcionalidad
        
            break

        elif opcion == 7:
            print("Saliendo del menú...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


def menu_admin(nombre_usuario):
    while True:
        print(f"--- Menu Administrador de {nombre_usuario} ---")
        print("1. Consultar automatizaciones activas")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Modificar el rol de un usuario")
        print("6. Salir")

        opcion = input_int("Seleccione una opción 1-6: ", 1, 6)
        print("-------------------------------------------")

        if opcion == 1:
            print(consultar_automatizaciones(lista_dispositivos))
        
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

        opcion = input_int("Seleccione una opción 1-3: ", 1, 3)

        if opcion == 1:
            usuario = input("Ingrese su nombre de usuario: ").strip()
            contraseña = input("Ingrese su contraseña: ").strip()
            nombre_usuario, rol = iniciar_sesion(cuentas, usuario, contraseña)
            if nombre_usuario and rol:
                if rol == Rol.ADMIN:
                    menu_admin(nombre_usuario)
                elif rol == Rol.USUARIO:
                    menu_usuario(nombre_usuario)
                elif rol == Rol.DUENO:
                    menu_viviendas(nombre_usuario)
            
        elif opcion == 2:
            nombre = input("Ingrese su nombre: ").strip()
            apellido = input("Ingrese su apellido: ").strip()
            usuario = input("ingrese su Usuario: ").strip()
            email = input("Ingrese su correo email: ").strip()
            contraseña = input("Ingrese una contraseña: ").strip()
            
            nuevoUsuario = registrar_usuario(cuentas,nombre,apellido,usuario,contraseña,email)
            if nuevoUsuario:
                print("Cuenta creada exitosamente. Iniciando sesión automáticamente...")
                menu_usuario(usuario)
            else:
                print("Ya existe un usuario con ese email. Intente con otro.")
        elif opcion == 3:
            print("Saliendo del sistema...")
            break
if __name__ == "__main__":    
    menu()