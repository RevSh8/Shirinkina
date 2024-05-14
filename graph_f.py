import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

from math import ceil

with open('settings.txt', 'r') as f:
    data = [float(line) for line in f.read().split()]

freq = 1/data[0]

period = 1/freq

step = data[1]

voltage = np.loadtxt('data.txt', dtype=float)

timepoints = np.linspace(0, len(voltage)*period, len(voltage))

ind_max = np.argmax(voltage)

time_charged = timepoints[ind_max]

time_discharged = timepoints[-1] - time_charged

fig, ax = plt.subplots()

ax.plot(timepoints, voltage, 'b', label='V(t)')

ax.scatter(timepoints[::round(freq)//2], voltage[::round(freq)//2], color='b', marker='o', linewidths=1)

plt.xticks(np.arange(0, ceil(len(voltage)*period), 1))

plt.xlim(-len(voltage)*period*0.05, ceil(len(voltage)*period))

plt.ylim(0, 1.1*np.max(voltage))

plt.xlabel('Time, s')

plt.ylabel('Voltage, V')

plt.grid(which='major', color='grey', linewidth=1.5, alpha=0.3)

plt.grid(which='minor', color='grey', linestyle='--', linewidth=1, alpha=0.1)

ax.xaxis.set_minor_locator(ticker.MaxNLocator((ceil(len(voltage)*period)-len(voltage)*period*0.05)*7))

ax.yaxis.set_minor_locator(ticker.MaxNLocator(1.1*np.max(voltage)*11))

plt.legend(loc=1)

plt.title(label='Процесс заряда и разряда конденсатора в RC-цепи', loc='center', wrap=True)

plt.text(0.63*timepoints[-1], 0.8*np.max(voltage), f'Время зарядки = {time_charged:4.1f} с', wrap=True)

plt.text(0.63*timepoints[-1], 0.7*np.max(voltage), f'Время разрядки = {time_discharged:4.1f} с', wrap=True)

plt.savefig("Graph.svg")

plt.show()