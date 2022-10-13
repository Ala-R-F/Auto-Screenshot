# Auto-Screenshot
Programa que faz capturas de tela automáticas de uma janela, incluindo no background. Foram utilizados Python, PySimpleGUI para a GUI, e outros pacotes python. Transformado em executável no Py2Exe, porém é versão não mantida.

Há duas maneiras de usar o programa:
<ul>
  <li>Executável
  <li>Pelo interpretador Python
</ul>

Não é possível capturar a tela de uma janela minimizada. O nome do alvo precisa ser o mesmo que aparece de título.


## Instalação do executável:

Transfira o arquivo <b>AutoScreenshot.rar</b> para sua máquina, disponível na pasta Application. Descompacte e execute <b>AutoScreenshot.exe</b>.


## Instalação por interpretador: 

Transfira os seguintes arquivos para sua máquina. 

<ul>
  <li><b>AutoScreenshot.py</b>
  <li><b>directionAS.bat</b>
  <br>Edite no notepad. Entre as primeiras aspas deve conter o caminho para o python.exe, e entre as segundas aspas o caminho para o AutoScreenshot.py. 
  <li><b>AutoScreenshot - Atalho.vbs</b>
  <br>Edite no notepad. Entre as aspas deve conter o caminho do directionAS.bat. 
</ul>

### Serão necessários: 
<ul>
  <li><b>Python >3</b> - Compatível com sistema operacional, versão 32 ou 64 bits.
</ul>

Disponível no site https://www.python.org/downloads/windows/

Ativar a opção ‘adicionar python ao PATH’ (add python to PATH).

Python vem com o pip, necessário para outras instalações. Para instalar com o pip, vá no Painel de Comando e digite “pip install”, sem aspas, e o nome do pacote a ser instalado.

<ul>
  <li><b>PySimpleGUI</b>
  <br>pip install PySimpleGUI <br>
  <li><b>win32gui</b> – Alternativamente contido no pacote PyWin32
  <br>pip install win32gui ou pip install PyWin32<br>
  <li><b>Pillow (PIL)</b>
  <br>pip install Pillow
</ul>

### Uso:

Para acessar o programa, clique no <b>AutoScreenshot - Atalho.vbs</b>. 

O código corre na máquina como um arquivo .py sendo interpretado pelo Python. 
<ul>
  <li>.bat - Diz, por comandos automáticos de terminal, para executar o código. 
  <li>.vbs - Faz com que o terminal se esconda ao executar os comandos por .bat.
</ul>
