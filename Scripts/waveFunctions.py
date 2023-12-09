#Длина: 140 см
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)



graphy=[]
timetemp=0
graphx=[]
try:
    while True:
        dac=[8,11,7,1,0,5,12,6]
        leds=[2,3,4,17,27,22,10,9]
        bits = len(dac)
        levels = 2**bits
        maxVoltage = 3.3
        comp=14
        troyka=13
        gpio.setup(21, gpio.IN)

        gpio.setup(dac, gpio.OUT, initial=gpio.LOW)
        gpio.setup(leds, gpio.OUT, initial=gpio.LOW)
        gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
        gpio.setup(comp, gpio.IN)

        def d2b(value):
            return [int(i) for i in bin(value)[2:].zfill(8)]
        def adc(value):
            signal = d2b(value)
            gpio.output(dac, signal)
            return signal

        if gpio.input(21)==1:
            while True:
                
                pust=[0,0,0,0,0,0,0,0]
                for i in range(8):
                    pust[i]=1
                    gpio.output(dac, pust)
                    time.sleep(0.05)
                    timetemp+=time.time()

                    comparatorValue = gpio.input(comp)
                    if comparatorValue == 1:
                        pust[i]=0
                uotn=0
                for i in range(8):
                    if pust[i]==1:
                        uotn+=2**(7-i)
                u = uotn / 256 * 3.3
                graphy.append(u)
                timetempstr=str(timetemp)[:5]
                graphx.append(timetempstr)
                print(u,pust)
                print(gpio.input(21))
                for i in range(8):
                    if uotn>256/8*i:
                        gpio.output(leds[i],1)
                    else:
                        gpio.output(leds[i],0)

except KeyboardInterrupt:
    print('\nThe program was stopped by keyboard')
else:
    print("No exceptions")
finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup(dac)
    gpio.output(leds, gpio.LOW)
    gpio.cleanup(leds)
    print('GPIO cleanup completed')
    d = open('datau.txt', 'w')
    for i in graphy:
        d.write(str(i)+"\n")
    d.close()
    d = open('datatime.txt', 'w')
    for i in graphx:
        d.write(str(i)+"\n")
    d.close()
    print(graphx)