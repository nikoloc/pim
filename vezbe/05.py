import pyb

segment_a = pyb.Pin("PA10", mode=pyb.Pin.OUT)
segment_b = pyb.Pin("PA9", mode=pyb.Pin.OUT)
segment_c = pyb.Pin("PA8", mode=pyb.Pin.OUT)
segment_d = pyb.Pin("PB10", mode=pyb.Pin.OUT)
segment_e = pyb.Pin("PB5", mode=pyb.Pin.OUT)
segment_f = pyb.Pin("PB4", mode=pyb.Pin.OUT)
segment_g = pyb.Pin("PB3", mode=pyb.Pin.OUT)

segments = [
    segment_a,
    segment_b,
    segment_c,
    segment_d,
    segment_e,
    segment_f,
    segment_g,
]

simbols = {"6": {""}}

mux_left = pyb.Pin("PB6", mode=pyb.Pin.OUT)
mux_right = pyb.Pin("PB7", mode=pyb.Pin.OUT)
mux.value(False)

for segment in segments:
    segment.value(False)

while True:
    pass
