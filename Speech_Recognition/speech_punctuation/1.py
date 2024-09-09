import speech_recognition as sr
from pydub import AudioSegment
import re


def convert_ogg_to_wav(ogg_file):
    # Converte o arquivo OGG para WAV
    sound = AudioSegment.from_ogg(ogg_file)
    wav_file = ogg_file.replace(".ogg", ".wav")
    sound.export(wav_file, format="wav")
    return wav_file


def mp3_to_text(mp3_file):
    # Converte o MP3 para WAV
    ogg_file = mp3_file.replace(".mp3", ".ogg")
    wav_file = convert_ogg_to_wav(ogg_file)

    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language="pt-BR")
            return text
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
        except sr.RequestError as e:
            print(f"Erro ao chamar a Google Web Speech API: {e}")


def add_punctuation(text):
    # Adiciona pontuação ao texto reconhecido
    # Você pode personalizar esse método de acordo com suas necessidades
    # Adiciona um espaço antes de pontuações para garantir que haja espaço entre palavras e pontuações
    text_with_punctuation = re.sub(r'(?<=[^\s])\s*([?.!,])', r' \1', text)
    return text_with_punctuation


if __name__ == "__main__":
    mp3_file_path = "audio.ogg"

    text_result = mp3_to_text(mp3_file_path)

    if text_result:
        text_with_punctuation = add_punctuation(text_result)

        txt_file_path = mp3_file_path.replace(".ogg", ".txt")
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text_with_punctuation)
        print(f"Texto convertido com pontuação salvo em: {txt_file_path}")
