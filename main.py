def on_button_pressed_a():
    global Helligkeit
    Helligkeit += 45
    if Helligkeit > 255:
        Helligkeit = 0
    strip.set_brightness(Helligkeit)
    strip.show_color(Farbe)
    strip.show()
input.on_button_pressed(Button.A, on_button_pressed_a)

def wechsel_regenbogen():
    while True:
        if input.button_is_pressed(Button.B):
            return
        for Index in range(256):
            strip.show_rainbow(1, 360)
            strip.set_brightness(Index)
            strip.show()
            basic.pause(20)
        for Index2 in range(256):
            strip.show_rainbow(1, 360)
            strip.set_brightness(255 - Index2)
            strip.show()
            basic.pause(20)

def on_button_pressed_ab():
    global Eingeschaltet
    if Eingeschaltet == True:
        strip.set_brightness(0)
        strip.show_color(Farbe)
        strip.show()
    else:
        strip.set_brightness(Helligkeit)
        strip.show_color(Farbe)
        strip.show()
    Eingeschaltet = not (Eingeschaltet)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

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
        wechsel_regenbogen()
    else:
        wechsel_farbig()
        FarbZaehler = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def wechsel_farbig():
    global st_rot, st_gruen, st_blau, st_delta_rot, st_delta_gruen, st_delta_blau, Farbe
    st_rot = 0
    st_gruen = 127
    st_blau = 255
    st_delta_rot = 2
    st_delta_gruen = 2
    st_delta_blau = 2
    while True:
        if input.button_is_pressed(Button.B):
            return
        Farbe = neopixel.rgb(st_rot, st_gruen, st_blau)
        strip.show_color(Farbe)
        strip.set_brightness(Helligkeit)
        strip.show()
        basic.pause(50)
        st_rot += st_delta_rot
        st_gruen += st_delta_gruen
        st_blau += st_delta_blau
        if st_rot > 255:
            st_rot = 255
            st_delta_rot = st_delta_rot * -1
        if st_rot < 0:
            st_rot = 0
            st_delta_rot = st_delta_rot * -1
        if st_gruen > 255:
            st_gruen = 255
            st_delta_gruen = st_delta_gruen * -1
        if st_gruen < 0:
            st_gruen = 0
            st_delta_gruen = st_delta_gruen * -1
        if st_blau > 255:
            st_blau = 255
            st_delta_blau = st_delta_blau * -1
        if st_blau < 0:
            st_blau = 0
            st_delta_blau = st_delta_blau * -1
st_delta_blau = 0
st_delta_gruen = 0
st_delta_rot = 0
st_blau = 0
st_gruen = 0
st_rot = 0
FarbListe: List[number] = []
Eingeschaltet = False
Helligkeit = 0
Farbe = 0
FarbZaehler = 0
strip: neopixel.Strip = None
FarbZaehler = 0
strip = neopixel.create(DigitalPin.P0, 12, NeoPixelMode.RGB)
Farbe = neopixel.rgb(255, 200, 25)
strip.show_color(Farbe)
Helligkeit = 102
Eingeschaltet = True
strip.show()
FarbListe = [neopixel.rgb(255, 0, 0),
    neopixel.rgb(0, 255, 0),
    neopixel.rgb(0, 0, 255),
    neopixel.rgb(255, 200, 25)]