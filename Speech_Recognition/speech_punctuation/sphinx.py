import speech_recognition as sr
import re

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_sphinx(audio_data, language="pt-BR")
        return text
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio.")
    except sr.RequestError as e:
        print(f"Erro ao chamar o serviço de reconhecimento de fala: {e}")

def add_punctuation(text):
    # Adiciona pontuação ao texto reconhecido com base em pausas de fala
    punctuation_marks = r'[?.!,;]' # Adicionado ponto e vírgula
    text_with_punctuation = re.sub(f'(?<=[^\s]){punctuation_marks}', r' \g<0>', text)
    return text_with_punctuation

if __name__ == "__main__":
    audio_file_path = "audio.wav"

    transcribed_text = transcribe_audio(audio_file_path)

    if transcribed_text:
        text_with_punctuation = add_punctuation(transcribed_text)

        txt_file_path = audio_file_path.replace(".wav", ".txt")
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text_with_punctuation)
        print(f"Texto convertido com pontuação salvo em: {txt_file_path}")
