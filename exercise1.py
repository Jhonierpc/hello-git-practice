# Crear una lista para almacenar los datos de las personas
personas = []

# Definir una función para ingresar los datos de una persona
def ingresar_persona():
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el apellido: ")
    edad = input("Ingresa la edad: ")

    # Crear un diccionario con los datos de la persona
    persona = {"Nombre": nombre, "Apellido": apellido, "Edad": edad}

    # Agregar el diccionario a la lista de personas
    personas.append(persona)

# Solicitar datos de varias personas
while True:
    ingresar = input("¿Deseas ingresar datos de una persona? (s/n): ")
    if ingresar.lower() != "s":
        break
    ingresar_persona()

# Mostrar los datos de todas las personas
print("\nDatos de las personas:")
for idx, persona in enumerate(personas, start=1):
    print(f"Persona {idx}:")
    print(f"Nombre: {persona['Nombre']}")
    print(f"Apellido: {persona['Apellido']}")
    print(f"Edad: {persona['Edad']}")
    print()
