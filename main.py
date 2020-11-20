angolo_finestra = 0
input.calibrate_compass()
angolo_finestra_chiusa = input.compass_heading()
timer = input.running_time() / 1000
chiusa = True

def on_forever():
    global angolo_finestra
    angolo_finestra = abs(input.compass_heading() - angolo_finestra_chiusa)
    if angolo_finestra > 20:
        basic.show_string("A")
        chiusa = False
        timer = input.running_time() / 1000
    else:
        basic.show_string("C")
        chiusa = True
    if chiusa == True and input.running_time() / 1000 - timer > 5:
        basic.show_icon(IconNames.SQUARE)
        basic.pause(3000)
    basic.pause(500)
basic.forever(on_forever)
