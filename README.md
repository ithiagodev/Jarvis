# **Jarvis** 
**Jarvis** é um assistente virtual em Python, desenvolvido para facilitar a interação por voz com o usuário. Ele pode realizar diversas tarefas, como consulta de informações sobre o tempo, hora, data, execução de comandos no sistema e muito mais, tudo por meio de comandos de voz.  

## **Requisitos**  
Este projeto é desenvolvido inteiramente em Python. Para garantir o funcionamento correto, certifique-se de que sua versão do Python seja compatível com o código utilizado.

- Python 3.13 ou superior instalado.
- Microfone funcionando para captura de áudio.
- Conexão com a internet para realizar buscas nas API e consultas em tempo real.
- Chave de API para **OpenWeatherMap**.

### **Instalação de dependências (se necessário):**  
Instale as dependências executando:  
```bash
pip install -r requirements.txt
```
**Obs:** Certifique-se de ter as bibliotecas abaixo instaladas:
- **pyttsx3**: Para síntese de fala.
- **speechrecognition**: Para reconhecimento de fala.
- **requests**: Para realizar requisições HTTP.
- **pywhatkit**: Para tocar músicas no YouTube.
- **sympy**: Para realizar expressões algébricas.
- **wikipedia**: Para realizar pesquisas na Wikipedia.

## **Estrutura dos Arquivos**  
1. **Script Principal (ex.: `main.py`)**: Arquivo responsável por iniciar o Jarvis e gerenciar o fluxo de interação. Ele contém a função `main`, que chama o menu de opções e executa funções específicas.
2. **Funções de Comando**:
   - **Saudação**: Realiza uma saudação dependendo do momento do dia (bom dia, boa tarde ou boa noite).
   - **Hora e Data**: Informa ao usuário a hora atual ou a data completa.
   - **Clima**: Exibe a previsão do tempo atual com temperatura.
   - **Abrir Aplicativos/Sites**: Permite abrir programas ou sites diretamente através de comandos de voz.
   - **Tocar Música**: Reproduz músicas no YouTube com base no nome informado.
   - **Pesquisar**: Realiza pesquisas na Wikipedia e retorna resumos.
   - **Cálculos**: Realiza cálculos matemáticos com base no comando do usuário.
3. **Diretório `core/`**:
   - **fala.py**: Contém a função `falar` que usa a biblioteca **pyttsx3** para a síntese de fala.
   - **reconhecimento.py**: Contém a função `ouvir_audio`, que usa a biblioteca **speechrecognition** para captar comandos de voz.
4. **Diretório `commands/`**:
   - Contém os scripts que implementam funções específicas, como `saudacao.py`, `hora.py`, `clima.py`, `youtube.py`, `pesquisa.py`, etc.

## **Como Executar**  
Para rodar o **Jarvis**, execute o comando abaixo no terminal:  
```bash
python main.py
```
A partir daí, você poderá interagir com o Jarvis por meio de comandos de voz. O sistema está configurado para reconhecer comandos de voz em português.

## **Fluxo de Funcionamento**  
1. **Inicialização**: Ao iniciar, o Jarvis saudará o usuário com base na hora do dia e ficará pronto para ouvir os comandos.
2. **Interação por Voz**: O sistema escuta os comandos do usuário e executa as ações solicitadas, como exibir hora, abrir sites, tocar músicas ou realizar cálculos.
3. **Armazenamento de Dados**: Embora não armazene grandes quantidades de dados, o Jarvis mantém algumas informações temporárias, como o histórico de comandos realizados ou o estado do sistema.

## **Comandos Suportados**  
- **Hora**: "Qual a hora?", "Que horas são?".
- **Data**: "Qual a data de hoje?", "Que dia é hoje?".
- **Clima**: "Qual a previsão do tempo?", "previsão?".
- **Abrir aplicativos**: "Abra o Google Chrome", "Abra o Spotify".
- **Tocar música**: "Toque [artista/banda]", "Tocar [nome da música] no YouTube".
- **Pesquisar**: "Procure por [termo]", "Pesquise sobre [assunto]".
- **Cálculos**: "Calcule [expressão matemática]".

## **Personalização**  
Você pode adicionar novos comandos ou personalizar as funções já existentes, modificando os arquivos dentro dos diretórios `core/` e `commands/`. Isso permite adaptar o Jarvis para atender às suas necessidades.
