import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

def adc(levels, maxVoltage, comp):
    for value in range(256):
        time.sleep(0.001)
        signal = num2dac(value)
        voltage = value / levels * maxVoltage
        compValue = GPIO.input(comp)
        if compValue == 1:
            print(value, signal, voltage)
            break
    return voltage

def led(voltage, leds):
    if 1.64 <= voltage <= 1.66:
        return 0
    res = [0,0,0,0,0,0,0,0]
    v = 3.3/8
    for i in range(7, 7 - int(voltage/v),-1):
        res[i] = 1
    GPIO.output(leds, res)
    return 0    

try:
    while True:
        start_time = time.time()
        voltage = adc(levels, maxVoltage, comp)
        led(voltage, leds)
        end_time = time.time()
        print('time:', end_time - start_time)
        GPIO.output(dac, GPIO.LOW)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.cleanup(leds)