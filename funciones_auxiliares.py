def input_int(mensaje, val_min=None, val_max=None):
    while True:
        try:
            valor = int(input(mensaje))
            if (val_min is not None and valor < val_min) or (val_max is not None and valor > val_max):
                print(f"Por favor ingrese un número entre {val_min} y {val_max}.")
                continue
            return valor
        except ValueError:
            return "Por favor ingrese un número válido."

def input_estado():
    while True:
        estado = input("¿Esta activo? (si/no): ").strip().lower()
        if estado == "si":
            return True
        elif estado == "no":
            return False
        else:
            return "Por favor ingrese 'si' o 'no'."

def input_confirmacion(mensaje="¿Está seguro? (si/no): "):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("si", "no"):
            return respuesta
        return "Por favor ingrese 'si' o 'no'."
