from machine import Pin, UART
import time, _thread

# set GPIO for stepper
s1_1 = Pin(6,Pin.OUT)
s1_2 = Pin(7,Pin.OUT)
s1_3 = Pin(8,Pin.OUT)
s1_4 = Pin(9,Pin.OUT)

# set GPIO for led
led = Pin(25,Pin.OUT)
led.high() # if led light, it is not in working

# set GPIO for E28
uart = UART(0, 9600, bits=8, tx=Pin(0), rx=Pin(1), parity=None, stop=1)
m0 = Pin(2,Pin.OUT)
m1 = Pin(3,Pin.OUT)
m2 = Pin(4,Pin.OUT)
aux = Pin(5,Pin.IN,Pin.PULL_UP)

# wait starting of E28
def E28_start():
    m0.value(0)
    m1.value(0)
    m2.value(1)
    while aux.value() == 0:
        time.sleep_ms(300)
    led.low() # it is  able to work

# led flashing
def led_flash(c, t):
    for x in range(c):
        led.high()
        time.sleep_ms(t)
        led.low()
        time.sleep_ms(t)

# config E28
E28_start()
m0.value(1)
m1.value(1)
m2.value(1)
led.high() # it means that E28 is just configing
time.sleep_ms(500)
uart.write(b"\xc0\x57\x57\x13\x5d\x04") # set the original config to E28
time.sleep_ms(500)
uart.read() # clean the message from uart
E28_start() # now it can work

# control of stepper
def step():
    while True:
        d=direction
        dd=delay
        if d == 0:
            s1_1(0)
            s1_2(0)
            s1_3(0)
            s1_4(0)
            time.sleep_ms(100)
        elif d == 1:
        
            s1_1(0)
            s1_2(0)
            s1_3(0)
            s1_4(1)
            time.sleep_ms(dd)
            
            s1_1(0)
            s1_2(0)
            s1_3(1)
            s1_4(1)
            time.sleep_ms(dd)
            
            s1_1(0)
            s1_2(0)
            s1_3(1)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(0)
            s1_2(1)
            s1_3(1)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(0)
            s1_2(1)
            s1_3(0)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(1)
            s1_2(1)
            s1_3(0)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(1)
            s1_2(0)
            s1_3(0)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(1)
            s1_2(0)
            s1_3(0)
            s1_4(1)
            time.sleep_ms(dd)
        else:
            s1_1(1)
            s1_2(0)
            s1_3(0)
            s1_4(1)
            time.sleep_ms(dd)
            
            s1_1(1)
            s1_2(0)
            s1_3(0)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(1)
            s1_2(1)
            s1_3(0)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(0)
            s1_2(1)
            s1_3(0)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(0)
            s1_2(1)
            s1_3(1)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(0)
            s1_2(0)
            s1_3(1)
            s1_4(0)
            time.sleep_ms(dd)
            
            s1_1(0)
            s1_2(0)
            s1_3(1)
            s1_4(1)
            time.sleep_ms(dd)
            
            s1_1(0)
            s1_2(0)
            s1_3(0)
            s1_4(1)
            time.sleep_ms(dd)

# set an original number for delay and direction
delay = 0
direction = 0

# start the control of stepper
_thread.start_new_thread(step,())

# this is a test
#uart.write('(5,1)')

while True:
    if uart.any()>=1:
        time.sleep_ms(30)
        receive = str(uart.read())
        e = receive.rfind(")")
        s = receive.rfind(",", 0, e)
        direction = int(receive[(s+1):e])
        e = receive.rfind("(", 0, s)
        delay = int(receive[(e+1):s])
    else:
        time.sleep_ms(30)
