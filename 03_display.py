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

        self.NUMBERS = [
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

    def select_left(self, value):
        self.left_select.value(not value)

    def select_right(self, value):
        self.right_select.value(not value)

    def toggle_left(self):
        self.left_select.value(not self.left_select.value())

    def toggle_right(self):
        self.right_select.value(not self.right_select.value())

    def write(self, values):
        for index, value in enumerate(values):
            self.segments[index].value(not value)


button_1 = Button("PC9")
button_2 = Button("PC8")

display = Display()
count = 0

while 1:
    if button_1.was_just_clicked():
        count += 1
        print(count)

        display.select_right(1)
        display.select_left(0)
        display.write(display.NUMBERS[count % 10])
        # display.write(display.NUMBERS[1])
        pyb.delay(500)

        display.select_right(0)
        display.select_left(1)
        display.write(display.NUMBERS[count // 10 % 10])
        # display.write(display.NUMBERS[2])
        pyb.delay(500)
