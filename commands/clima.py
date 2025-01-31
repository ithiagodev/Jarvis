from core.fala import falar
import requests

# Configurações da API
API_KEY = "INFORME A KEY DA API AQUI"

# link da API para obter a API_KEY (OpenWeatherMap): https://openweathermap.org/

CIDADE = "COLOQUE SUA CIDADE AQUI"
LINK = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

def previsao(comando):
    try:
        # Faz a requisição para a API do OpenWeatherMap
        resposta = requests.get(LINK)
        resposta.raise_for_status()
        dados = resposta.json()
        
        # Extrai a descrição do clima e a temperatura
        descricao = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        
        # Monta e informa a previsão do tempo
        mensagem = f"A previsão do tempo para {CIDADE} é de {temperatura} graus com {descricao}, senhor!"
        falar(mensagem)
        print(mensagem)

        # Informa o erro quando há um problema na conexão com a API
    except requests.exceptions.RequestException as e:
        mensagem = f"Erro na requisição: {e}"
        falar("Desculpe, não consegui obter a previsão do tempo, senhor.")
        print(mensagem)
        
        # Informa o erro quando os dados esperados não são encontrados na resposta da API
    except KeyError:
        mensagem = "Dados não encontrados na resposta da API."
        falar("Desculpe, não consegui encontrar informações para a cidade especificada, senhor.")
        print(mensagem)

def extrair_dados():
    # Obtém os dados da API
    resposta = requests.get(LINK).json()
    
    # Extrai a temperatura e a descrição do clima
    temperatura = resposta['main']['temp']
    descricao = resposta['weather'][0]['description']
    
    return temperatura, CIDADE, descricao
