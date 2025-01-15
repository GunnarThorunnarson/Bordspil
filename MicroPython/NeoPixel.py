from machine import Pin
import neopixel
import time

# LEDPixel tenging ( IN )
# S digital pinni
# V 5V
# G GND

pin = Pin(48, Pin.OUT)
np = neopixel.NeoPixel(pin, 8)	# 8 x RGB Leds

# breytur
brightness = 255                # birtustig frá 0 - 255
red   =  [ brightness, 0, 0]    # red
green =  [ 0, brightness, 0]    # green  
blue  =  [ 0, 0, brightness]    # blue
off   =  [ 0, 0, 0]             # ekkert ljós

while True:
    # stjórnum öllum 8 leds í einu með að nota fill
    neo.fill([0, 0, 0])
    
    # led 1  
    np[0] = red		        # eða [255, 0, 0] 
    np.write()              # kveikjum á led 1
    time.sleep_ms(500)      # hinkrum í hálfa sek. þar til við gerum eitthvað annað.

    # led 2
    np[1] = green	        # eða [0, 255, 0] 
    np.write()
    time.sleep_ms(500)

    # led 3
    np[2] = blue	        # eða [0, 0, 255] 
    np.write()
    time.sleep_ms(500)
    
    np[0] = off             # eða [0, 0, 0] 
    np[1] = off
    np[2] = off
    np.write()	

    time.sleep_ms(1000) 
    
