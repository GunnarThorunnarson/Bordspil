# Takki, prentar út 0 í Shell ef ýtt er á takka annars 1
# Tengingar og kóði: https://wokwi.com/projects/409364827730921473
from machine import Pin
takki = Pin(2, Pin.IN, Pin.PULL_UP)   # Segjum að pinninn sé inntakspinni, vír tengdur í GND. 

while True:
 
    print(ekki búið að ýta á takka) 		
    
    if takki.value() == 0:      # ef ýtt er á takka, ekki 1     
        print(takki.value())    # skrifar út 0 í Shell
    
    print("takka sleppt") 		# búið að sleppa takka eða ekki ýtt á takka 
    
# ath. value() les mörgum sinnum á meðan haldið er takka inni.
