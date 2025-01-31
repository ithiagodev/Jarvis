from core.fala import falar
from core.reconhecimento import ouvir_audio
import os

def abrir(comando):
    comando = comando.replace("abra", "").replace("abrir", "").replace("abra o", "").replace("abrir o", "").strip()
    
    # Caminho onde os aplicativos estão localizados
    caminho = r"CLOQUE AQUI O CAMINHO PARA OS ARQUIVOS"
    
    # Mapeamento de aplicativos conhecidos
    aplicativos = { # Especifique manualmente os arquivos
        "discord": "discord",
        "valorant": "valorant",
        "tlauncher": "tlauncher",
        "roblox": "roblox"
    }

    # Verifica se o comando está na lista de aplicativos conhecidos
    if comando in aplicativos:
        arquivo = aplicativos[comando]
    else:
        falar("Qual aplicativo devo abrir, senhor?")
        resposta = ouvir_audio().strip().lower()
        arquivo = resposta
    
    # Monta o caminho completo do arquivo
    caminho_arquivo = os.path.join(caminho, arquivo)
    
    try:
        # Tenta abrir o arquivo
        os.startfile(caminho_arquivo)
        mensagem = f"O {comando} foi aberto com sucesso, senhor!"
        falar(mensagem)
        print(mensagem)

        # Informa o erro quando ocorre uma falha ao tentar abrir o arquivo
    except FileNotFoundError:
        mensagem = f"O arquivo {arquivo} não foi encontrado, senhor."
        falar(mensagem)
        print(mensagem)
    
        # Informa o erro quando ocorre um problema ao tentar abrir o arquivo
    except Exception as e:
        mensagem = f"Erro ao abrir o {arquivo}: {e}"
        falar(f"Erro ao abrir o {arquivo}, senhor.")
        print(mensagem)
