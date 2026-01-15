import pyb

led_1 = pyb.Pin("PA11", mode=pyb.Pin.OUT)
led_2 = pyb.Pin("PB15", mode=pyb.Pin.OUT)

pot_1 = pyb.Pin("PA0", mode=pyb.Pin.ANALOG)
pot_2 = pyb.Pin("PA1", mode=pyb.Pin.ANALOG)

adc_1 = pyb.ADC(pot_1)
adc_2 = pyb.ADC(pot_2)

while True:
    print(f"adc_1 {adc_1.read()}")
    print(f"adc_2 {adc_2.read()}")
    pyb.delay(500)
