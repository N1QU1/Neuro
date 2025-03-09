from math import floor
import random
######Utils#######
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
######End of Utils#######





########LECTURAS#########
def read1(data_file, percentage):
    with open(data_file, 'r') as f:
        try:
            input_array = []
            output_array = []
            test_input_array = []
            test_output_array = []
            lines = f.readlines()
            line_number = len(lines) - 1
            reduced_line_number = floor(percentage * line_number)
            if reduced_line_number > line_number:
                raise Exception("Percentage must be between 0 and 1")
            attributes, classes = check_first_line_format(lines[0])

            random_lines = random.sample(lines[1:], reduced_line_number)
            unused_lines = list(set(lines[1:]) - set(random_lines))

            file_transformation(random_lines, attributes, classes, input_array, output_array)
            file_transformation(unused_lines, attributes, classes, test_input_array, test_output_array)
        except Exception as e:
            print(e)
    f.close()
    return input_array, output_array, test_input_array, test_output_array

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