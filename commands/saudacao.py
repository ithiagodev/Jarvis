from core.fala import falar
from commands.clima import extrair_dados
import datetime
import random

frases = ["Hoje é um ótimo dia para aprender algo novo em programação.",
          "Cada linha de código escrita hoje é um passo mais próximo do seu objetivo.",
          "Transforme erros de compilação em oportunidades de aprendizado.",
          "Um código bem escrito hoje é uma vitória amanhã.",
          "Programar é como resolver enigmas: quanto mais você pratica, mais fácil fica.",
          "Hoje é perfeito para desvendar os segredos do Python.",
          "Nunca foi tão bom dia para dominar algoritmos e lógica.",
          "Pequenos avanços na programação levam a grandes conquistas.",
          "Aprender programação é como plantar uma árvore: comece agora!",
          "Hoje, escreva códigos que inspirem o seu futuro.",
          "Hoje é um ótimo dia para explorar novas ideias.",
          "Use sua imaginação para transformar o ordinário em extraordinário.",
          "Inovar começa com um pequeno ato de coragem: tente algo novo hoje.",
          "Todo grande projeto começa com uma faísca: acenda a sua.",
          "Permita-se sonhar e crie algo maravilhoso hoje.",
          "As ideias mais simples podem ser as mais revolucionárias.",
          "Hoje é perfeito para transformar um pensamento em realidade.",
          "A criatividade é infinita: mergulhe nela sem medo.",
          "Inspire-se no mundo ao seu redor e crie algo único.",
          "Hoje, deixe sua mente voar e sua imaginação florescer.",
          "Hoje é o dia ideal para começar aquele projeto que você adiou.",
          "O que você faz hoje constrói o amanhã que você deseja.",
          "Grandes mudanças começam com pequenos passos, dê o primeiro hoje.",
          "Encare cada desafio como uma chance de crescer.",
          "Aproveite o dia para se aproximar dos seus sonhos.",
          "Hoje é perfeito para criar algo que o mundo nunca viu.",
          "O sol nasceu para lembrar que cada dia é uma nova chance.",
          "Coloque sua energia em coisas que fazem você feliz.",
          "Sua dedicação de hoje definirá suas conquistas futuras.",
          "Aproveite a oportunidade de ser sua melhor versão."]

def bem_vindo():
    # Obtém a hora atual
    hora = datetime.datetime.now().hour

    # Verificando a parte do dia, criando e falando a saudação
    if 6 <= hora < 12:
        descricao = extrair_dados()
        saudacao = f"Bom dia, São {hora} da manhã em {descricao[1]}, {descricao[0]} graus, o tempo está {descricao[2]}."
        falar(saudacao)
        print(saudacao)
        falar(random.choice(frases))
        print(random.choice(frases))
    elif 12 <= hora < 18:
        saudacao = "Boa tarde, senhor! Bem-vindo de volta. Estou à sua disposição!"
        falar(saudacao)
        print(saudacao)
    else:
        saudacao = "Boa noite, senhor! Bem-vindo de volta. Estou à sua disposição!"
        falar(saudacao)
        print(saudacao)