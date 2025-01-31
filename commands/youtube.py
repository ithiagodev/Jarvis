from core.fala import falar
from pywhatkit import playonyt

def tocar_musica(comando):
        musica = comando.lower().replace("toque", "").replace("tocar", "").replace("youtube", "").strip()

        # Verificando se o comando está vazio após o processamento
        if not musica:
            falar("Desculpe, não consegui identificar a música que você deseja tocar, senhor!")
            return
        
        # Tocando a música no YouTube
        playonyt(musica)
        falar(f"Tocando {musica} no YouTube.")
        print(f"Tocando {musica} no YouTube.")
