from machine import Pin, PWM 
import time
import random

led = Pin(4, Pin.OUT)
takki = Pin(2, Pin.IN, Pin.PULL_UP)	 
passiveBuzzer = PWM(Pin(21)) # hljóð

passiveBuzzer.init()         
passiveBuzzer.duty(900) # to generate smooth sound waves (0 til 1023)   

# intro lag
# freq er notað til að vinna með tíðni, nótur eru t.d. frá 31 til 4978.
passiveBuzzer.freq(4000)       
time.sleep_ms(500)   

# bæta við meira hér ...


passiveBuzzer.duty(0) # slökkva á hljóði

while True:
    random_time = random.randint(2000, 6000)   # millisekúndur
    time.sleep_ms(random_time)
    led.value(1) # led on
    
    # ef ýtt er á takka  
    if takki.value() == 0:
        # hljóð
        passiveBuzzer.freq(4000)       
        time.sleep_ms(500)   
    
    time.sleep_ms(2000) #  leyfa ljósi að loga í 2 sek
    led.value(0)
        

