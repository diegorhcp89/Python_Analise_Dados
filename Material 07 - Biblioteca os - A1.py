# Biblioteca os
# Utilizada para interagir com o sistema operaconal

import os

os.system("cls")  # Limpar a tela (Windows). Use "clear" para Linux/Mac
print(os.name)  # Nome do sistema operacional

os.system('clear' if os.name == 'posix' else 'cls')  # Limpar a tela de forma cross-platform

# environ: Variáveis de ambiente do sistema
print(os.environ.get('username'), '\n')  # Nome do usuário no Windows
print(os.environ.get('path'), '\n')  # Caminho do sistema
print(os.environ.get('computername'), '\n')  # Nome do computador no Windows
print(os.environ.get('userprofile'), '\n')  # Diretório do perfil do usuário no Windows
print(os.environ.get('homepath'), '\n')  # Diretório home do usuário no Windows

# Exiba todos os intens do dicionario
for param in os.environ:
    print(f'{param}: {os.environ.get(param)}', '\n')

# Manipular ou acessar o sistema de arquivos
unidade = 'c:\\'
caminho_a = 'temp'
caminho_b = 'podeApagar'

# Juntar caminhos
caminho_completo = os.path.join(unidade, caminho_a, caminho_b, '\n')
print(caminho_completo)
print(os.getcwd(), '\n')  # Diretório atual

# Exibir partes do caminho
caminho = os.path.join(os.getcwd(), 'teste.py')
print(caminho, '\n')
print('Dicionario atual:', os.curdir, '\n')  # Diretório atual
print('Caminho absoluto:', os.path.basename(caminho), '\n')  # Nome do arquivo