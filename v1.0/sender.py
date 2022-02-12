from machine import Pin, UART, ADC
import time, _thread

# set GPIO for ADC
t1 = ADC(26)

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

# set the delay on every step with stepper (ms)
# those number shouldn't be set too small
s_delay_min = 5
s_delay_max = 10

# set the unmove range for stepper
uns = 5000

max_min = s_delay_max-s_delay_min
uns_max = 32768+uns
uns_min = 32768-uns

# to count the delay and direction
def s_delay(adc_read):
    global direction
    global delay
    if adc_read in range(uns_min, uns_max):
        direction = 0
        delay = 0
    else:
        if adc_read < uns_min:
            delay = round(adc_read/uns_min*max_min+s_delay_min)
            direction = -1
        else:
            delay = round((uns_max-adc_read)/uns_min*max_min+s_delay_max)
            direction = 1

# count then send delay and direction
while True:
    _thread.start_new_thread(s_delay, (t1.read_u16(),))
    time.sleep_ms(30)
    
    send = "("+str(delay)+","+str(direction)+")"
    uart.write(send)
    time.sleep_ms(20)