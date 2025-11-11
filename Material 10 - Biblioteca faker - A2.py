# Biblioteca Faker
# Exemplo prático de uso

from faker import Faker
import pandas as pd
import os
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

for i in range(2500):
    nota_fiscal.append(fake.random_number(digits=6, fix_len=True))
    nome.append(fake.name())
    cpf.append(fake.cpf())
    cidade.append(fake.city())
    profissao.append(fake.job())
    endereco.append(fake.street_address())
    email.append(fake.email())
    data_nascimento.append(fake.date_of_birth())
    idade.append(data_atual.year - data_nascimento[-1].year)
    data_emissao.append(data_atual - timedelta(days=fake.random_int(min=0, max=365)))
    valor_nota.append(fake.pyfloat(left_digits=3, right_digits=2, positive=True))
    comissao.append(valor_nota[-1] * porcentagem_comissao)
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

df.to_csv(r'.\output\Material 10 - Vendas (Bruto).csv', index=False)

print('Arquivo gerado com sucesso...')