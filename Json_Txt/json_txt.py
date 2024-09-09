import json

# Carregar o arquivo JSON
with open(r'h:\TCD\_Projects\Json_Txt\D78S_conversations_290824.json', 'r') as f:
    data = json.load(f)



# Função para formatar os dados
def formatar_dados(data):
    texto_formatado = ''
    for item in data:
        if 'title' in item and 'mapping' in item:
            texto_formatado += item['title'] + ':\n\n'
            for chave, valor in item['mapping'].items():
                if valor['message'] and valor['message']['content'] and valor['message']['content']['parts']:
                    texto_formatado += valor['message']['content']['parts'][0] + '\n\n'
    return texto_formatado


# Dados formatados em arquivo .txt
with open('nome_arquivo_txt.txt', 'w', encoding='utf-8') as f:
    texto_formatado = formatar_dados(data)
    f.write(texto_formatado)
