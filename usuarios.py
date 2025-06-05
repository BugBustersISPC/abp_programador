from roles import Rol

def buscar_por_email(email, lista):
    for i in lista:
        if email == i["email"]:
            return True

    return False 


def registrar_usuario(cuentas: list, nombre, apellido, email, contraseña):
    if not buscar_por_email(email, cuentas):
        cuentas.append({
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "contraseña": contraseña,
            "rol": Rol.USUARIO.value
        })
        return True
    return False