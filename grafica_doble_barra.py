import matplotlib
import matplotlib.pyplot as plt
import numpy as np

asistencia = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

#Obtenemos la posicion de cada etiqueta en el eje de X
x = np.arange(len(asistencia))
#tamaño de cada barra
width = 0.35

fig, ax = plt.subplots()

#Generamos las barras para el conjunto de hombres
rects1 = ax.bar(x - width/2, men_means, width, label='Hombres')
#Generamos las barras para el conjunto de mujeres
rects2 = ax.bar(x + width/2, women_means, width, label='Mujeres')

#Añadimos las etiquetas de identificacion de valores en el grafico
ax.set_ylabel('Asistencia')
ax.set_title('Asistencia de Hombres y Muejes')
ax.set_xticks(x)
ax.set_xticklabels(asistencia)
#Añadimos un legen() esto permite mmostrar con colores a que pertence cada valor.
ax.legend()

def autolabel(rects):
    """Funcion para agregar una etiqueta con el valor en cada barra"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

#Añadimos las etiquetas para cada barra
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.savefig('doble_barra.png')
#Mostramos la grafica con el metodo show()
plt.show()