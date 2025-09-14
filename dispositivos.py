from enum import Enum
from datetime import datetime

hora_activacion_modo_noche = 23

class TipoDispositivo(Enum):
    CAMARA = 1
    LUZ = 2
    SONIDO = 3

def gestor_dispositivos():

    dispositivos = [
        {'nombre': 'Camara seguridad', 'tipo': TipoDispositivo.CAMARA, 'estado': False, 'ambiente': 'Entrada'},
        {'nombre': 'Camara trasera', 'tipo': TipoDispositivo.CAMARA, 'estado': True, 'ambiente': 'Patio'},
        {'nombre': 'Luces', 'tipo': TipoDispositivo.LUZ, 'estado': True, 'ambiente': 'Comedor'},
        {'nombre': 'Luz', 'tipo': TipoDispositivo.LUZ, 'estado': False, 'ambiente': 'Sala'},
        {'nombre': 'Luz RGB', 'tipo': TipoDispositivo.LUZ, 'estado': True, 'ambiente': 'Dormitorio'},
        {'nombre': 'Parlantes TV', 'tipo': TipoDispositivo.SONIDO, 'estado': True, 'ambiente': 'Living'},
        {'nombre': 'Equipo musica', 'tipo': TipoDispositivo.SONIDO, 'estado': True, 'ambiente': 'Habitación'},
    ]

    # MARK: Gestión de Dispositivos

    def buscar_por_nombre(nombre):
        for i in dispositivos:
            if nombre == i['nombre']:
                return True
        
        return False

    def agregar_dispositivo(nombre, tipo, estado):
        if not buscar_por_nombre(nombre):
            dispositivos.append({
                'nombre': nombre,
                'tipo': tipo,
                'estado': estado,
            })

            return True

        return False

    def eliminar_dispositivo(nombre, confirmar):
        for dis in dispositivos:
            if dis['nombre'].lower() == nombre.lower():
                if confirmar.lower() == 'si':
                    dispositivos.remove(dis)
                    return f'El dispositivo "{nombre}" fue eliminado.'
                elif confirmar.lower() == 'no':
                    return 'Operación cancelada...'
                else:
                    return 'Error: Solamente escriba "si" o "no".'
        return f'No se encontro ningun dispositivo llamado "{nombre}".'

    def listar_dispositivos():
        if not dispositivos:
            return 'No hay dispositivos registrados.'
        for dis in dispositivos:
            print(f'- {dis['nombre']} (Tipo: {dis['tipo']}) - {'Estado: On' if dis['estado'] else 'Estado: Off'}')

    # MARK: Automatizaciones

    def consultar_automatizaciones():
        modo_fiesta = True
        for dispositivo in dispositivos:
            if dispositivo["tipo"] in [2, 3]:
                if dispositivo["estado"] == False:
                    modo_fiesta = False
                    break

        modo_noche = True
        for dispositivo in dispositivos:
            if dispositivo["tipo"] == 1 and dispositivo["estado"] == False:
                modo_noche = False
                break

        return modo_fiesta, modo_noche

    def activar_modo_fiesta():
        for dispositivo in dispositivos:
            if dispositivo["tipo"].value in [2, 3] and dispositivo["estado"] == False :  # 2: luces, 3: música
                dispositivo["estado"] = True
                
        return "Modo Fiesta activado: luces y equipos de música encendidos."

    def apagar_modo_fiesta():
        for dispositivo in dispositivos:
            if dispositivo["tipo"].value in [2, 3] and dispositivo["estado"] == True:  # 2: luces, 3: música
                dispositivo["estado"] = False

        return "Modo Fiesta apagado: luces y equipos de música apagados."

    def activar_modo_noche():
        for dispositivo in dispositivos:
            if dispositivo["tipo"].value in [2, 3] and dispositivo["estado"] == True :  # 2: luces, 3: música
                dispositivo["estado"] = False
            if dispositivo["tipo"].value == 1 and dispositivo["estado"] == False:
                dispositivo["estado"] = True
        return "Modo Noche activado: luces y equipos de música apagados, cámaras encendidas."

    def apagar_modo_noche():
        for dispositivo in dispositivos:
            if dispositivo["tipo"].value == 1 and dispositivo["estado"] == True:
                dispositivo["estado"] = False
        return "Modo Noche desactivado: cámaras apagadas."             

    def configurar_hora_modo_noche(nueva_hora):
        if nueva_hora > 23 or nueva_hora < 0:
            return False
        
        global hora_activacion_modo_noche
        hora_activacion_modo_noche = nueva_hora

    def verificar_hora_modo_noche():
        time = datetime.now()
        modo_fiesta, modo_noche = consultar_automatizaciones()

        # Para que el modo noche se active automaticamente, no debe estar activo el modo
        # fiesta ni el modo noche y tiene que ser la hora a la que esta configurada para
        # que se active
        if modo_fiesta or modo_noche or time.hour != hora_activacion_modo_noche:
            return False
        else:
            return True

    return (
        # Dispositivos (0-3)
        listar_dispositivos,
        buscar_por_nombre,
        agregar_dispositivo,
        eliminar_dispositivo,

        # Automatizaciones (4-10)
        consultar_automatizaciones,
        activar_modo_fiesta,
        apagar_modo_fiesta,
        activar_modo_noche,
        apagar_modo_noche,
        configurar_hora_modo_noche,
        verificar_hora_modo_noche,
    )