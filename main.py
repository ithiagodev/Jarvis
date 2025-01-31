from core import fala
from core import reconhecimento
from commands import saudacao, hora, data, clima, abra, calculadora, youtube, pesquisa

def main():
    saudacao.bem_vindo()

    # Loop principal
    while True:

        # Ouve o comando do usuário
        comando = reconhecimento.ouvir_audio()

        if comando is None:
            continue

        # Função para uma resposta rápida do jarvis
        if any(term in comando for term in ["ta ai", "tá ai", "tá", "ai"]):
            fala.falar("Sempre á sua disposição, senhor!")
            continue

        # Função para informa a hora atual
        if any(term in comando for term in ["hora", "horas", "horário"]):
            hora.horas()
            continue
        
        # Função para informa a data (dia, mês, ano)
        if any(term in comando for term in ["data", "dia", "mes", "mês", "ano"]):
            if "data" in comando:
                data.data()
            elif "dia" in comando:
                data.dia()
            elif "mes" in comando or "mês" in comando:
                data.mes()
            elif "ano" in comando:
                data.ano()
            continue

        # Função para buscar a previsão do tempo
        if any(term in comando for term in ["previsão", "previsão do tempo", "tempo"]):
            clima.previsao(comando)
            continue

        # Função para abrir aplicativos
        if any(term in comando for term in ["abra", "abrir", "abra o", "abrir o"]):
            abra.abrir(comando)
            continue

        # Função para calcular uma expressão númerica
        if any(term in comando for term in ["calcular", "calcule"]):
            calculadora.calcular(comando)
            continue
        
        # Função para tocar música no youtube
        if any(term in comando for term in ["toque", "tocar", "youtube"]):
            youtube.tocar_musica(comando)
            continue

        # Função para pesquisar
        if any(term in comando for term in ["procure por", "pesquise sobre", "pesquise", "procure"]):
            pesquisa.pesquisar(comando)
            continue
        
        # Função para encerrar o jarvis
        if any(term in comando for term in ["obrigado"]):
            fala.falar("Tudo bem! Se precisar, estou aqui!")
            break # Finaliza o loop e encerra o programa

# Inicia o jarvis
if __name__ == "__main__":
    main()