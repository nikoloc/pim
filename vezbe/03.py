import pyb

led_1 = pyb.Pin("PA11", mode=pyb.Pin.OUT)
led_2 = pyb.Pin("PB15", mode=pyb.Pin.OUT)

button_1 = pyb.Pin("PC9", mode=pyb.Pin.IN)
button_2 = pyb.Pin("PC8", mode=pyb.Pin.IN)

led_1.value(True)
led_2.value(True)

while True:
    led_1.value(button_1.value())
    led_2.value(button_2.value())
