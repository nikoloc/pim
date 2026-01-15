import pyb

# um1724 book
# micropython pyb docs

# ld2 -> D13
led = pyb.Pin("D13", mode=pyb.Pin.OUT_PP)
button = pyb.Pin("PC13", mode=pyb.Pin.IN)

period = 500
duty_cycle = 0.8

while True:
    on_time = int(duty_cycle * period)
    off_time = int((1 - duty_cycle) * period)

    led.value(True)
    pyb.udelay(on_time)

    led.value(False)
    pyb.udelay(off_time)
