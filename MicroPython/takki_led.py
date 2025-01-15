# Takki sem kveikir á led. Notum 0 eða 1 fyrir takka
# Tengingar og kóði: https://wokwi.com/projects/409365625870394369

from machine import Pin

led = Pin(4, Pin.OUT)
takki = Pin(2, Pin.IN, Pin.PULL_UP)	 # vír tengdur í GND, upphafsstaða á takka er 1  (ekki ýtt á takka)

while True:
    # ef ýtt er á takka (1 verður 0). 
    if takki.value() == 0:  # ef ýtt er á takka þá er gildið 0 lesið af takka með value() aðferð. 
        led.value(1)        # led on
    else:
        led.value(0)        # led off (ekki ýtt á takka eða takka sleppt) 
        

