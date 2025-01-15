<!--
Punktar:
- 3 dagar (2 dagar of lítið og langir dagar)
- Gera kóðatemplate fyrir spil
- einfalda kóðadæmin enn frekar og fækka.
- skoða tónlist sem virkar með pazzive buzzer, virðist ekki ráða við alla tóna.
- halda lóðun í lágmarki, nota frekar led strip og neopixel hringi.
- of langur tími í að hanna spilið, hafa skýrari mörk og hafa flækustigið í lágmarki.
-->

## Borðspil 
Í þessu verkefni ætlið þið að hanna, forrita og smíða frá grunni rafrænt borðspil. Spilið má einnig innihalda spilastokk, teninga, leikmenn og fleira sem ykkur dettur í hug. Hugið vel að leikjaspilun og reglum. Þegar þið hafið lokið við verkefnið ættuð þið að hafa fullbúið rafrænt borðspil í höndunum sem er tilbúið að fara í verslanir.

Borðspilið þarf að innihalda eftirfarandi íhluti:

- [ ] leds eða NeoPixel hringur
- [ ] takki (arcade)
- [ ] reed switch (segull)
- [ ] hátalari 

> [rafræn borðspil](https://boardgamegeek.com/boardgamecategory/1072/electronic) fyrir hugmyndavinnu.

---

### Hönnun
<details>
<summary>Hönnun - leiðbeiningar</summary>
<br>

1. Notaðu [Inkscape](https://github.com/GunnarThorunnarson/Bordspil/blob/main/Inkscape.md) forrit til að hanna borðspilið (svartur litur er notaður fyrir laserskurð).
1. Notaðu [lok/topp](https://github.com/GunnarThorunnarson/Bordspil/blob/main/bordspil_lok_V24.svg) template fyrir borðspilið.
1. Mál á götum:
   * Led (5 mm): Gat: 5 mm þvermál
   * Arcade takki (stór 100 mm): Gat: 25mm þvermál (eða 94 mm þvermál).   
   * Arcade takki (mið 65 mm): Gat 25 mm þvermál (eða 58mm þvermál).
   * Arcade takki (lítill 28 mm): Gat: 25 mm þvermál
1. Skrifið spilaleiðbeiningar á toppinn.

> [Boardgame templates](https://www.pinterest.com.mx/pin/595741856946792806/)

</details>

---


### Forritun
<details>
<summary>Forritun - kóðadæmi</summary>
<br>

1. [Innbyggt LED (blink)](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/blink.py)
2. [LED pera og brauðbretti](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/led_breadboard.py)
3. [Takki](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/takki.py)
4. [Takki og LED](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/takki_led.py)
5. [Reed switch (segull)](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/reedswitch.py)
6. [Hljóð (Passive Buzzer)](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/PassiveBuzzer.py)  og [nótur og tíðni](https://muted.io/note-frequencies/)
7. [Hljóð og takki](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/Buzzer_takki.py)
8. [Random](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/random.py)
9. [NeoPixel hringur (LED strip)](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/NeoPixel.py)
    
:warning: **Ekki nota pinna; GPIO0, GPIO3, GPIO19, GPIO20, GPIO45, GPIO46.** :warning:

<!--
- [Lag (Passive Buzzer)](https://github.com/GunnarThorunnarson/Bordspil/blob/main/MicroPython/lag.py)
https://github.com/james1236/buzzer_music?tab=readme-ov-file
-->

</details>

---

### Lóðun 
<details>
<summary>Lóðun - leiðbeiningar</summary>
<br>

#### Aðstaða og öryggi

1. Hafa gott loftrými, t.d. opinn gluggi og vifta, ekki anda að þér reyknum.
1. Nota öryggisgleraugu.
1. Hafa undirlag sem þolir hita.
1. Passa snúrur og umgengni í kring.
1. Mundu að slökkva á lóðunartækinu í lok tímans.
1. Muna að þvo vel hendur eftir að hafa lóðað, blýagnir á höndum.
1. Nota rakan svamp til að hreinsa odd í byrjun og í lokin.
1. Hreinsaðu odd í hvert sinn sem þú lóðar.
1. 315 gráður Celsíur fyrir snögga lóðun á punktum, 60/40 tin (60% tin, 40% blý)
1. 370 gráður fyrir holur snögglega, 60/40 tin.
1. Ef of mikill hiti eða of lengi þá hætta á að bræða rásir (e. circuits).
1. Ef of lítill hiti þá færðu kalda lóðningu (e. cold solder joint) sem lítur út einsog dropi.

---

#### Tutorial og sýnidæmi
1. [Soldering, setup](https://www.instructables.com/lesson/Soldering-1/) 
1. [Algeng mistök](https://learn.adafruit.com/adafruit-guide-excellent-soldering/common-problems)
1. [Að lóða og aflóða](https://learn.adafruit.com/collins-lab-soldering) (myndband)
1. [How to solder header pins](https://youtu.be/8Z-2wPWGnqE?t=124) (myndband)

</details>

<!--
## GAMALT - ARDUINO
[Arduino nano](https://www.studiopieters.nl/arduino-nano-pinout/)
### Kóðadæmi:
1. [Blink](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds/blinking-the-led)
1. [Takki](https://docs.arduino.cc/tutorials/generic/digital-input-pullup)
1. [Buzzer](https://www.circuitbasics.com/how-to-use-active-and-passive-buzzers-on-the-arduino/#:~:text=Passive%20buzzers%20need%20a%20square,(pin%2C%20frequency%2C%20duration)%3B) og velja [lög](https://projecthub.arduino.cc/tmekinyan/playing-popular-songs-with-arduino-and-a-buzzer-546f4a)
1. [reed switch](https://lastminuteengineers.com/reed-switch-arduino-tutorial/?utm_content=cmp-true)
1. [Random](https://reference.arduino.cc/reference/en/language/functions/random-numbers/random/)
#### Málfræði 
- breytur, HIGH/LOW, OUTPUT/INPUT, int/long, if/else og == 
- setup(), loop(), pinMode(), digitalWrite(), digitalRead(), analogRead(), delay(), Serial.begin(), Serial.println(), tone(), noTone, random(), randomSeed()
> driver CH340 rekilinn https://sparks.gogo.co.nz/ch340.html
-->

