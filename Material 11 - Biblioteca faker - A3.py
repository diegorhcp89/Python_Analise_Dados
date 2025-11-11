# ETL no Python

# Biblioteca Faker
# Exemplo prático de uso

from faker import Faker
import pandas as pd
import os
import csv
from datetime import date, timedelta

os.system('cls')

data_atual = date.today()
porcentagem_comissao = 0.015
fake = Faker(locale='pt-BR')

nota_fiscal = []
nome = []
cpf = []
cidade = []
profissao = []
endereco = []
email = []
data_nascimento = []
idade = []
data_emissao = []
valor_nota = []
comissao = []
vendedor = []

for i in range(1000):
    nota_fiscal.append(fake.random_number(digits=6, fix_len=True))
    nome.append(fake.name())
    cpf.append(fake.cpf())
    cidade.append(fake.city())
    profissao.append(fake.job())
    endereco.append(fake.street_address())
    email.append(fake.email())

    cc_dt_nascimento = fake.date_of_birth()
    data_nascimento.append(cc_dt_nascimento.strftime('%d/%m/%Y'))

    idade.append(data_atual.year - cc_dt_nascimento.year)

    cc_dt_emissao = data_atual - timedelta(days=fake.random_int(min=0, max=365))
    data_emissao.append(cc_dt_emissao.strftime('%d/%m/%Y'))

    cc_valor_nota = round(fake.pyfloat(left_digits=3, right_digits=2, positive=True))
    valor_nota.append(str(cc_valor_nota).replace('.', ','))

    cc_comissao = cc_valor_nota * porcentagem_comissao
    comissao.append(str(round(cc_comissao, 2)).replace('.', ','))

    vendedor.append(
        fake.random_choices(
            ['Vendendor_A', 'Vendendor_B', 'Vendendor_C', 'Vendedor_D', 'Vendedor_E'], 1)[0]
        )
    
# Geração do DataFrame

df = pd.DataFrame(
    {
        'NOTA_FISCAL': nota_fiscal,
        'NOME': nome,
        'CPF': cpf,
        'CIDADE': cidade,
        'CARGO': profissao,
        'ENDERECO': endereco,
        'EMAIL': email,
        'DATA_NASCIMENTO': data_nascimento,
        'IDADE': idade,
        'DATA_EMISSAO': data_emissao,
        'VALOR_NOTA': valor_nota,
        'COMISSAO': comissao,
        'VENDEDOR': vendedor
    }
)

# print(df.head(), '\n')

df.to_csv(r'.\output\Material 10 - Vendas (Bruto).csv', sep=';', index=False, quoting=csv.QUOTE_MINIMAL)

print('Arquivo gerado com sucesso...')