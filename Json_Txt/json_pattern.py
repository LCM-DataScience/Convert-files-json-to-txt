import json

# Carregar o arquivo JSON
with open(r'H:\TCD\_Projects\Json_Txt\D78S_conversations_290824.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Função para formatar os dados
def formatar_dados(data):
    if isinstance(data, (str, int, float, bool, type(None))):
        # Se os dados forem um valor simples, apenas retornar o valor
        return str(data)
    # Caso seja uma lista ou dicionário
    else:
        texto_formatado = ''
        for item in data:
            if 'title' in item and 'mapping' in item:
                texto_formatado += item['title'] + ':\n\n'
                for chave, valor in item['mapping'].items():
                    if valor['message'] and valor['message']['content'] and valor['message']['content']['parts']:
                        texto_formatado += valor['message']['content']['parts'][0] + '\n\n'
        return texto_formatado

# Escrever os dados formatados em um arquivo .txt
with open('out.txt', 'w', encoding='utf-8') as f:
    texto_formatado = formatar_dados(data)
    f.write(texto_formatado)
