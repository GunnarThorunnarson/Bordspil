from machine import Pin, PWM            # PWM til að vinna með hliðrænt gildi (ekki bara 0 og 1)
import time

# Passive buzzer er með grænt circuit á botninum. 
passiveBuzzer = PWM(Pin(21))          

while True:
    passiveBuzzer.init()          # enable PWM pinna
    passiveBuzzer.duty(900)       # to generate smooth sound waves (0 til 1023)   
    passiveBuzzer.freq(4000)       # freq er notað til að vinna með tíðni, nótur eru t.d. frá 31 til 4978 sjá neðar.
    time.sleep_ms(500)   
    passiveBuzzer.duty(0)         # skrifar út 0V, slökkva á hljóði
