def on_button_pressed_a():
    global Helligkeit
    Helligkeit += 45
    if Helligkeit > 255:
        Helligkeit = 0
    strip.set_brightness(Helligkeit)
    strip.show_color(Farbe)
    strip.show()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global FarbZaehler, Farbe
    FarbZaehler += 1
    if FarbZaehler < len(FarbListe):
        Farbe = FarbListe[FarbZaehler]
        strip.set_brightness(Helligkeit)
        strip.show_color(Farbe)
        strip.show()
    elif FarbZaehler == len(FarbListe):
        strip.show_rainbow(1, 360)
    elif FarbZaehler == len(FarbListe) + 1:
        Farbe = neopixel.rgb(120, 50, 30)
        strip.set_brightness(Helligkeit)
        strip.show_color(Farbe)
        strip.show()
    else:
        Farbe = neopixel.rgb(30, 50, 120)
        strip.set_brightness(Helligkeit)
        strip.show_color(Farbe)
        strip.show()
        FarbZaehler = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

FarbListe: List[number] = []
Helligkeit = 0
Farbe = 0
strip: neopixel.Strip = None
FarbZaehler = 0
FarbZaehler = 0
strip = neopixel.create(DigitalPin.P0, 12, NeoPixelMode.RGB)
Farbe = neopixel.rgb(255, 255, 255)
strip.show_color(Farbe)
Helligkeit = 102
strip.show()
FarbListe = [neopixel.rgb(255, 0, 0),
    neopixel.rgb(0, 255, 0),
    neopixel.rgb(0, 0, 255),
    neopixel.rgb(255, 255, 255)]

def on_forever():
    pass
basic.forever(on_forever)
