from core.fala import falar
import datetime

def horas():
    # Obtém a hora atual no formato HH:MM
    hora_minuto = datetime.datetime.now().strftime("%H:%M")
    hora = datetime.datetime.now().hour  

    # Define o período do dia com base na hora atual
    if 6 <= hora < 12:
        periodo = "da manhã"
    elif 12 <= hora < 18:
        periodo = "da tarde"
    else:
        periodo = "da noite"

    # Monta e fala a hora atual
    mensagem = f"Agora são {hora_minuto} {periodo}, senhor!"
    falar(mensagem)
    print(f"Hora: {hora_minuto} ({periodo})")
