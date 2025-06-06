from roles import Rol

def buscar_por_email(email, lista):
    for i in lista:
        if email == i["email"]:
            return True

    return False 


def registrar_usuario(cuentas: dict, nombre, apellido, usuario, contraseña, email):
    if usuario not in cuentas:
        cuentas[usuario] = {
            "nombre": nombre,
            "apellido": apellido,
            "contraseña": contraseña,
            "email": email,
            "rol": Rol.USUARIO.value,
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
        return None, None
    
def consultar_datos_personales(usuario, cuentas):
    if usuario in cuentas:
        usuario = cuentas[usuario]
        print(f"\n--- DATOS PERSONALES---")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Apellido: {usuario['apellido']}")
        print(f"Email: {usuario['email']}")
        print(f"Rol: {usuario['rol']}")
    else:
        print("Error: No se encontraron los datos del usuario.")
