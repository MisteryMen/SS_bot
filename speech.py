import speech_recognition as sr
import pyaudio

# Crear un reconocedor
recognizer = sr.Recognizer()

# Capturar el audio desde el micrófono
with sr.Microphone() as source:
    print("Di algo...")
    audio = recognizer.listen(source)

# Reconocer el habla usando Google Web Speech API
try:
    print("Dijiste: " + recognizer.recognize_google(audio, language="es-ES"))
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print("Error al solicitar resultados; {0}".format(e))