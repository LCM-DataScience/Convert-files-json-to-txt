import speech_recognition as sr
from pydub import AudioSegment

def convert_ogg_to_wav(ogg_file):
    # Converte o arquivo OGG para WAV
    sound = AudioSegment.from_ogg(ogg_file)
    wav_file = ogg_file.replace(".ogg", ".wav")
    sound.export(wav_file, format="wav")
    return wav_file

def ogg_to_text(ogg_file):
    # Converte o OGG para WAV
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

if __name__ == "__main__":
    ogg_file_path = r"H:\TCD\_Projects\Speech_Recognition\Victor\AnaliseZeroNans.ogg"

    text_result = ogg_to_text(ogg_file_path)

    if text_result:
        txt_file_path = ogg_file_path.replace(".ogg", ".txt")
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text_result)
        print(f"Texto convertido salvo em: {txt_file_path}")
    else:
        print("Nenhum texto foi reconhecido.")


