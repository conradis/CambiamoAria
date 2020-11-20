let angolo_finestra = 0
input.calibrateCompass()
let angolo_finestra_chiusa = input.compassHeading()
let timer = input.runningTime() / 1000
let chiusa = true
basic.forever(function () {
    angolo_finestra = Math.abs(input.compassHeading() - angolo_finestra_chiusa)
    if (angolo_finestra > 20) {
        basic.showString("A")
        chiusa = false
        timer = input.runningTime() / 1000
    } else {
        basic.showString("C")
        chiusa = true
    }
    if (chiusa == true && input.runningTime() / 1000 - timer > 5) {
        basic.showIcon(IconNames.Square)
        basic.pause(3000)
    }
    basic.pause(100)
})
