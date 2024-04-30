import matplotlib.pyplot as plt
import numpy as np

file_d = open("data.txt", 'r+')
data = []
while True:
    line = file_d.readline()
    if not line:
        break
    data.append(float(line))

settings = open("settings.txt", 'r+')
sett = settings.readline().split()
t = float(sett[0])

tim = [i*t for i in range(len(data))]

fig, ax = plt.subplots()
ax.plot(tim, data)
ax.set_xlabel('time, s')
ax.set_ylabel('Voltage, V')
ax.set_title(f"Freq = {t}, Quant = {sett[1]}")
plt.show()
file_d.close()
settings.close()