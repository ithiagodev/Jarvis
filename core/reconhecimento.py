from core.fala import falar
import speech_recognition as sr
import time

def ouvir_audio():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Aguardando sua fala...")
        time.sleep(1) # Pausa de 1 segundo antes de escutar a fala
        audio = microfone.listen(source, timeout=2, phrase_time_limit=10)

    try:
        print("Processando...")

        # Usando o serviço de reconhecimento do Google para transcrever o áudio
        comando = microfone.recognize_google(audio, language="pt-BR") # Converte áudio para texto em português
        print(f"Você disse: {comando}") 

        # Remover palavras-chave como "jarvis", "jar" etc., se presentes
        if any(term in comando for term in ["jarvis", "jar", "vis"]):
            comando = comando.lower().replace("javis", "").replace("jar", "").replace("vis", "").strip()

        return comando.lower() # Colocando o comando em minúsculas para padronização
    
    except sr.UnknownValueError:
        # Caso não entenda o que foi dito
        print("Desculpe, não entendi o que disse, senhor!")
        return None

    except sr.RequestError as e:
        # Caso haja erro de conexão com o serviço de reconhecimento de fala
        print(f"Erro na conexão: {e}")
        print("Erro ao se conectar ao serviço de reconhecimento de fala.")

        falar("Senhor, houve um problema na conexão. Por favor, fale novamente.")
        return None
