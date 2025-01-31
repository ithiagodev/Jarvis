import pyttsx3

# Inicializando o TTS
engine = pyttsx3.init()
engine.setProperty("rate", 250) # Ajusta a velocidade da fala
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 = Masculina, 1 = Feminina

def falar(texto):
    engine.say(texto)
    engine.runAndWait()
