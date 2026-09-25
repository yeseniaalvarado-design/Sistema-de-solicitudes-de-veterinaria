from datetime import datetime

# Lista de campus permitidos
CAMPUS_PERMITIDOS = [
    "Campus medellin - Ciudad Universitaria",
    "Campus medellin - Ciudadela Robledo",
    "Campus en el Area de la salud",
    "Campus medellin - Sede de Posgrado",
    "Campus medellin - Edificio San Ignacio",
    "Campus medellin - Antigua Escuela de Derecho",
    "Campus medellin - Edificio Antioquia",
    "Campus medellin - Casas Patrimoniales",
    "Campus medellin - Edificio de Extension"
]

def validar_nombre(nombre: str) -> bool:
    """ Valida que el nombre tenga entre 3 y 100 caracteres y no contenga numeros. """
    nombre = nombre.strip()
    
    # Validar longitud
    if len(nombre) < 3 or len(nombre) > 100:
        return False
        
    # Verificar que no contenga numeros
    for caracter in nombre:
        if caracter.isdigit():  # Si encuentra algun numero, es invalido
            return False
            
    return True


def validar_tipo_doc(tipo: str) -> bool:
    """ Valida que el tipo de documento sea una de las opciones permitidas. """
    tipos_validos = ["CC", "TI", "CE", "PP", "NIT"]
    return tipo.strip().upper() in tipos_validos


def validar_num_doc(numero: str) -> bool:
    """ Valida que el documento sea solo numeros y tenga entre 3 y 15 digitos. """
    numero = numero.strip()
    
    # Comprobar que todos sean numeros y la longitud este en el rango
    if numero.isdigit() and 3 <= len(numero) <= 15:
        return True
    return False


def validar_tipo_tel(tipo: str) -> bool:
    """ Valida las opciones de tipo de telefono. """
    tipos_validos = ["Celular", "Fijo", "Corporativo", "Otro"]
    return tipo.strip().capitalize() in tipos_validos


def validar_telefono(telefono: str) -> bool:
    """ Valida que el telefono tenga exactamente 10 digitos numericos. """
    telefono = telefono.strip()
    return telefono.isdigit() and len(telefono) == 10


def validar_correo(correo: str) -> bool:
    """ Valida de forma sencilla que el correo tenga '@', un punto '.' y no supere 254 caracteres. """
    correo = correo.strip()
    
    if len(correo) > 254:
        return False
        
    # Verificacion basica para principiantes: debe tener '@' y '.'
    if "@" in correo and "." in correo:
        return True
        
    return False


def validar_direccion(direccion: str) -> bool:
    """ La direccion es opcional. Si se ingresa, debe tener entre 5 y 200 caracteres. """
    direccion = direccion.strip()
    if direccion == "":
        return True  # Es opcional, asi que vacia es valida
    
    return 5 <= len(direccion) <= 200


def validar_tipo_solicitud(tipo: str) -> bool:
    """ Valida que sea Peticion, Queja, Reclamo o Sugerencia. """
    solicitudes_validas = ["Peticion", "Peticion", "Queja", "Reclamo", "Sugerencia"]
    return tipo.strip().capitalize() in solicitudes_validas


def validar_canal(canal: str) -> bool:
    """ Valida los canales de recepcion permitidos. """
    canales_validos = ["Presencial", "Correo electronico", "Pagina web", "Telefono", "Redes sociales", "Otro"]
    return canal.strip() in canales_validos


def validar_asunto(asunto: str) -> bool:
    """ Valida la longitud del asunto entre 5 y 150 caracteres. """
    asunto = asunto.strip()
    return 5 <= len(asunto) <= 150


def validar_descripcion(descripcion: str) -> bool:
    """ Valida que la descripcion tenga entre 20 y 2000 caracteres. """
    descripcion = descripcion.strip()
    return 20 <= len(descripcion) <= 2000


def validar_mascota(mascota: str) -> bool:
    """ Valida el tipo de mascota. """
    mascotas_validas = ["Perro", "Gato", "Otro"]
    return mascota.strip().capitalize() in mascotas_validas


def validar_campus(campus: str) -> bool:
    """ Verifica que el campus seleccionado este en la lista permitida. """
    return campus.strip() in CAMPUS_PERMITIDOS