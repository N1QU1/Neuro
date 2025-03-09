
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

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

####A partir de aqui definiremos funciones utiles que utilizaremos a lo largo de todos los codigos####

def plot_list(l,x_label,y_label,title):
    plt.plot(l)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.show()






