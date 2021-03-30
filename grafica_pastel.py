import matplotlib
import matplotlib.pyplot as plt
import numpy as np

medios_transporte = 'Vehiculos', 'Motocicletas', 'Bicicleta', 'Metro'
#Declaramos el tamaño de cada 'rebanada' y en sumatoria todos deben dar al 100%
sizes = [45, 30, 15, 10]
#En este punto señalamos que posicion debe 'resaltarse' y el valor, si se coloca 0, se omite
explode = (0.1, 0, 0, 0)  

fig1, ax1 = plt.subplots()
#Creamos el grafico, añadiendo los valores
ax1.pie(sizes, explode=explode, labels=medios_transporte, autopct='%1.1f%%',
        shadow=True, startangle=90)
#señalamos la forma, en este caso 'equal' es para dar forma circular
ax1.axis('equal')
plt.title("Principal Medio de Transporte")
plt.legend()
plt.savefig('grafica_pastel.png')
plt.show()