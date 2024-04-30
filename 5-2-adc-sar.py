import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

def adc(levels, maxVoltage, comp):
    res = [0, 0, 0, 0, 0, 0, 0, 0]
    for value in range(8):
        res[value] = 1
        GPIO.output(dac, res)
        time.sleep(0.002)
        compValue = GPIO.input(comp)
        if compValue != 0:
            res[value] = 0
    voltage = int(''.join([str(i) for i in res]), base=2) / levels * maxVoltage
    signal = num2dac(int(''.join([str(i) for i in res]), base=2))

    return voltage

f = 1
data = []
try:
    start_time = time.time()
    GPIO.output(troyka, 1)
    while f:
        v = adc(levels, maxVoltage, comp)
        data.append(v)
        print(v)
        if v >=3.13:
            f = 0
    GPIO.output(troyka, 0)
    while v >=maxVoltage*0.1:
        v = adc(levels, maxVoltage, comp)
        data.append(v)
        print(v)
    end_time = time.time()

finally:
    t = end_time - start_time
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    new_file = open("data.txt", "w+")
    for i in data:
        new_file.write(f"{i}\n")
    new_file.close()
    settings  = open("settings.txt", 'w+')
    settings.write(f"{t/len(data)} {3.3/255}")
    settings.close()
    print(f"Freq = {t/len(data)}, Quant=3.3/255")
    