

def gestor_viviendas():
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

    def agregar_vivienda(nombre: str, direccion: str):
        if not buscar_vivienda_por_nombre(nombre):
            viviendas.append({
                "nombre": nombre,
                "direccion": direccion,
                "ambientes": []  
            })
            return True
        return False


    def buscar_vivienda_por_nombre(nombre: str):
        for vivienda in viviendas:
            if vivienda["nombre"].lower() == nombre.lower():
                return vivienda
        return None


    def eliminar_vivienda(nombre: str, confirmar: str):
        vivienda_a_eliminar = buscar_vivienda_por_nombre(nombre)
        if vivienda_a_eliminar:
            if confirmar.lower() == "si":
                viviendas.remove(vivienda_a_eliminar)
                return f"La vivienda '{nombre}' fue eliminada."
            elif confirmar.lower() == "no":
                return "Operación cancelada..."
            else:
                return "Error: Solamente escriba 'si' o 'no'."
        return f"No se encontró ninguna vivienda llamada '{nombre}'."


    def listar_viviendas():
        if len(viviendas) == 0:
            return "No hay viviendas registradas."
        
        print("\n--- LISTA DE VIVIENDAS ---")
        for vivienda in viviendas:
            print(f"- {vivienda["nombre"]} (Dirección: {vivienda["direccion"]}) - Ambientes: {len(vivienda["ambientes"])}")


    def agregar_ubicacion_a_vivienda(nombre_vivienda: str, ubicacion: str):
        vivienda = buscar_vivienda_por_nombre(nombre_vivienda)
        if vivienda:
            if ubicacion.strip() and ubicacion not in vivienda["ambientes"]:
                vivienda["ambientes"].append(ubicacion)
                return True
            elif ubicacion in vivienda["ambientes"]:
                return False
            else:
                return False
        return None


    def menu_viviendas():
        while True:
            print("\n--- MENÚ DE VIVIENDAS ---")
            print("1. Agregar vivienda")
            print("2. Buscar vivienda por nombre")
            print("3. Eliminar vivienda")
            print("4. Listar viviendas")
            print("5. Agregar ubicación a una vivienda")
            print("6. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                nombre = input("Nombre de la vivienda: ").strip()
                direccion = input("Dirección de la vivienda: ").strip()
                if not nombre or not direccion: 
                    print("El nombre y la dirección no pueden estar vacíos.")
                    continue
                if agregar_vivienda(viviendas, nombre, direccion):
                    print("Vivienda agregada correctamente.")
                else:
                    print("Ya existe una vivienda con ese nombre.")

            elif opcion == "2":
                nombre = input("Nombre de la vivienda a buscar: ").strip()
                if not nombre:
                    print("El nombre a buscar no puede estar vacío.")
                    continue
                vivienda = buscar_vivienda_por_nombre(nombre, viviendas)
                if vivienda:
                    print(f"\n--- DETALLES DE LA VIVIENDA ---")
                    print(f"Nombre: {vivienda["nombre"]}")
                    print(f"Dirección: {vivienda["direccion"]}")
                    print(f"Ubicaciones ({len(vivienda["dispositivos"])}): {", ".join(vivienda["dispositivos"]) if vivienda["dispositivos"] else "Ninguna"}")
                else:
                    print("No se encontró la vivienda.")

            elif opcion == "3":
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

            elif opcion == "4":
                resultado = listar_viviendas(viviendas)
                if resultado: 
                    print(resultado)

            elif opcion == "5":
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

            elif opcion == "6":
                print("Saliendo del menú...")
                break

            else:
                print("Opción inválida. Intente de nuevo.")

    return agregar_vivienda, buscar_vivienda_por_nombre, eliminar_vivienda, listar_viviendas, agregar_ubicacion_a_vivienda, menu_viviendas