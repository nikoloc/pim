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


led_1 = LED("PA11")
led_2 = LED("PB15")

button_1 = Button("PC9")
button_2 = Button("PC8")

while True:
    if button_1.was_just_clicked():
        led_1.toggle()

    if button_2.was_just_clicked():
        led_2.toggle()
