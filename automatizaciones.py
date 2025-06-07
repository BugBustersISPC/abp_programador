from datetime import datetime

hora_activacion_modo_noche = 23

def consultar_automatizaciones(dispositivos):
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

def activar_modo_fiesta(dispositivos):
    for dispositivo in dispositivos:
        if dispositivo["tipo"] in [2, 3] and dispositivo["estado"] == False :  # 2: luces, 3: música
            dispositivo["estado"] = True
            
    return "Modo Fiesta activado: luces y equipos de música encendidos."

def apagar_modo_fiesta(dispositivos):
    for dispositivo in dispositivos:
        if dispositivo["tipo"] in [2, 3] and dispositivo["estado"] == True:  # 2: luces, 3: música
            dispositivo["estado"] = False

    return "Modo Fiesta apagado: luces y equipos de música apagados."

def activar_modo_noche(dispositivos):
    for dispositivo in dispositivos:
        if dispositivo["tipo"] in [2, 3] and dispositivo["estado"] == True :  # 2: luces, 3: música
            dispositivo["estado"] = False
        if dispositivo["tipo"] == 1 and dispositivo["estado"] == False:
            dispositivo["estado"] = True
    return "Modo Noche activado: luces y equipos de música apagados, cámaras encendidas."

def apagar_modo_noche(dispositivos):
    for dispositivo in dispositivos:
        if dispositivo["tipo"] == 1 and dispositivo["estado"] == True:
            dispositivo["estado"] = False
    return "Modo Noche desactivado: cámaras apagadas."             

def configurar_hora_modo_noche(nueva_hora):
    if nueva_hora > 23 or nueva_hora < 0:
        return False
    
    global hora_activacion_modo_noche
    hora_activacion_modo_noche = nueva_hora

def verificar_hora_modo_noche(dispositivos):
    time = datetime.now()
    modo_fiesta, modo_noche = consultar_automatizaciones(dispositivos)

    # Para que el modo noche se active automaticamente, no debe estar activo el modo
    # fiesta ni el modo noche y tiene que ser la hora a la que esta configurada para
    # que se active
    if modo_fiesta or modo_noche or time.hour != hora_activacion_modo_noche:
        return False
    else:
        return True