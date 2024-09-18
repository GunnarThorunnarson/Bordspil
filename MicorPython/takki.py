from machine import Pin
takki = Pin(14, Pin.IN, Pin.PULL_UP)   	# Segjum að pinninn sé inntakspinni, vír tengdur í GND. 

while True:
    # ef ekki er ýtt á takka
    print(takki.value()) 		# skrifar út 1 í Shell (upphafsstaða)
  
    # ef ýtt er á takka 
    if not takki.value():        # ef ekki 1     
        print(takki.value())     # skrifar út 0 í Shell
    
# ath. value() les mörgum sinnum á meðan haldið er takka inni.
