import pyb

# um1724 book
# micropython pyb docs

# ld2 -> D13
led = pyb.Pin("D13", mode=pyb.Pin.OUT_PP)
button = pyb.Pin("PC13", mode=pyb.Pin.IN)

button_state = 0
led_state = 0
while True:
    led.value(led_state)

    current = not button.value()

    if current and not button_state:
        led_state = not led_state
        button_state = current
