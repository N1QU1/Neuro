import classes_neuro as cn
def init_monolayer_nn(num_neuronas_input, num_neuronas_output, type, alpha, threshold):
    # Crear la red del perceptrón
    network = cn.Network()
    input_layer = cn.Layer()
    output_layer = cn.Layer()

    # Añadir neuronas de entrada a la capa de entrada
    for _ in range(num_neuronas_input):
        input_layer.add_neuron(cn.Direct())
    # anado el bias
    input_layer.add_neuron(cn.Bias())
    # Añadir neuronas de salida a la capa de salida
    if (type.lower() == "adaline"):
        for _ in range(num_neuronas_output):
            output_layer.add_neuron(cn.Adaline(alpha, threshold))
    else:
        for _ in range(num_neuronas_output):
            output_layer.add_neuron(cn.Perceptron(alpha,threshold))
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

def train_perceptron(network, input_layer, output_layer, inputs, expected_outputs, max_epochs):

    # Iniciar el ciclo de entrenamiento
    changed = True  # Variable que controla el ciclo de entrenamiento
    counter = 0
    mse_list = []
    accuracies = []
    while changed and max_epochs > 0:
        #tiene que encargarse de establecer el input de cada neurona de la capa a los valores de nuestro array
        changed = False
        mse = 0
        accuracy = 0
        for input, expected_output in zip(inputs, expected_outputs):
            for i, current_i in enumerate(input):
                input_layer.neurons[i].initialize(current_i)
            network.fire()
            network.initialize(0)
            network.propagate()
            output_layer.fire()
            for current_e_o,o_neuron in zip(expected_output,output_layer.neurons):
                error = current_e_o - o_neuron.output
                mse += error ** 2
                if o_neuron.output == current_e_o:
                    accuracy += 1
                if o_neuron.output - current_e_o != 0:
                    for index,neuron in enumerate(input_layer.neurons):
                        for j,connection in enumerate(neuron.connections):
                            if connection.next_neuron == o_neuron:
                                if index < len(inputs[0]):
                                    connection.weight += current_e_o * o_neuron.alpha * input[index]
                                else:
                                    connection.weight += current_e_o * o_neuron.alpha
                    changed = True
        accuracy /= len(inputs) * len(expected_outputs[0])
        accuracies.append(accuracy)
        mse /= len(inputs) * len(expected_outputs[0]) * len(inputs[0])
        mse_list.append(mse)
        max_epochs -= 1
    return mse_list, accuracies

def train_adaline(network, input_layer, output_layer, inputs, expected_outputs, threshold, max_epochs):
    # Iniciar el ciclo de entrenamiento
    changed = True  # Variable que controla el ciclo de entrenamiento
    mse_list = []
    accuracies = []
    while changed and max_epochs > 0:
        max_epochs -= 1
        mse = 0
        max_value = 0.0
        accuracy = 0
        for input, expected_output in zip(inputs, expected_outputs):
            for i, current_i in enumerate(input):
                input_layer.neurons[i].initialize(current_i)
            network.fire()
            network.initialize(0)
            network.propagate()
            output_layer.fire()
            for current_e_o,o_neuron in zip(expected_output,output_layer.neurons):
                error = current_e_o - o_neuron.output
                mse += error ** 2
                for index,neuron in enumerate(input_layer.neurons):
                    for connection in neuron.connections:
                        if connection.next_neuron == o_neuron:
                            if index < len(inputs[0]):
                                variation = o_neuron.alpha * error * input[index]
                                connection.weight += variation
                            else:
                                variation = o_neuron.alpha * error
                                connection.weight += variation
                            max_value = max(max_value, abs(variation))
                if o_neuron.output == current_e_o:
                    accuracy += 1
        accuracy /= len(inputs) * len(expected_outputs[0])
        accuracies.append(accuracy)
        mse /= len(inputs) * len(expected_outputs[0]) * len(inputs[0])
        mse_list.append(mse)
        if max_value < threshold:
            changed = False

    return mse_list, accuracies

def exploit_network(network, input_layer, output_layer, inputs, expected_outputs, max_epochs):
    accuracies = []
    if len(inputs) == 0 or len(expected_outputs) == 0:
        return accuracies
    for i in range(max_epochs):
        accuracy = 0
        for input, expected_output in zip(inputs, expected_outputs):
            for j, current_i in enumerate(input):
                input_layer.neurons[j].initialize(current_i)
                for current_e_o, o_neuron in zip(expected_output, output_layer.neurons):
                    if o_neuron.output == current_e_o:
                        accuracy += 1
        accuracy /= len(inputs) * len(expected_outputs[0]) * len(inputs[0])
        accuracies.append(accuracy)
    return accuracies