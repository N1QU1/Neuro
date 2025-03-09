import sys
import os
import argparse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import lecturas as l
import perceptron_adaline as pa
import classes_neuro as cn


def main(file_path, type, split, threshold,lr, epochs, test_epochs):
    # Leer los datos
    inputs, expected_outputs, inputs_test, expected_outputs_test = l.read1("texts/"+ file_path, split)

    if type == "perceptron":
        network, input_layer, output_layer = pa.init_monolayer_nn(len(inputs[0]), len(expected_outputs[0]),
                                                                  "perceptron", lr,
                                                                  threshold)
        mse_list, accuracy_list = pa.train_perceptron(network, input_layer, output_layer, inputs, expected_outputs, epochs)
    elif type == "adaline":
        network, input_layer, output_layer = pa.init_monolayer_nn(len(inputs[0]), len(expected_outputs[0]),
                                                                  "adaline", lr,
                                                                  threshold)
        mse_list, accuracy_list = pa.train_adaline(network, input_layer, output_layer, inputs, expected_outputs, threshold, epochs)
    else:
        print("Type ha de ser incluido para el correcto funcionamiento del script")
        return

    cn.plot_list(mse_list, "Epoch", "MSE", "MSE Development")
    cn.plot_list(accuracy_list, "Epoch", "Accuracy", "Accuracy Development")
    # Evaluar la red neuronal
    accuracies = pa.exploit_network(network, input_layer, output_layer, inputs_test, expected_outputs_test, test_epochs)
    if accuracies == 0:
        print("No se ha podido realizar el test porque no se ha divido la muestra")
    # Graficar los resultados
    cn.plot_list(accuracies, "Epoch", "Accuracy", "Accuracy Development On Test Sample")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutar entrenamiento de una red neuronal perceptrón.")
    parser.add_argument("--file_path", type=str, help="Ruta al archivo de datos.")
    parser.add_argument("--type", type=str, help="Tipo de problema a ejecutar")
    parser.add_argument("--split", type=float, default=0.8, help="Proporción de datos de entrenamiento.")
    parser.add_argument("--threshold", type=float, default=0.2, help="Umbral de activación del perceptrón.")
    parser.add_argument("--lr", type=float, default=1, help="Tasa de aprendizaje")
    parser.add_argument("--epochs", type=int, default=1000, help="Número de épocas para el entrenamiento.")
    parser.add_argument("--test_epochs", type=int, default=800, help="Número de épocas para la evaluación.")

    args = parser.parse_args()

    main(args.file_path, args.type, args.split, args.threshold, args.lr, args.epochs, args.test_epochs)