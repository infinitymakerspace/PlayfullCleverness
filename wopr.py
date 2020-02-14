import time
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
print('GREETINGS PROFESSOR FALKEN!')
time.sleep(2)
speak.Speak("GREETINGS PROFESSOR FALKEN")
time.sleep(2)
print('WOULD YOU LIKE TO PLAY A GAME?')
time.sleep(2)
speak.Speak("WOULD YOU LIKE TO PLAY A GAME")