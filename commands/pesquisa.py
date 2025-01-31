from core.fala import falar
import wikipedia

def pesquisar(comando):
    comando = comando.replace("procure por", "").replace("pesquise sobre", "").replace("pesquise", "").replace("procure", "").strip()

    # Definindo o idioma da Wikipedia como português
    wikipedia.set_lang('pt')

    resultado = ""

    # Realizando a pesquisa na Wikipedia e obtendo o resumo
    try:
        resultado = wikipedia.summary(comando)
    except wikipedia.exceptions.DisambiguationError as e:
        # Caso haja uma ambiguidade, trata o erro e mostra opções ao usuário
        resultado = "Houve uma ambiguidade na pesquisa. Tente ser mais específico, por favor, senhor."
        opcoes = f"Opções: {e.options}"
        falar(opcoes)
        print(opcoes)

    # Monta e Fala o resultado
    falar("De acordo com a Wikipedia")
    falar(resultado)
    print(resultado)
