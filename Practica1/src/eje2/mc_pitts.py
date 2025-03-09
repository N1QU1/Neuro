import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import classes_neuro as cn

# Neurons creating
sensor = cn.Direct()
alarm_delay = cn.McCullochPitts(2)
alarm = cn.McCullochPitts(2)
cooling_delay = cn.McCullochPitts(2)
cooling = cn.McCullochPitts(2)

# Layer creating
entry_layer = cn.Layer()
alarm_delay_layer = cn.Layer()
alarm_layer = cn.Layer()
cooling_delay_layer = cn.Layer()
cooling_layer = cn.Layer()

# Network creating
system_network = cn.Network()

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