from dispositivos import gestor_dispositivos
from usuarios import gestor_usuarios, Rol
from viviendas import gestor_viviendas

from funciones_auxiliares import input_int, input_confirmacion, input_estado

def menu_usuario(nombre_usuario):
    (
        listar_dispositivos,
        buscar_por_nombre,
        _,
        _,

        _,
        activar_modo_fiesta,
        apagar_modo_fiesta,
        activar_modo_noche,
        apagar_modo_noche,
        configurar_hora_modo_noche,
        verificar_hora_modo_noche,
    ) = gestor_dispositivos()

    consultar_datos_personales, *resto = gestor_usuarios()

    while True:
        print(f"--- Menu Usuario Estandar de {nombre_usuario} ---")
        print("1. Consultar los datos personales")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Modificar Modo Fiesta")
        print("5. Modificar Modo Noche")
        print("6. Configurar la Hora de activacion de Modo Noche")
        print("7. Salir")

        opcion = input_int("Seleccione una opcion 1-7: ", 1, 7)
        print("-------------------------------------------")

        if opcion == 1:
            consultar_datos_personales(nombre_usuario)

        elif opcion == 2:
            listar_dispositivos()

        elif opcion == 3:
            nombre = input("Ingrese el nombre del dispositivo a buscar: ").strip()
            if buscar_por_nombre(nombre):
                print(f"El dispositivo ingresado como '{nombre}' si existe.")
            else:
                print(f"No existe ningun dispositivo llamado '{nombre}'.")

        elif opcion == 4:
            accion = input_int("Ingrese 1 para activar Modo Fiesta o 2 para apagarlo: ", 1, 2)
            if accion == 1:
                print(activar_modo_fiesta())
            else:
                print(apagar_modo_fiesta())

        elif opcion == 5:
            accion = input_int("Ingrese 1 para activar Modo Noche o 2 para apagarlo: ", 1, 2)
            if accion == 1:
                print(activar_modo_noche())
            else:
                print(apagar_modo_noche())
        
        elif opcion == 6:
            nueva_hora = int(input("Ingrese la nueva hora de activacion del modo noche (0-23):"))
            configurar_hora_modo_noche(nueva_hora)

        elif opcion == 7:
            print("Saliendo de la Cuenta")
            break

        # Verificar la hora por cada iteración y activar el modo noche si la hora coincide
        # con la configurada para que se encienda.
        if verificar_hora_modo_noche():
            activar_modo_noche()
            print("MODO NOCHE ACTIVADO AUTOMATICAMENTE!!!")

