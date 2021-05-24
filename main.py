from matplotlib.colors import same_color
import matplotlib.pyplot as plt
import numpy as np
import math

sample_count = 44100
x_axis = np.arange(sample_count)
frequency = 10

sine = []

for i in range(sample_count):
    sine.append(math.sin(math.pi*2*(i/sample_count)*frequency*math.sin(math.pi*2*(i/sample_count)*frequency*0.5)))

plt.plot(x_axis, sine)
plt.show()