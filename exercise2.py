"""Module providing a function printing python version."""
import datetime


def obtener_nombre_dia(fecha):
    """Function printing python version."""
    dias = ['Lunes', 'Martes', 'Miércoles',
            'Jueves', 'Viernes', 'Sábado', 'Domingo']
    nombre_d = dias[fecha.weekday()]
    return nombre_d


# Solicitar al usuario que ingrese la fecha
anio = int(input("Ingresa el año (formato AAAA): "))
mes = int(input("Ingresa el mes (número): "))
dia = int(input("Ingresa el día (número): "))

# Crear un objeto datetime con la fecha ingresada
fecha_dada = datetime.date(anio, mes, dia)

# Obtener el nombre del día
nombre_dia = obtener_nombre_dia(fecha_dada)

# Imprimir el resultado
print(f"El día es: {nombre_dia}")
