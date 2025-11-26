# Biblioteca Pandas - Aula 11
# A análise de dados com o Python
import pandas as pd
import os
os.system('cls')

# Leitura do arquivo CSV
dados_csv = pd.read_csv(
    filepath_or_buffer='.\output\Material 27 - Vendas - análise.csv', 
    sep=';', 
    encoding='utf-8'
)

# print(dados_csv)

# Adicionar uma coluna de Vendas Total
# 1) substituir a vírgula pelo ponto
dados_csv['PREÇO UNITÁRIO'] = dados_csv['PREÇO UNITÁRIO'].str.replace(',', '.')

# 2) converte a coluna para um valor numérico
dados_csv['PREÇO UNITÁRIO'] = pd.to_numeric(dados_csv['PREÇO UNITÁRIO'])

# 3) Multiplicar qtd x preço unitário
dados_csv['TOTAL'] = dados_csv['QUANTIDADE'] * dados_csv['PREÇO UNITÁRIO']

# Função para formatar em reais
def formatar_em_reais(pValor):
    return 'R$ {:,.2f}'.format(pValor).replace(',', '#').replace('.', ',').replace('#', '.')

# Agrupamento por Mês e Totalização
# Cuidados nesse tipo de totalização. O agrupamento por mês
# não leva em conta a segmentação por ano.

print('Total de vendas por mês'.center(50, '-'),'\n')
resultado_mes = dados_csv.groupby('MES')['TOTAL'].sum()
print(resultado_mes.apply(formatar_em_reais))
print()

print('Total por referência'.center(50, '-'),'\n')
resultado_ref = dados_csv.groupby('REFERENCIA')['TOTAL'].sum()
print(resultado_ref.apply(formatar_em_reais))
print()

print('Quantidade de registros:', dados_csv['PRODUTO'].count())
print()

print('Total Faturamento:', formatar_em_reais(dados_csv['TOTAL'].sum()))
print()

# Somatória dos valores acima de R$ 5.000
valor_total = 0
diferenca = 0
limite = 5000

for registro in dados_csv['TOTAL']:
    if registro > limite:
        valor_total += registro
    else:
        diferenca += registro

print('Valor total acima de',
      formatar_em_reais(limite),
      'é de',
      formatar_em_reais(valor_total), '\n')

print('Valor total da diferença é de',
      formatar_em_reais(diferenca), '\n')

# Salvar
dados_csv.to_csv(r'.\output\Material 27 - Resultado final.csv',
                 sep=';',
                 index=False)

print('Arquivo gerado com sucesso ')
