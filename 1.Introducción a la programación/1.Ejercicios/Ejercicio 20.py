# Escribir un programa que muestre por pantalla el resultado de dos sumas de 3 variables, una de tipo int, una de tipo float y otra de tipo bool que primero tomará el valor True y luego el valor False. (analice la situación y responda qué sucedió)

# Variables con valores de distinto tipo
variable_entera = 5
variable_flotante = 2.5
variable_booleana = True

# Sumas de variables
suma_entera_float = variable_entera + variable_flotante
suma_entera_booleana = variable_entera + variable_booleana
suma_float_booleana = variable_flotante + variable_booleana

# Mostrar resultados
print(f"La suma de variable_entera y variable_flotante es: {suma_entera_float}")
print(f"La suma de variable_entera y variable_booleana es: {suma_entera_booleana}")
print(f"La suma de variable_flotante y variable_booleana es: {suma_float_booleana}")

# Análisis:
# La suma de variable_entera y variable_flotante es correcta porque ambos son números y se pueden sum
# La suma de variable_entera y variable_booleana es incorrecta porque se está sumando un número con
# un valor booleano, lo que no tiene sentido en el contexto de las matemáticas.


# Ahora, si cambiamos el valor de variable_booleana a False
variable_booleana = False

# Sumas nuevamente
suma_entera_float = variable_entera + variable_flotante
suma_entera_booleana = variable_entera + variable_booleana
suma_float_booleana = variable_flotante + variable_booleana

# Mostrar resultados nuevamente
print(f"La suma de variable_entera y variable_flotante es: {suma_entera_float}")
print(f"La suma de variable_entera y variable_booleana es: {suma_entera_booleana}")
print(f"La suma de variable_flotante y variable_booleana es: {suma_float_booleana}")

# Análisis:
# La suma de variable_entera y variable_flotante sigue siendo correcta porque ambos son números y se pueden
# sumar.
# La suma de variable_entera y variable_booleana sigue siendo incorrecta porque se está sumando un número
# con un valor booleano, lo que no tiene sentido en el contexto de las matemáticas
# La suma de variable_flotante y variable_booleana sigue siendo incorrecta porque se está sumando un número
# con un valor booleano, lo que no tiene sentido en el contexto de las matemáticas
# En resumen, la suma de un número con un valor booleano siempre es incorrecta.
# La suma de dos números siempre es correcta.  # La suma de un número con un
# valor booleano siempre es incorrecta.  # La suma de dos números siempre es correcta
# La suma de un número con un valor booleano siempre es incorrecta.  # La suma
# de dos números siempre es correcta.  # La suma de un número con un valor boolean
# o siempre es incorrecta.  # La suma de dos números siempre es correcta.
