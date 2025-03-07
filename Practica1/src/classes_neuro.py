import random
from abc import ABC, abstractmethod
from math import floor
import matplotlib.pyplot as plt
# ==============================
# Class Connection
# ==============================
class Connection:
    def __init__(self, weight, neuron):
        self.weight = weight
        self.next_neuron = neuron


class Neuron(ABC):
    def __init__(self):
        self.connections = []

    def connect(self, weight, neuron):
        self.connections.append(Connection(weight, neuron))

    def initialize(self, input):
        self.input = input

    def propagate(self):
        for connection in self.connections:
            connection.next_neuron.input += self.output * connection.weight


class Layer:
    def __init__(self):
        self.neurons = []

    def add_neuron(self, neuron: Neuron):
        self.neurons.append(neuron)

    def add_neurons(self, neurons):
        self.neurons.extend(neurons)

    def connect_neuron(self, neuron_conn, min_w, max_w):
        for neuron in self.neurons:
            neuron.connect(min_w, neuron_conn)

    def connect_layer(self, layer, min_w, max_w):
        for next_neuron in layer.neurons:
            self.connect_neuron(next_neuron, min_w, max_w)

    def initialize(self, value):
        for neuron in self.neurons:
            neuron.initialize(value)

    def fire(self):
        for neuron in self.neurons:
            neuron.fire()

    def propagate(self):
        for neuron in self.neurons:
            neuron.propagate()


class Network:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer):
        self.layers.append(layer)

    def add_layers(self, layers):
        self.layers.extend(layers)

    def initialize(self, value):
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
        else:
            self.output = 0


class Direct(Neuron):
    def __init__(self):
        super().__init__()

    def fire(self):
        self.output = self.input


class Perceptron(Neuron):
    def __init__(self, alpha, threshold):
        super().__init__()
        if 0 < alpha and alpha <= 1:
            self.alpha = alpha
        else:
            print("alpha must be greater than 0 and smaller than 1, set to default: 1")
            self.alpha = 1
        if threshold > 0:
            self.threshold = threshold
        else:
            print("threshold must be greater than 0, set to default: 0.2")
            self.threshold = 0.2

    def fire(self):
        if self.input > self.threshold:
            self.output = 1
        elif -self.threshold <= self.input <= self.threshold:
            self.output = 0
        else:
            self.output = -1


class Adaline(Perceptron):
    def __init__(self, alpha, threshold):
        super().__init__(alpha, threshold)

    def fire(self):
        if self.input >= 0:
            self.output = 1
        else:
            self.output = -1


class Bias(Neuron):
    def __init__(self):
        super().__init__()

    def fire(self):
        self.output = 1



# Ej3
def check_first_line_format(line):
    line_array = line.strip().split()
    if len(line_array) != 2:
        raise Exception("Error de formato: atributos (M) clases (N)")
    if not line_array[0].isdigit() or not line_array[1].isdigit():
        raise Exception("Error de formato en primer linea: int int)")
    else:
        attributes = int(line_array[0])
        classes = int(line_array[1])
    return attributes, classes

def file_transformation(lines, attributes, classes, input_array, output_array):
    for line in lines:
        input_array_line = [int(float(cell)) if float(cell).is_integer() else float(cell) for cell in
                            line.strip().split()]
        output_array_line = []
        i = 0
        if len(input_array_line) < attributes or len(
                input_array_line) < classes or len(input_array_line) < (attributes + classes):
            raise Exception(
                "Error en el formato, no puede haber mas entradas ni salidas que numeros insertados")
        #print("Inicio de removida input_array_line = {}".format(input_array_line))
        for i in range(classes):
            output_array_line.insert(0, input_array_line.pop())
            #print("input_array_line = {}".format(input_array_line))
            #print("Inicio de removida output_array_line = {}".format(output_array_line))
        input_array.append(input_array_line)
        output_array.append(output_array_line)

def read1(data_file, percentage):
    with open(data_file, 'r') as f:
        try:
            input_array = []
            output_array = []
            lines = f.readlines()
            line_number = len(lines) - 1
            reduced_line_number = floor(percentage * line_number)
            if reduced_line_number > line_number:
                raise Exception("Percentage must be between 0 and 1")
            attributes, classes = check_first_line_format(lines[0])

            random_lines = random.sample(lines[1:], reduced_line_number)

            file_transformation(random_lines, attributes, classes, input_array, output_array)
        except Exception as e:
            print(e)
    f.close()
    return input_array, output_array

def read2(data_file):
    with open(data_file, 'r') as f:
        try:
            lines = f.readlines()
            attributes, classes = check_first_line_format(lines[0])
            input_array = []
            output_array = []
            file_transformation(lines[1:], attributes, classes, input_array, output_array)
        except Exception as e:
            print(e)
    f.close()
    return input_array, output_array

