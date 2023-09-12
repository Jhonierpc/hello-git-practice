from matplotlib import pyplot as plt

# Definir los nombres de las ramas
ramas = ['Master', 'Develop', 'Feature', 'Release', 'Hotfix']

# Definir las conexiones entre las ramas
conexiones = [(0, 1), (1, 2), (1, 3), (0, 4)]

# Crear la figura
fig, ax = plt.subplots()

# Dibujar las ramas y las conexiones
for i, rama in enumerate(ramas):
    ax.text(0, i, rama, va='center', ha='right', fontweight='bold', fontsize=12)
    ax.plot([0.05, 1], [i, i], color='black')

for conexion in conexiones:
    ax.plot([0.95, 1.1, 1.1], [conexion[0], conexion[0], conexion[1]], color='black')

# Configurar la apariencia del gráfico
ax.axis('off')
plt.show()
