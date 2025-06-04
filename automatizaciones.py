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