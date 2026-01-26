import pyb


class Button(pyb.Pin):
    def __init__(self, pin):
        super().__init__(pin, mode=pyb.Pin.IN)

        self.last_state = 1

    def was_just_pressed(self):
        state = self.value()

        ret = self.last_state == 1 and state == 0
        self.last_state = state

        return ret


def toggle(pin):
    pin.value(not pin.value())


MODE_OFF = 0
MODE_ON = 1
MODE_BLINK = 2
MODE_BLINK_ALT = 3
MODE_COUNT = 4


mode = MODE_OFF

button = Button("PC13")
leds = [
    pyb.Pin("PB15", mode=pyb.Pin.OUT),
    pyb.Pin("PA11", mode=pyb.Pin.OUT),
    pyb.Pin("D13", mode=pyb.Pin.OUT),
]


def timer_callback(timer):
    if mode == MODE_OFF:
        for led in leds:
            led.value(0)
    elif mode == MODE_ON:
        for led in leds:
            led.value(1)
    elif mode == MODE_BLINK:
        for led in leds:
            toggle(led)
    elif mode == MODE_BLINK_ALT:
        if leds[0].value():
            leds[0].value(0)
            leds[1].value(1)
        elif leds[1].value():
            leds[1].value(0)
            leds[2].value(1)
        else:
            leds[2].value(0)
            leds[0].value(1)


timer = pyb.Timer(4)
timer.init(period=500, callback=timer_callback)

while 1:
    if button.was_just_pressed():
        print("text")
        mode = (mode + 1) % MODE_COUNT
