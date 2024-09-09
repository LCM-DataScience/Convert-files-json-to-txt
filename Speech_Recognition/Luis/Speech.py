import speech_recognition as sr
from pydub import AudioSegment


def convert_ogg_to_wav(ogg_file):
    # Converte o arquivo OGG para WAV
    sound = AudioSegment.from_ogg(ogg_file)
    wav_file = ogg_file.replace(".ogg", ".wav")
    sound.export(wav_file, format="wav")
    return wav_file


def mp3_to_text(mp3_file):
    # Converte o MP3 para WAV
    ogg_file = mp3_file.replace(".mp3", ".ogg")  # Corrigido para .ogg
    wav_file = convert_ogg_to_wav(ogg_file)  # Corrigido para convert_ogg_to_wav(ogg_file)

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


if __name__ == "__main__":
    mp3_file_path = r"H:\TCD\_Projects\Converter\Speech_Recognition\Luis\oseias.ogg"

    text_result = mp3_to_text(mp3_file_path)

    if text_result:
        txt_file_path = mp3_file_path.replace(".ogg", ".txt")  # Corrigido para .ogg
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text_result)
        print(f"Texto convertido salvo em: {txt_file_path}")
