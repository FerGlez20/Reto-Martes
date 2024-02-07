def validar_entrada(cadena, longitud_minima=5, longitud_maxima=50):
    if len(cadena) < longitud_minima or len(cadena) > longitud_maxima:
        return False
    else:
        return True

def validar_telefono(telefono):
    if len(telefono) != 10:
        return False
    elif not telefono.isdigit():
        return False
    else:
        return True

def registro_usuario():
    while True:
        nombre = input("Ingrese su nombre: ")
        if validar_entrada(nombre):
            break
        else:
            print("El nombre debe tener entre 5 y 50 caracteres.")

    while True:
        apellido = input("Ingrese su apellido: ")
        if validar_entrada(apellido):
            break
        else:
            print("El apellido debe tener entre 5 y 50 caracteres.")

    while True:
        telefono = input("Ingrese su número de teléfono: ")
        if validar_telefono(telefono):
            break
        else:
            print("El número de teléfono debe ser de 10 dígitos.")

    while True:
        correo = input("Ingrese su correo electrónico: ")
        if validar_entrada(correo):
            break
        else:
            print("El correo electrónico debe tener entre 5 y 50 caracteres.")

    return nombre, apellido, telefono, correo

def bienvenida(usuario):
    nombre_completo = usuario[0] + " " + usuario[1]
    correo_usuario = usuario[3]
  
    print("Hola " + nombre_completo + ", en breve recibirás un correo a " + correo_usuario)

def registrar_usuarios():
    num_usuarios = int(input("¿Cuántos usuarios desea registrar? "))

    for _ in range(num_usuarios):
        usuario = registro_usuario()
        bienvenida(usuario)

registrar_usuarios()