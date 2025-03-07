# Memoria Practica 1 Neurocomputacion
## Ejercicio 2.1
Para la realizacion del ejercicio, hemos realizado una red de neuronas mcculloch Pitts
cabe destacar que el resultado que obtenemos no es igual al presentado en la tabla del enunciado 
debido a:
 - Este no tiene en cuenta que la funcion fire se ha de ejecutar con un desfase respecto a cuando llega el input
por la mera definicion de mcculloch pitts se presenta un desfase de 1 tiempo respecto al input recibido y dicha tabla 
no lo respeta

 - Para probar dicho funcionamiento encontrara en la funcion ej1 la ejecucion de nuestra red en ella se puede apreciar
los outputs de la misma y como responde a las distintas entradas
### Estructura de la red
![](diseno_mc_pitts.png)

## Ejercicio 3

Encontrará las distintas funciones requeridas realizadas y con una breve explicacion al pie de cada una.

## Ejercicio 4

Las Fronteras de los algoritmos utilizando una inicializacion de pesos a cero, un aprendizaje de 1 y un threshold de 
0.2 son:

### Perceptrón:
 - And.txt: 2x1 + 3x2 = 4
 - Or.txt: 2x1 + 2x2 = 1
 - Nand.txt: 3x1 + 2x2 = -4  
### Adaline
 - And.txt: 2x1 + 4x2 = 4
 - Or.txt: 2x1 + 2x2 = 2
 - Nand.txt: 2x1 + 4x2 = -4

El problema que no puede solucionarse resulta ser la puerta xor, esto se debe principalmente a que es un problema no separable
linealmente, presentandose como un problema imposible para perceptrones o adaline de una sola capa, esto podria resolverse
metiendo una o varias capas ocultas de tal manera que permitamos al perceptron o adaline resolver problemas mas complejos.


### Ejercicio 4.2
Tanto nuestro Adaline como nuestro Perceptron comparten estructura, estos se basan en el uso de un forward, encargado de 
generar una respuesta sin delay. Ambos miden el MSE en cada una de sus épocas y además son capaces de minimizarlo mediante
la actualización de los distintos pesos en las conecciones de la red.

El MSE se reduce hasta converger en los problemas linealmente separables, en aquellos que no lo son ha de acercarse a cero
y parar en la época definida por nosotros puesto, que sino simplemente oscilarían los valores hasta el infinito.
### Ejercicio 4.3
Los distintos parámetros a incluir pueden generar una gran variedad de cambios:
- Max epochs limita el número máximo de épocas de estudio, esto nos permite ver en casos como el de los problemas real 1 y 2
, que el mse se reduce, pero no podemos hacerlo converger, puesto que el sistema no es capaz de analizar problemas no lineales.

- El alpha se encarga de la tasa de aprendizaje del sistema, en caso de ser muy grande puede no ser suficientemente preciso
y en caso de ser demasiado pequeño puede llevarnos a caer en mínimos parciales

- El threshold se encarga de verificar en el caso del adaline, para checkear si el cambio más grande realizado en los pesos es
relevante aún para el estudio, mientras que en el perceptrón nos permite identificar nuestra zona de indecisión.