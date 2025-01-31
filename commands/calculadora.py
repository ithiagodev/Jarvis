from core.fala import falar
from sympy import sympify

def calcular(comando):
    expressao = (comando.replace("calcule", "").replace("calcular", "").strip())

    try:
        # Avalia a expressão matemática com segurança
        resultado = sympify(expressao)
        
        # Fala e exibe o resultado
        mensagem = f"O resultado de {expressao} é {resultado}, senhor!"
        falar(mensagem)
        print(mensagem)
    
    except Exception as e:
        # Informa o erro quando a expressão matemática é inválida ou ocorre outra falha
        falar("Desculpe, houve um erro ao tentar calcular, senhor.")
        print(f"Erro: {e}")
