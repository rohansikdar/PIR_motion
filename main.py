from machine import Pin

PIR = Pin(28,Pin.IN)
BUZ = Pin(15,Pin.OUT)

while True:
    if PIR.value() == 1:
        BUZ.high()
    
    else:
        BUZ.low()
