import pyb


class Button(pyb.Pin):
    def __init__(self, pin_name):
        super().__init__(pin_name, pyb.Pin.IN, pyb.Pin.PULL_UP)

        self.state = 0

    def was_just_clicked(self):
        current_state = not self.value()

        if current_state and not self.state:
            self.state = current_state
            return True

        self.state = current_state
        return False


class LED(pyb.Pin):
    def __init__(self, pin_name):
        super().__init__(pin_name, pyb.Pin.OUT_PP, pyb.Pin.PULL_UP)

        self.state = 1
        self.value(1)

    def toggle(self):
        self.state = not self.state
        self.value(self.state)


class Display:
    def __init__(self):
        self.left_select = pyb.Pin("PB6", pyb.Pin.OUT_PP)
        self.right_select = pyb.Pin("PC7", pyb.Pin.OUT_PP)

        self.segments = [
            pyb.Pin("PA10", pyb.Pin.OUT_PP),
            pyb.Pin("PA9", pyb.Pin.OUT_PP),
            pyb.Pin("PA8", pyb.Pin.OUT_PP),
            pyb.Pin("PB10", pyb.Pin.OUT_PP),
            pyb.Pin("PB5", pyb.Pin.OUT_PP),
            pyb.Pin("PB4", pyb.Pin.OUT_PP),
            pyb.Pin("PB3", pyb.Pin.OUT_PP),
        ]

        self.DIGITS = [
            [1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1],
        ]

        self.CLEAR = [0 for _ in range(0, 7)]

    def _write(self, values):
        for index, value in enumerate(values):
            self.segments[index].value(not value)

    def write(self, value, leading_zero=True):
        left_digit = value // 10 % 10
        right_digit = value % 10

        left_value = (
            self.CLEAR
            if not leading_zero and left_digit == 0
            else self.DIGITS[left_digit]
        )
        right_value = self.DIGITS[right_digit]

        display.right_select.value(1)
        display.left_select.value(0)
        self._write(left_value)

        pyb.delay(5)

        display.left_select.value(1)
        display.right_select.value(0)
        self._write(right_value)

        pyb.delay(5)


button_inc = Button("PC9")
button_dec = Button("PC8")

button_reset = Button("PC13")

display = Display()
count = 0

while 1:
    if button_inc.was_just_clicked():
        count += 1
    elif button_dec.was_just_clicked():
        count -= 1
    elif button_reset.was_just_clicked():
        count = 0

    display.write(count, False)
