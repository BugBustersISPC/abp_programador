from roles import Rol

def buscar_por_email(email, lista):
    for i in lista:
        if email == i["email"]:
            return True

    return False 


def registrar_usuario(cuentas: dict, nombre, apellido, email, contraseña):
    if email not in cuentas:
        cuentas[email] = {
            "nombre": nombre,
            "apellido": apellido,
            "contraseña": contraseña,
            "rol": Rol.USUARIO.value
        }
        return True
    return False

def iniciar_sesion(cuentas, usuario, contraseña):
    if usuario in cuentas and cuentas[usuario]["contraseña"] == contraseña:
        rol = Rol(cuentas[usuario]["rol"])
        print(f"{usuario} Se inicio sesion con exito")
        return usuario, rol
    else:
        print("Error: Usuario o contraseña incorrectos")
        return None