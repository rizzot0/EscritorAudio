import whisper

def transcribe_with_whisper(file_path):
    # Cargar el modelo de Whisper
    model = whisper.load_model("base")  # Prueba con "small", "medium", o "large" para mayor precisión

    # Transcribir el audio
    print("Transcribiendo el audio, esto puede tardar un momento...")
    result = model.transcribe(file_path, language="es")  # "es" para español
    return result["text"]

# Ruta del archivo de audio en formato PCM WAV
file_path = "Entrevista_PCM.wav"  # Asegúrate de que el archivo esté en este formato

# Transcribir el audio y guardar el resultado en un archivo de texto
transcripcion = transcribe_with_whisper(file_path)

# Guardar la transcripción en un archivo de texto
with open("transcripcion.txt", "w", encoding="utf-8") as file:
    file.write(transcripcion)

print("Transcripción completa guardada en 'transcripcion.txt'")
print("Transcripción: ")
print(transcripcion)
