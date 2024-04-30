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
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

def adc(levels, maxVoltage, comp):
    for value in range(256):
        time.sleep(0.01)
        signal = num2dac(value)
        voltage = value / levels * maxVoltage
        compValue = GPIO.input(comp)
        if compValue == 1:
            print(value, signal, voltage)
            break
    return 0

try:
    while True:
        start_time = time.time()
        adc(levels, maxVoltage, comp)
        end_time = time.time()
        print('time:', end_time - start_time)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)