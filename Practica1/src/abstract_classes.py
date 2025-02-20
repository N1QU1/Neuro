import random
from abc import ABC, abstractmethod

# ==============================
# Class Connection
# ==============================
class Connection:
    def __init__(self, weight, neuron):
        self.weight = weight
        self.next_neuron = neuron
    

# ==============================
# Class Neuron
# ==============================
class Neuron(ABC):
    def __init__(self):
        self.connections = []

    def connect(self, weight: float, neuron):
        self.connections.append(Connection(weight, neuron))

    def initialize(self, input: float):
        self.input = input
    
    def propagate(self):
        for connection in self.connections:
            connection.next_neuron.input += self.output * connection.weight


# ==============================
# Class Layer
# ==============================
class Layer:
    def __init__(self):
        self.neurons = []

    def add_neuron(self, neuron):
        self.neurons.append(neuron)
    
    def add_neurons(self, neurons):
        self.neurons.extend(neurons)

    def connect_neuron(self, neuron_conn: Neuron, min_w: float, max_w: float):
        for neuron in self.neurons:
            neuron.connect(min_w, neuron_conn)
            
    def connect_layer(self, layer, min_w: float, max_w: float):
        for next_neuron in layer.neurons:
            self.connect_neuron(next_neuron, min_w, max_w)
    
    def initialize(self, value: int):
        for neuron in self.neurons:
            neuron.initialize(value)
    
    def fire(self):
        for neuron in self.neurons:
            neuron.fire()

    def propagate(self):
        for neuron in self.neurons:
            neuron.propagate()


# ==============================
# Class Net
# ==============================
class Network:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer): 
        self.layers.append(layer)
    
    def add_layers(self, layers):
        self.layers.extend(layers)
    
    def initialize(self, value:int):
        for layer in self.layers:
            layer.initialize(value)
    
    def fire(self):
        for layer in self.layers:
            layer.fire()

    def propagate(self):
        for layer in self.layers:
            layer.propagate()
    

class McCullochPitts(Neuron):
    def __init__(self, threshold):
        super().__init__()
        self.threshold = threshold
        
    def fire(self):
        if self.input >= self.threshold:
            self.output = 1
        else: self.output = 0


class Direct(Neuron):
    def __init__(self):
        super().__init__()
        
    def fire(self):
        self.output = self.input



"""def ej1():
    # ---------------------------
    # Crear la red y las capas
    # ---------------------------
    red = Network()
    
    # Crear dos capas: entrada y salida
    capa_entrada = Layer()
    capa_salida = Layer()
    
    # ---------------------------
    # Agregar neuronas a las capas
    # ---------------------------
    # En la capa de entrada, por ejemplo, agregamos dos neuronas.
    neurona_e1 = Neuron()
    neurona_e2 = Neuron()
    capa_entrada.add_neuron([neurona_e1, neurona_e2])
    
    # En la capa de salida, agregamos tres neuronas.
    neurona_s1 = Neuron()
    neurona_s2 = Neuron()
    neurona_s3 = Neuron()
    capa_salida.add_neuron([neurona_s1, neurona_s2, neurona_s3])
    
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
    print("Resultados en la capa de salida:")
    for idx, neurona in enumerate(capa_salida.neurons):
        print(f"Neurona {idx}: output = {neurona.output}")"""


def ej2():
    # Neurons creating
    sensor = Direct()
    alarm_delay = McCullochPitts(2)
    alarm = McCullochPitts(2)
    cooling_delay = McCullochPitts(2)
    cooling = McCullochPitts(2)

    # Layer creating
    entry_layer = Layer()
    alarm_delay_layer = Layer()
    alarm_layer = Layer()
    cooling_delay_layer = Layer()
    cooling_layer = Layer()

    # Network creating
    system_network = Network()

    # Neurons connections
    sensor.connect(2, alarm_delay)
    sensor.connect(1, alarm)
    alarm_delay.connect(1, alarm)
    alarm.connect(2, cooling_delay)
    alarm.connect(1, cooling)
    cooling_delay.connect(1, cooling)

    # Layers neuron adding
    entry_layer.add_neuron(sensor)
    alarm_delay_layer.add_neuron(alarm_delay)
    alarm_layer.add_neuron(alarm)
    cooling_delay_layer.add_neuron(cooling_delay)
    cooling_layer.add_neuron(cooling)

    # Network layer adding
    system_network.add_layers([entry_layer, alarm_delay_layer, alarm_layer, cooling_delay_layer, cooling_layer])

    entry_inputs = [0, 1, 1, 1, 1, 0, 0]

    system_network.initialize(0)

    # len(entry_inputs) stages
    for i, input in enumerate(entry_inputs):
        sensor.initialize(input)
        system_network.fire()
        system_network.initialize(0)
        system_network.propagate()

        print(f"Etapa: {1+i}")
        print(f"Alarm output: {alarm.output}")
        print(f"Cooling output: {cooling.output}")


if __name__ == "__main__":
    #ej1()
    ej2()