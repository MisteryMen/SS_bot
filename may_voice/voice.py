from TTS.api import TTS
from pydub import AudioSegment

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

texto = "Hola, Mi nombre es Aura, soy un bot que te ayudara con la aplicación de la prueba DASS-21"
tts.tts_to_file(text=texto,speaker_wav="1.wav",language="es",file_path="prueba.wav")

sound = AudioSegment.from_wav("prueba.wav")
sound.export("prueba.mp3",format="mp3")