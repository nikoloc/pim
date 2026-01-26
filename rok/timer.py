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


class Display:
    def __init__(self):
        self.sel_left = pyb.Pin("PB6", mode=pyb.Pin.OUT)
        self.sel_right = pyb.Pin("PC7", mode=pyb.Pin.OUT)

        self.segments = [
            pyb.Pin("PA10", mode=pyb.Pin.OUT),
            pyb.Pin("PA9", mode=pyb.Pin.OUT),
            pyb.Pin("PA8", mode=pyb.Pin.OUT),
            pyb.Pin("PB10", mode=pyb.Pin.OUT),
            pyb.Pin("PB5", mode=pyb.Pin.OUT),
            pyb.Pin("PB4", mode=pyb.Pin.OUT),
            pyb.Pin("PB3", mode=pyb.Pin.OUT),
        ]

        self.NUMBERS = [
            [0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [1, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
        ]

    def _write(self, states):
        for index, state in enumerate(states):
            # [1, 0, 0, 0, 1, 0, 1]
            self.segments[index].value(state)

    def write(self, number):
        first_digit = int(number / 10) % 10
        second_digit = number % 10

        self.sel_right.value(1)
        self.sel_left.value(0)

        self._write(self.NUMBERS[first_digit])
        pyb.delay(10)

        self.sel_right.value(0)
        self.sel_left.value(1)

        self._write(self.NUMBERS[second_digit])
        pyb.delay(10)


MODE_PAUSED = 0
MODE_RUNNING = 1
MODE_ENDED = 2

mode = MODE_PAUSED
count = 10


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

display = Display()

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

    display.write(count)
