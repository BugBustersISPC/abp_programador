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
from funciones_auxiliares import input_int, input_estado, input_confirmacion

lista_dispositivos = [
    {"nombre": 'Luces', "tipo": 2, "estado": True},
    {"nombre": 'Camara seguridad', "tipo": 1, "estado": False},
    {"nombre": 'Equipo musica', "tipo": 3, "estado": True},
    {"nombre": 'Luces 2', "tipo": 2, "estado": True}
]

if __name__ == '__main__':
    while True:
        print("--- MENU PRINCIPAL ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Modificar Modo Fiesta")
        print("6. Modificar Modo Noche")
        print("7. Salir")

        opcion = input_int("Seleccione una de las opciones (1-7): ", 1, 7)
        print("-------------------------------------------")

        if opcion == 1:
            nombre = input("Nombre del nuevo dispositivo: ").strip()
            tipo = input_int("Tipo (1: camara, 2: luces, 3: musica): ", 1, 3)
            estado = input_estado()
            if agregar_dispositivo(lista_dispositivos, nombre, tipo, estado):
                print("El dispositivo ingresado se registro con exito.")
            else:
                print("Ya existe un dispositivo con ese nombre. Vuelva a intentarlo con otro")

        elif opcion == 2:
            listar_dispositivos(lista_dispositivos)

        elif opcion == 3:
            nombre = input("Ingrese el nombre del dispositivo a buscar: ").strip()
            if buscar_por_nombre(nombre, lista_dispositivos):
                print(f"El dispositivo ingresado como '{nombre}' si existe.")
            else:
                print(f"No existe ningún dispositivo llamado '{nombre}'.")

        elif opcion == 4:
            dispositivo = input("Ingrese el dispositivo que quiere eliminar: ").strip()
            confirmar = input_confirmacion(f"¿Esta seguro que desea eliminar el dispositivo2 '{dispositivo}'? (si/no): ")
            resultado = eliminar_dispositivo(dispositivo, confirmar, lista_dispositivos)
            print(resultado)

        elif opcion == 5:
            accion = input_int("Ingrese 1 para activar Modo Fiesta o 2 para apagarlo: ", 1, 2)
            if accion == 1:
                print(activar_modo_fiesta(lista_dispositivos))
            else:
                print(apagar_modo_fiesta(lista_dispositivos))

        elif opcion == 6:
            accion = input_int("Ingrese 1 para activar Modo Noche o 2 para apagarlo: ", 1, 2)
            if accion == 1:
                print(activar_modo_noche(lista_dispositivos))
            else:
                print(apagar_modo_noche(lista_dispositivos))

        elif opcion == 7:
            print("Saliendo del sistema...")
            break