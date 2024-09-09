import json

# Função para carregar e ler o arquivo JSON
def carregar_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

# Função para formatar os dados do JSON para texto
def formatar_dados(data):
    texto_formatado = ''
    
    # Itera pelos itens no JSON
    for item in data:
        if isinstance(item, dict):  # Verifica se o item é um dicionário
            for chave, valor in item.items():
                texto_formatado += f'{chave}: '
                
                if isinstance(valor, dict):  # Se o valor for outro dicionário
                    texto_formatado += '\n' + formatar_dados([valor])  # Chama recursivamente
                
                elif isinstance(valor, list):  # Se o valor for uma lista
                    texto_formatado += '\n'
                    for sub_item in valor:
                        texto_formatado += formatar_dados([sub_item])  # Chama recursivamente
                
                else:  # Se o valor for um dado simples
                    texto_formatado += f'{valor}\n'
                    
        elif isinstance(item, list):  # Se o item for uma lista
            for sub_item in item:
                texto_formatado += formatar_dados([sub_item])  # Chama recursivamente
                
        else:  # Para valores simples
            texto_formatado += f'{item}\n'
    
    texto_formatado += '\n'  # Adiciona uma nova linha entre itens
    return texto_formatado

# Função para salvar o texto formatado em um arquivo .txt
def salvar_para_txt(caminho_arquivo, texto_formatado):
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(texto_formatado)

# Caminho dos arquivos
caminho_json = r'H:\TCD\_Projects\Json_Txt\D78S_conversations_290824.json'  # Substitua pelo caminho do seu arquivo JSON
caminho_txt = r'H:\TCD\_Projects\Json_Txt\290824.txt'  # Substitua pelo nome desejado para o arquivo TXT

# Processo de conversão
try:
    dados_json = carregar_json(caminho_json)
    texto_formatado = formatar_dados(dados_json)
    salvar_para_txt(caminho_txt, texto_formatado)
    print(f"Arquivo '{caminho_txt}' gerado com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
