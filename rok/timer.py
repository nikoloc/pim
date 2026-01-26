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


MODE_PAUSED = 0
MODE_RUNNING = 1
MODE_ENDED = 2

mode = MODE_PAUSED
count = 0


def timer_callback(timer):
    global mode, count
    if mode == MODE_PAUSED or mode == MODE_ENDED:
        return

    count -= 1
    print(count)

    if count <= 0:
        mode = MODE_ENDED
        print("mode: ended")


dec_button = Button("PC8")
inc_button = Button("PC9")

user_button = Button("PC13")

led_1 = pyb.Pin("PA11", mode=pyb.Pin.OUT)
led_2 = pyb.Pin("PB15", mode=pyb.Pin.OUT)

timer = pyb.Timer(4)
timer.init(period=1000, callback=timer_callback)

while 1:
    was_inc_pressed = inc_button.was_just_pressed()
    was_dec_pressed = dec_button.was_just_pressed()
    was_user_pressed = user_button.was_just_pressed()

    if mode == MODE_PAUSED:
        led_1.value(0)
        led_2.value(0)

        if was_inc_pressed:
            count += 1
            print(count)

        if was_dec_pressed:
            count -= 1
            print(count)

        if was_user_pressed:
            mode = MODE_RUNNING
            print("mode: running")
    elif mode == MODE_RUNNING:
        led_1.value(1)
        led_2.value(0)

        if was_user_pressed:
            mode = MODE_PAUSED
            print("mode: paused")
    else:
        led_1.value(0)
        led_2.value(1)

        if was_user_pressed:
            mode = MODE_PAUSED
            print("mode: paused")
            count = 10