def read3(learning_file, testing_file):
    with (
        open(learning_file, 'r') as f,
        open(testing_file, 'r') as t
    ):
        try:
            learning_lines = f.readlines()
            testing_lines = t.readlines()
            input_learning_array = []
            output_learning_array = []
            input_testing_array = []
            output_testing_array = []
            learning_attributes, learning_classes = check_first_line_format(learning_lines[0])
            testing_attributes, testing_classes = check_first_line_format(testing_lines[0])

            file_transformation(learning_lines[1:], learning_attributes, learning_classes, input_learning_array,
                                output_learning_array)
            file_transformation(testing_lines[1:], testing_attributes, testing_classes, input_testing_array,
                                output_testing_array)
        except Exception as e:
            print(e)
    f.close()
    return input_learning_array, output_learning_array, input_testing_array, output_testing_array

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
        print(f"Etapa: {1 + i}")
        print(f"Alarm output: {alarm.output}")
        print(f"Cooling output: {cooling.output}")

def train_perceptron(attributes,classes,alpha, threshold):
    network, input_layer, output_layer = init_monolayer_nn(len(attributes[0]), len(classes[0]), "perceptron", alpha,
                                                           threshold)

    # Iniciar el ciclo de entrenamiento
    changed = True  # Variable que controla el ciclo de entrenamiento
    counter = 0
    mse_list = []
    while changed:
        #tiene que encargarse de establecer el input de cada neurona de la capa a los valores de nuestro array
        changed = False
        mse = 0
        for atts, cla in zip(attributes, classes):
            for i, att in enumerate(atts):
                input_layer.neurons[i].initialize(att)
            network.fire()
            network.initialize(0)
            network.propagate()
            output_layer.fire()
            for c,o_neuron in zip(cla,output_layer.neurons):
                mse += 1 / len(classes) * (c - o_neuron.output) ** 2
                if o_neuron.output - c != 0:
                    for index,neuron in enumerate(input_layer.neurons):
                        for j,connection in enumerate(neuron.connections):
                            if index < len(attributes[0]):
                                connection.weight += c * o_neuron.alpha * atts[index]
                            else:
                                connection.weight += c * o_neuron.alpha
                    changed = True
        counter += 1
        mse_list.append(mse)
    return mse_list

def train_adaline(attributes, classes, alpha, threshold, max_epochs):

    network, input_layer, output_layer = init_monolayer_nn(len(attributes[0]), len(classes[0]), "adaline", alpha,
                                                           threshold)
    # Iniciar el ciclo de entrenamiento
    changed = True  # Variable que controla el ciclo de entrenamiento
    max_value = -99999999
    mse_list = []
    while changed and max_epochs > 0:
        #tiene que encargarse de establecer el input de cada neurona de la capa a los valores de nuestro array
        max_epochs -= 1
        mse = 0
        for atts, cla in zip(attributes, classes):
            for i, att in enumerate(atts):
                input_layer.neurons[i].initialize(att)
            network.fire()
            network.initialize(0)
            network.propagate()
            output_layer.fire()
            for c,o_neuron in zip(cla,output_layer.neurons):
                mse += (1 / len(classes)) * (c - o_neuron.output)** 2
                for index,neuron in enumerate(input_layer.neurons):
                    for connection in neuron.connections:
                        if index < len(attributes[0]):
                            variation = o_neuron.alpha * (c - o_neuron.input) * atts[index]
                            connection.weight += variation
                        else:
                            variation = o_neuron.alpha * (c - o_neuron.input)
                            connection.weight += variation
                        max_value = max(max_value, abs(variation))
        mse_list.append(mse)
        if max_value < threshold:
            changed = False
    return mse_list

def init_monolayer_nn(num_neuronas_input, num_neuronas_output, type, alpha, threshold):
    # Crear la red del perceptrón
    network = Network()
    input_layer = Layer()
    output_layer = Layer()

    # Añadir neuronas de entrada a la capa de entrada
    for _ in range(num_neuronas_input):
        input_layer.add_neuron(Direct())
    # anado el bias
    input_layer.add_neuron(Bias())
    # Añadir neuronas de salida a la capa de salida
    if (type == "adaline"):
        for _ in range(num_neuronas_output):
            output_layer.add_neuron(Adaline(alpha, threshold))
    else:
        for _ in range(num_neuronas_output):
            output_layer.add_neuron(Perceptron(alpha,threshold))
    # Añadir capas al perceptrón
    network.add_layers([input_layer, output_layer])

    # Conectar la capa de entrada a la capa de salida con pesos aleatorios
    min_w = 0
    max_w = 0
    input_layer.connect_layer(output_layer, min_w, max_w)

    # Primer initilize
    input_layer.initialize(0)
    output_layer.initialize(0)
    return network, input_layer, output_layer

def plot_list(l,x_label,y_label,title):
    plt.plot(l)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.show()

def ej_perceptron():
    attributes,classes=read2("nand.txt")
    mse_list = train_perceptron(attributes,classes,1,0.2)
    plot_list(mse_list, "Epoch", "MSE", "MSE Development")

def ej_adaline():
    attributes,classes=read2("and.txt")
    mse_list = train_adaline(attributes,classes,1,1e-5,30)
    plot_list(mse_list,"Epoch","MSE","MSE Development")

if __name__ == "__main__":
    # ej1()
    #ej2()
    #print(read2("and.txt"))
    ej_adaline()
    #ej_adaline()


