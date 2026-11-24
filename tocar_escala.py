from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

buzzer = TonalBuzzer(18)

escala = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]

try:
    while True:
        for nota in escala:
            buzzer.play(Tone(nota))
            sleep(0.5)
        buzzer.stop()
        sleep(1)
except KeyboardInterrupt:
    buzzer.stop()
finally:
    buzzer.stop()
