# Biblioteca os

import os
os.system('cls')

caminho = os.path.join(os.getcwd(), 'temp')
print('Path/Caminho:', caminho, '\n')
print('Caminho exite?', os.path.exists(caminho), '\n')
print('Caminho existe?', 'Sim' if os.path.exists(caminho) else 'Não', '\n')

# Verificação
try:
    if os.path.exists(caminho):
        print('A pasta existe!')
        os.rmdir('temp')
        print('A pasta foi apagada!')
    else:
        print('A pasta não existe!')
        os.mkdir('temp')
        print('A pasta foi criada!')
except PermissionError:
    print('Permissão negada.')

# Verificaçãp do tipo de objetos
caminho_completo = os.path.join(os.getcwd(), 'testes.py')
print(os.path.isdir(caminho), '\n')
print(os.path.isdir(caminho_completo), '\n')
print(os.path.isfile(caminho_completo), '\n')

# Mudar de diretorio
if os.path.exists(caminho):
    os.chdir('temp')
    print('Path atual:', os.getcwd())
else:
    print('Caminho não encontrado!')
    os.chdir('../')
    print(os.getcwd())

print()