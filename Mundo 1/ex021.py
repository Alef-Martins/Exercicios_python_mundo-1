#programa para reproduzir um áudio em MP3
from pygame import mixer
mixer.init() 
mixer.music.load('06. The Temple Of The King.mp3')
mixer.music.play()
import time
time.sleep(360)
#Ctrl+C para interromper