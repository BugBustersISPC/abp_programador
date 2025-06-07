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


def listar_usuarios(cuentas: dict):
    print(f"\n--- Lista de usuarios---")
    for usuario in cuentas:
        datos_usuario = cuentas[usuario]
        rol_numero = datos_usuario['rol']
        rol_texto = ""
        if rol_numero == 1:
            rol_texto = "Usuario"
        elif rol_numero == 2:
            rol_texto = "Admin"
        elif rol_numero == 3:
            rol_texto = "Dueno"

    print(f"- Usuario: {usuario} | Rol: {rol_texto}")



def modificar_rol_usuario(cuentas: dict, usuario_a_modificar: str, nuevo_rol_valor: int):
    if usuario_a_modificar not in cuentas:
        return "Error: El usuario ingresado no existe."

    if nuevo_rol_valor < 1 or nuevo_rol_valor > 3:
        return f"El rol '{nuevo_rol_valor}' no es un número de rol válido (debe ser 1, 2 o 3)."
    
    cuentas[usuario_a_modificar]['rol'] = nuevo_rol_valor
    
    return f"El rol de '{usuario_a_modificar}' ha sido actualizado."