def menu_viviendas(nombre_usuario):

    agregar_vivienda, buscar_vivienda_por_nombre, eliminar_vivienda, listar_viviendas, agregar_ubicacion_a_vivienda, _ = gestor_viviendas()


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
            if agregar_vivienda(nombre, direccion):
                print("Vivienda agregada correctamente.")
            else:
                print("Ya existe una vivienda con ese nombre.")

        elif opcion == 2:
            nombre = input("Nombre de la vivienda a buscar: ").strip()
            if not nombre:
                print("El nombre a buscar no puede estar vacío.")
                continue
            vivienda = buscar_vivienda_por_nombre(nombre)
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
            
            vivienda_existente = buscar_vivienda_por_nombre(nombre)
            if not vivienda_existente:
                print(f"No se encontró ninguna vivienda llamada '{nombre}'.")
                continue

            confirmar = input(f"¿Está seguro que desea eliminar la vivienda '{nombre}'? (si/no): ").strip()
            print(eliminar_vivienda(nombre, confirmar))

        elif opcion == 4:
            resultado = listar_viviendas()
            if resultado: 
                print(resultado)

        elif opcion == 5:
            nombre_vivienda = input("Nombre de la vivienda: ").strip()
            if not nombre_vivienda:
                print("El nombre de la vivienda no puede estar vacío.")
                continue
            
            vivienda_obj = buscar_vivienda_por_nombre(nombre_vivienda)
            if not vivienda_obj:
                print("No se encontró la vivienda para agregarle una ubicación.")
                continue

            ubicacion = input("Nombre del ambiente/ubicación a agregar: ").strip()
            if not ubicacion:
                print("El nombre de la ubicación no puede estar vacío.")
                continue
            
            resultado = agregar_ubicacion_a_vivienda(nombre_vivienda, ubicacion)
            if resultado is True:
                print("Ubicación agregada correctamente.")
            elif resultado is False: 
                if ubicacion in vivienda_obj["dispositivos"]:
                    print("La ubicación ya existe en esa vivienda.")
                else:
                    print("No se pudo agregar la ubicación (posiblemente estaba vacía o ya existía).")

        elif opcion == 6: # Falta implementar esta funcionalidad
        
            continue

        elif opcion == 7:
            print("Saliendo del menú...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


def menu_admin(nombre_usuario):
    (
        listar_dispositivos,
        buscar_por_nombre,
        agregar_dispositivo,
        eliminar_dispositivo,

        consultar_automatizaciones,
        _,
        _,
        activar_modo_noche,
        _,
        _,
        verificar_hora_modo_noche,
    ) = gestor_dispositivos()

    _, _, _, listar_usuarios, modificar_rol_usuario, _ = gestor_usuarios()

    while True:
        print(f"--- Menu Administrador de {nombre_usuario} ---")
        print("1. Consultar automatizaciones activas")
        print("2. Agregar dispositivos")
        print("3. Listar dispositivos")
        print("4. Buscar dispositivo")
        print("5. Eliminar dispositivo")
        print("6. Modificar el rol de un usuario")
        print("7. Salir")

        opcion = input_int("Seleccione una opción 1-7: ", 1, 7)
        print("-------------------------------------------")

        if opcion == 1:
            print(consultar_automatizaciones())

        elif opcion == 2:
            print("\n--- AGREGAR NUEVO DISPOSITIVO ---")
            nombre_nuevo = input("Ingrese el nombre del dispositivo: ").strip()
            print("Tipos disponibles:  1: Cámara | 2: Luz | 3: Música")
            tipo_nuevo = input_int("Ingrese el tipo de dispositivo (1-3): ", 1, 3)
            input_estado()
            resultado = agregar_dispositivo(nombre_nuevo, tipo_nuevo, input_estado)
            if resultado:
                print(f"Dispositivo {nombre_nuevo} agregado")
            else:
                print(f"El dispositovo {nombre_nuevo} ya existe")
        elif opcion == 3:
            listar_dispositivos()
        
        elif opcion == 4:
            nombre = input("Ingrese el nombre del dispositivo a buscar: ").strip()
            if buscar_por_nombre(nombre):
                print(f"El dispositivo ingresado como '{nombre}' si existe.")
            else:
                print(f"No existe ningUn dispositivo llamado '{nombre}'.")
        
        elif opcion == 5:
            dispositivo = input("Ingrese el dispositivo que quiere eliminar: ").strip()
            confirmar = input_confirmacion(f"¿Esta seguro que desea eliminar el dispositivo '{dispositivo}'? (si/no): ")
            resultado = eliminar_dispositivo(dispositivo, confirmar)
            print(resultado)
        
        elif opcion == 6:
             listar_usuarios()
             usuario_a_modificar = input("\nIngrese el nombre de usuario que desea modificar: ").strip()
             if usuario_a_modificar == nombre_usuario:
                 print("No puedes modificar tu propio rol")
                 continue
             print("\nRoles disponibles: 1:Usuario, 2:Admin, 3:Dueño")
             nuevo_rol_num = input_int("Ingrese el número del nuevo rol para el usuario:", 1, 3)
             resultado = modificar_rol_usuario(usuario_a_modificar, nuevo_rol_num)
             print(resultado)
        
        elif opcion == 7:
            print("Saliendo de la cuenta...")
            break

        # Verificar la hora por cada iteración y activar el modo noche si la hora coincide
        # con la configurada para que se encienda.
        if verificar_hora_modo_noche():
            activar_modo_noche()
            print("MODO NOCHE ACTIVADO AUTOMATICAMENTE!!!")



def crear_cuenta():
    print("Crear Cuenta")

def menu():
    _, iniciar_sesion, registrar_usuario, *resto = gestor_usuarios()

    while True:
        print("Menu Principal:")
        print("1. Iniciar sesion")
        print("2. Crear cuenta")
        print("3. Salir")

        opcion = input_int("Seleccione una opción 1-3: ", 1, 3)

        if opcion == 1:
            usuario = input("Ingrese su nombre de usuario: ").strip()
            contraseña = input("Ingrese su contraseña: ").strip()
            nombre_usuario, rol = iniciar_sesion(usuario, contraseña)
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
            
            nuevoUsuario = registrar_usuario(nombre, apellido, usuario, contraseña, email)
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