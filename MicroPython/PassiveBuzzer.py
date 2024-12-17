from machine import Pin, PWM            # PWM til að vinna með hliðrænt gildi (ekki bara 0 og 1)
import time

# Passive buzzer er með grænt circuit á botninum. 
# Með passiveBuzzer og speaker er hægt að búa til lag (melody) með mismunandi tíðn (0 til 4978).
passiveBuzzer = PWM(Pin(21))          

while True:
    passiveBuzzer.init()          # enable PWM pinna
    passiveBuzzer.duty(900)       # to generate smooth sound waves (0 til 1023)
        
    passiveBuzzer.freq(4000)       # freq er notað til að vinna með tíðni, nótur eru t.d. frá 31 til 4978 sjá neðar.
    time.sleep_ms(500)
        
        
    passiveBuzzer.duty(0)         # skrifar út 0V, slökkva á hljóði


# passiveBuzzer.deinit()        # disable PWM pinna	
        
        
# Hægt er að tengja NPN transistor (nr. 8050) til að fá hærra hljóð. Viðnám (220) til að vernda NPN og diode til að verja pinnann á ESP32.
# https://techexplorations.com/arduino/how-to-use-a-buzzer-the-correct-way/
