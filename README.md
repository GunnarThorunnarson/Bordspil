## Borðspil 
Í þessu verkefni ætlið þið að hanna og smíða frá grunni rafrænt borðspil með notkun Arduino og íhlutum. Spilið má einnig innihalda spilastokk, teninga, leikmenn og fleira sem ykkur dettur í hug. Hugið vel að leikjaspilun og reglum. Þegar þið hafið lokið við verkefnið ættuð þið að hafa fullbúið rafrænt borðspil í höndunum sem er tilbúið að fara í verslanir, [sýnidæmi](https://github.com/Chicken405/Skyrsla?tab=readme-ov-file).

[Borðspilið](https://boardgamegeek.com/boardgamecategory/1072/electronic) þarf að innihalda eftirfarandi íhluti (einn eða fleiri):

- [ ] Leds
- [ ] arcade takka
- [ ] buzzer/hátalara
- [ ] [reed switch](https://lastminuteengineers.com/reed-switch-arduino-tutorial/)
- [ ] on/off takki og batterí.
      
<!--
- [Pyramids secret](https://projecthub.arduino.cc/marcelomaximiano/fac9edcd-e76f-40c8-a4a4-c867072599c4)
- [Would you rather](https://www.instructables.com/How-To-Make-A-Board-Game-Using-Arduino/)
-->

---

### Hönnun með Inkscape
1. Hannið og útfærið [Boardgame template](https://www.pinterest.com.mx/pin/595741856946792806/) útfrá leikjahönnun.
1. [Grunnur fyrir borðspil](https://github.com/VESM1VS/AFANGI/blob/main/Myndir/bordspil_lok_V24.svg)
1. Mál á götum:
   * Led (5 mm): Gat: 5 mm þvermál
   * Arcade takki (stór 100 mm): Gat: 94 mm þvermál   
   * Arcade takki (mið 65 mm): Gat 25 mm þvermál eða 58mm þvermál.
   * Arcade takki (lítill 28 mm): Gat: 25 mm þvermál
1. Skrifið spilaleiðbeiningar á toppinn.

---

[Arduino nano](https://www.studiopieters.nl/arduino-nano-pinout/)

### Kóðadæmi:
1. [Blink](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds/blinking-the-led)
1. [Takki](https://docs.arduino.cc/tutorials/generic/digital-input-pullup)
1. [Buzzer](https://www.circuitbasics.com/how-to-use-active-and-passive-buzzers-on-the-arduino/#:~:text=Passive%20buzzers%20need%20a%20square,(pin%2C%20frequency%2C%20duration)%3B)
1. [reed switch](https://lastminuteengineers.com/reed-switch-arduino-tutorial/?utm_content=cmp-true)
1. [Random](https://reference.arduino.cc/reference/en/language/functions/random-numbers/random/)


#### Málfræði 
- breytur, HIGH/LOW, OUTPUT/INPUT, int/long, if/else og == 
- setup(), loop(), pinMode(), digitalWrite(), digitalRead(), analogRead(), delay(), Serial.begin(), Serial.println(), tone(), noTone, random(), randomSeed()


> driver CH340 rekilinn https://sparks.gogo.co.nz/ch340.html

<!--
Gamalt
- [touchpad úr álpappír](https://medium.com/@paramaggarwal/a-touchpad-using-plastic-and-aluminum-foil-88042f2346)
- How to Make a Board Game Circuit Tile! https://www.youtube.com/watch?v=HM61WVwi6Mg
- https://www.youtube.com/watch?v=5_JgvaB3esg&ab_channel=QVisible
- [Þrýstiplata úr álpappír](https://www.instructables.com/Use-a-DIY-Pressure-Plate-Switch-to-Automate-Your-H/)
- [Boardgame geek](https://boardgamegeek.com/boardgamecategory/1072/electronic)
- [retro electronic board games](https://www.oobject.com/category/retro-electronic-board-games/)
- [Hackster boardgames](https://www.hackster.io/search?q=board%20games&i=projects)
- [DIY board games to handheld video game consoles](https://www.hackster.io/news/take-a-look-at-some-of-the-best-diy-gaming-projects-from-around-the-community-4596332d1c72)
- [Pyramids secret](https://projecthub.arduino.cc/marcelomaximiano/fac9edcd-e76f-40c8-a4a4-c867072599c4)
- [Would you rather](https://www.instructables.com/How-To-Make-A-Board-Game-Using-Arduino/)
- Match;  [1](https://www.youtube.com/watch?v=z8wadyaIsy0), [2](https://www.youtube.com/watch?v=OwhoSbvQ1yc&ab_channel=Kutuhal-SundayScienceSchool)
- [Operation](https://youtu.be/4RF9nLUDt0Q?t=41)
- [Probability pathways](https://makecode.adafruit.com/courses/maker/projects/board-games)
-->

<!--
Linkar
- random.py  nota random fyrir tengi https://github.com/VESM1VS/AFANGI/blob/main/python/Random.py
- passive buzzer lög https://github.com/VESM1VS/Kennarasvaedi/blob/master/Boardgame/PassiveBuzzerMario.py
- passive buzzer tónar https://github.com/VESM1VS/Kennarasvaedi/blob/master/Boardgame/PassiveBuzzer.py
-->
