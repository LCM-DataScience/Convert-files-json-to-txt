import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_opus_to_wav(opus_file):
    # Verifica se o arquivo existe
    if not os.path.isfile(opus_file):
        print(f"Arquivo não encontrado: {opus_file}")
        return None
    
    # Converte o arquivo OPUS para WAV
    sound = AudioSegment.from_file(opus_file, format="opus")
    wav_file = opus_file.replace(".opus", ".wav")
    sound.export(wav_file, format="wav")
    return wav_file

def opus_to_text(opus_file):
    # Converte o OPUS para WAV
    wav_file = convert_opus_to_wav(opus_file)
    
    if wav_file is None:
        return None

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
    opus_file_path = r"H:\TCD\_Projects\Speech_Recognition\Victor\PTT-20240725-WA0000.opus"

    # Imprime o caminho do arquivo para depuração
    print(f"Convertendo arquivo: {opus_file_path}")

    # Listar arquivos no diretório
    directory = os.path.dirname(opus_file_path)
    print(f"Arquivos no diretório {directory}:")
    for filename in os.listdir(directory):
        print(filename)

    text_result = opus_to_text(opus_file_path)

    if text_result:
        txt_file_path = opus_file_path.replace(".opus", ".txt")
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text_result)
        print(f"Texto convertido salvo em: {txt_file_path}")
    else:
        print("Nenhum texto foi reconhecido.")
