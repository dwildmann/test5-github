input.onButtonPressed(Button.A, function () {
    Helligkeit += 45
    if (Helligkeit > 255) {
        Helligkeit = 0
    }
    strip.setBrightness(Helligkeit)
    strip.showColor(Farbe)
    strip.show()
})
input.onButtonPressed(Button.B, function () {
    FarbZaehler += 1
    if (FarbZaehler < FarbListe.length) {
        Farbe = FarbListe[FarbZaehler]
        strip.setBrightness(Helligkeit)
        strip.showColor(Farbe)
        strip.show()
    } else if (FarbZaehler == FarbListe.length) {
        strip.showRainbow(1, 360)
    } else if (FarbZaehler == FarbListe.length + 1) {
        Farbe = neopixel.rgb(120, 50, 30)
        strip.setBrightness(Helligkeit)
        strip.showColor(Farbe)
        strip.show()
    } else {
        Farbe = neopixel.rgb(30, 50, 120)
        strip.setBrightness(Helligkeit)
        strip.showColor(Farbe)
        strip.show()
        FarbZaehler = 0
    }
})
let FarbListe: number[] = []
let Helligkeit = 0
let Farbe = 0
let strip: neopixel.Strip = null
let FarbZaehler = 0
FarbZaehler = 0
strip = neopixel.create(DigitalPin.P0, 12, NeoPixelMode.RGB)
Farbe = neopixel.rgb(255, 255, 255)
strip.showColor(Farbe)
Helligkeit = 102
strip.show()
FarbListe = [
neopixel.rgb(255, 0, 0),
neopixel.rgb(0, 255, 0),
neopixel.rgb(0, 0, 255),
neopixel.rgb(255, 255, 255)
]
basic.forever(function () {
	
})
