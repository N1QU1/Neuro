import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import classes_neuro as cn

# ---------------------------
# Crear la red y las capas
# ---------------------------
red = cn.Network()

# Crear dos capas: entrada y salida
capa_entrada = cn.Layer()
capa_salida = cn.Layer()

# ---------------------------
# Agregar neuronas a las capas
# ---------------------------
# En la capa de entrada, por ejemplo, agregamos dos neuronas.
neurona_e1 = cn.Direct()
neurona_e2 = cn.Direct()
capa_entrada.add_neurons([neurona_e1, neurona_e2])

# En la capa de salida, agregamos tres neuronas.
neurona_s1 = cn.Direct()
neurona_s2 = cn.Direct()
neurona_s3 = cn.Direct()
capa_salida.add_neurons([neurona_s1, neurona_s2, neurona_s3])

# Agregar las capas a la red
red.add_layer(capa_entrada)
red.add_layer(capa_salida)

# ---------------------------
# Conectar las capas
# ---------------------------
# Conectamos cada neurona de la capa de entrada con cada neurona de la capa de salida.
# Se utiliza un peso fijo (por ejemplo, 2.0). (El parámetro max_w no se utiliza en el código actual).
capa_entrada.connect_layer(capa_salida, min_w=2.0, max_w=2.0)

# ---------------------------
# Inicializar las neuronas
# ---------------------------
# Inicializamos la capa de entrada con un valor (por ejemplo, 3)
# y la capa de salida con 0 (para comenzar sin aporte previo).
print("inicializamos las neuronas, con un valor de 3, y realizamos una red de conexiones densas con pesos de 2")
capa_entrada.initialize(3)
capa_salida.initialize(0)

# ---------------------------
# Activar y propagar
# ---------------------------
# Primero, activamos la capa de entrada: esto copia el valor de input a output.
capa_entrada.fire()

# Luego, propagamos desde la capa de entrada.
# Cada neurona de la capa de entrada recorrerá sus conexiones y sumará a la input de cada neurona conectada:
#    next_neuron.input += self.output * weight
capa_entrada.propagate()

# Finalmente, activamos la capa de salida para que sus outputs sean iguales a sus inputs (ya actualizados).
capa_salida.fire()

# ---------------------------
# Mostrar resultados
# ---------------------------
print("Al efectuar la formula de la propagacion sumamos las entradas pesadas, esperamos un valor de 12"
      "obtenido de (2*3 + 2*3) o la suma pesada de las entradas:")
print("Resultados en la capa de salida:")
for idx, neurona in enumerate(capa_salida.neurons):
    print(f"Neurona {idx}: output = {neurona.output}")

