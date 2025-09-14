from enum import Enum

class Rol(Enum):
    USUARIO = 1
    ADMIN = 2
    DUENO = 3

def gestor_usuarios():

    usuarios: list[dict] = [
        {
            "username": "JuanPerez",
            "nombre": "Juan",
            "apellido": "Perez",
            "contraseña": "1234",
            "rol": Rol.ADMIN.value,
            "email": "juan.perez@email.com"
        },
        {
            "username": "AnaLopez",
            "nombre": "Ana",
            "apellido": "Lopez",
            "contraseña": "5678",
            "rol": Rol.USUARIO.value,
            "email": "ana.lopez@email.com"
        },
        {
            "username": "CarlosGomez",
            "nombre": "Carlos",
            "apellido": "Gomez",
            "contraseña": "abcd",
            "rol": Rol.DUENO.value,
            "email": "carlos.gomez@email.com"
        },
        {
            "username": "MariaGarcia",
            "nombre": "Maria",
            "apellido": "Garcia",
            "contraseña": "abcd",
            "rol": Rol.USUARIO.value,
            "email": "maria.garcia@email.com"
        }
    ]

    def buscar_por_email(email):
        for i in usuarios:
            if email == i["email"]:
                return True
        return False 
    
    def buscar_por_usuario(usuario):
        for i in range(len(usuarios)):
            if usuario == usuarios[i]['username']:
                return i
        return None

    def registrar_usuario(nombre, apellido, usuario, constrasenia, email):
        if buscar_por_usuario(usuario) != None:
            usuarios.append({
                "username": usuario,
                "nombre": nombre,
                "apellido": apellido,
                "contrasenia": constrasenia,
                "email": email,
            })
            return True
        return False

    def iniciar_sesion(usuario, contrasenia):
        indice_usuario = buscar_por_usuario(usuario)

        if indice_usuario != None and usuarios[indice_usuario]["contraseña"] == contrasenia:
            rol = Rol(usuarios[indice_usuario]["rol"])
            print(f"{usuario} Se inicio sesion con exito")
            return usuario, rol
        else:
            print("Error: Usuario o contraseña incorrectos")
            return None, None
        
    def consultar_datos_personales(usuario):
        indice_usuario = buscar_por_usuario(usuario)
    
        if indice_usuario != None and usuario == usuarios[indice_usuario]['username']:
            print(f"\n--- DATOS PERSONALES---")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Apellido: {usuario['apellido']}")
            print(f"Email: {usuario['email']}")
            print(f"Rol: {usuario['rol']}")
        else:    
            print("Error: No se encontraron los datos del usuario.")

    def listar_usuarios():
        print(f"\n--- Lista de usuarios---")
        for i in range(len(usuarios)):
            datos_usuario = usuarios[i]
            rol_numero = datos_usuario['rol']
            rol_texto = ""
            if rol_numero == 1:
                rol_texto = "Usuario"
            elif rol_numero == 2:
                rol_texto = "Admin"
            elif rol_numero == 3:
                rol_texto = "Dueno"
            print(f"- Usuario: {usuarios[i]['username']} | Rol: {rol_texto}")

    def modificar_rol_usuario(usuario_a_modificar: str, nuevo_rol_valor: int):
        indice_usuario = buscar_por_usuario(usuario_a_modificar)

        if indice_usuario == None:
            return "Error: El usuario ingresado no existe."

        if nuevo_rol_valor < 1 or nuevo_rol_valor > 3:
            return f"El rol '{nuevo_rol_valor}' no es un número de rol válido (debe ser 1, 2 o 3)."
        
        usuarios[indice_usuario]['rol'] = nuevo_rol_valor
        
        return f"El rol de '{usuario_a_modificar}' ha sido actualizado."
    
    return (
        consultar_datos_personales,
        iniciar_sesion,
        registrar_usuario,
        listar_usuarios,
        modificar_rol_usuario,
        buscar_por_email,
    )