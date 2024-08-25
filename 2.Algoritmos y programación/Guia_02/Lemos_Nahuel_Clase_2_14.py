# Alumno: Lemos, Nahuel

# Funciones recursivas:

# Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertir(texto):
    # Si el texto está vacío, se devuelve el texto
    if len(texto) == 0:
        return texto
    # Devuelve el texto invertido (sin el primer carácter) más el primer carácter al final
    return (invertir(texto[1:]) + texto[0])
