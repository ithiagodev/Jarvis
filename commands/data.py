from core.fala import falar
import datetime

def data():
    # Lista dos meses do ano
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    # Obtém a data atual
    agora = datetime.datetime.now()
    dia = agora.day
    mes = meses[agora.month - 1]  
    ano = agora.year

    # Monta a mensagem da data completa
    mensagem = f"Hoje é dia {dia} de {mes}, de {ano}, senhor!"
    falar(mensagem)
    print(f"Data: {dia} de {mes} de {ano}")

def dia():
    # Obtém o dia atual
    dia = datetime.datetime.now().day
    mensagem = f"Hoje é dia {dia}, senhor!"
    falar(mensagem)
    print(f"Dia: {dia}")

def mes():
    # Lista dos meses do ano
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho", 
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]

    # Obtém o mês atual
    mes_atual = datetime.datetime.now().month
    mensagem = f"Estamos no mês de {meses[mes_atual - 1]}, senhor!"
    falar(mensagem)
    print(f"Mês: {meses[mes_atual - 1]}")

def ano():
    # Obtém o ano atual
    ano_atual = datetime.datetime.now().year
    mensagem = f"O ano atual é {ano_atual}, senhor!"
    falar(mensagem)
    print(f"Ano: {ano_atual}")
