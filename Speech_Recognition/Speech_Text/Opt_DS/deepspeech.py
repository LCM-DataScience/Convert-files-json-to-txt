import os
import requests
import wave
import numpy as np
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

    # Carrega o áudio WAV
    with wave.open(wav_file, 'rb') as wf:
        frames = wf.getnframes()
        buffer = wf.readframes(frames)
        audio = np.frombuffer(buffer, np.int16)

    # Faz a requisição para a API de reconhecimento de fala do Google
    url = "https://speech.googleapis.com/v1/speech:recognize"
    api_key = "sua_chave_api_do_google"
    data = {
        "config": {
            "encoding": "LINEAR16",
            "sampleRateHertz": 16000,
            "languageCode": "pt-BR"
        },
        "audio": {
            "content": audio.tobytes().decode('utf-8')
        }
    }
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    response = requests.post(url, json=data, headers=headers, params={"key": api_key})
    result = response.json()

    if "results" in result and result["results"]:
        text = result["results"][0]["alternatives"][0]["transcript"]
        return text
    else:
        return None

if __name__ == "__main__":
    ogg_file_path = r"H:\TCD\_Projects\Speech_Recognition\Victor\Anova_Repet.ogg"

    text_result = ogg_to_text(ogg_file_path)

    if text_result:
        txt_file_path = ogg_file_path.replace(".ogg", ".txt")
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text_result)
        print(f"Texto convertido salvo em: {txt_file_path}")
    else:
        print("Nenhum texto foi reconhecido.")
