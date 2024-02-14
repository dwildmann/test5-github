basic.showNumber(0)
basic.pause(100)
basic.showLeds(`
    . . . . .
    . . # . .
    . . # . .
    . . # . .
    . . . . .
    `)
basic.pause(100)
basic.forever(function () {
    for (let Index = 0; Index <= 4; Index++) {
        basic.showIcon(IconNames.Heart)
        basic.pause(100)
        basic.showString("" + (Index))
        basic.pause(100)
    }
})
