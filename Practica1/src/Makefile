# Definir el intérprete de Python
PYTHON = python3

# Nombre del archivo principal
EJE1 = eje1/eje1.py
MC_PITTS = eje2/mc_pitts.py
TEST = eje4_2_2/test_models.py
DATASET ?= and.txt
EPOCHS ?= 1000
TEST_EPOCHS ?= 800
LR ?= 0.01

# Objetivo de ayuda
.PHONY: ayuda_eje1
ayuda_eje1:
	@echo "Uso del programa:"
	@echo "  make compila_eje1   - No es necesario para Python, pero reservado por estructura."
	@echo "  make ejecuta_eje1   - Ejecuta el script de prueba de la red neuronal."
	@echo "  make ayuda_eje1     - Muestra este mensaje."

# Objetivo de compilación (No es necesario en Python, pero se mantiene por estructura)
.PHONY: compila_eje1
compila_eje1:
	@echo "Python no requiere compilación explícita."

# Objetivo de ejecución
.PHONY: ejecuta_eje1
ejecuta_eje1:
	$(PYTHON) $(EJE1)

# Objetivo de ayuda
.PHONY: ayuda_mp
ayuda_mp:
	@echo "Uso del programa:"
	@echo "  make compila_mp   - No es necesario para Python, pero reservado por estructura."
	@echo "  make ejecuta_mp   - Ejecuta el script de prueba de la red neuronal."
	@echo "  make ayuda_mp     - Muestra este mensaje."

# Objetivo de compilación (No es necesario en Python, pero se mantiene por estructura)
.PHONY: compila_mp
compila_mp:
	@echo "Python no requiere compilación explícita."

# Objetivo de ejecución
.PHONY: ejecuta_mp
ejecuta_mp:
	$(PYTHON) $(MC_PITTS)


.PHONY: compilar ayuda_perceptron ejecuta_perceptron ayuda_adaline ejecuta_adaline clean

# Mostrar ayuda para ejecutar el perceptrón
ayuda_perceptron:
	@echo "Uso del perceptrón:"
	@echo "make ejecuta_perceptron DATASET=\"and.txt\" EPOCHS=200 LR=0.02 THRESHOLD=0.01 SPLIT=0.7 TYPE=\"perceptron\" TEST_EPOCHS=500"
	@echo "Argumentos:"
	@echo "  --split        Porcentaje que queremos de conjunto de entrenamiento, valores de 0 < x <= 1 "
	@echo "  --type        Ejercicio a ejecutar, adaline o perceptron"
	@echo "  --data        Archivo con datos de entrenamiento"
	@echo "  --epochs      Número de épocas para el entrenamiento"
	@echo "  --lr          Tasa de aprendizaje (learning rate)"
	@echo "  --test_epochs Número de épocas para la evaluación"

# Ejecutar el perceptrón con datos reales y modo correcto
ejecuta_perceptron:
	@$(PYTHON) $(TEST) --file_path $(DATASET) --type perceptron --split $(SPLIT) --threshold $(THRESHOLD)  --lr $(LR) --epochs $(EPOCHS) --test_epochs $(TEST_EPOCHS)

# Mostrar ayuda para ejecutar el modelo Adaline
ayuda_adaline:
	@echo "Uso de Adaline:"
	@echo "make ejecuta_adaline DATASET=\"and.txt\" EPOCHS=200 LR=0.02 THRESHOLD=0.01 SPLIT=0.7 TYPE=\"adaline\" TEST_EPOCHS=500"
	@echo "Argumentos:"
	@echo "  --split        Porcentaje que queremos de conjunto de entrenamiento, valores de 0 < x <= 1 "
	@echo "  --type        Ejercicio a ejecutar, adaline o perceptron"
	@echo "  --data        Archivo con datos de entrenamiento"
	@echo "  --epochs      Número de épocas para el entrenamiento"
	@echo "  --lr          Tasa de aprendizaje (learning rate)"
	@echo "  --test_epochs Número de épocas para la evaluación"

# Ejecutar Adaline con datos reales y modo correcto
ejecuta_adaline:
	@$(PYTHON) $(TEST) --file_path $(DATASET) --type adaline --split $(SPLIT) --threshold $(THRESHOLD) --lr $(LR) --epochs $(EPOCHS) --test_epochs $(TEST_EPOCHS)

