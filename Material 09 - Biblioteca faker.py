# Biblioteca Faker
# Utilizada para gerar dados ficticios em vários idiomas

from faker import Faker
import os

os.system('cls')

fake = Faker(locale='pt-BR')
fake_2 = Faker(locale=['pt-BR', 'es-ES', 'en-US'])

# Como utilizar?
print(fake.text(), '\n')
print(fake.address(), '\n')
print(fake.ascii_email(), '\n')
print(fake.ascii_free_email(), '\n')
print(fake.mac_address(), '\n')

# 10 nomes aleatórios
for _ in range(10):
    print(fake.name())
print()

for _ in range(10):
    print(fake.name_female())
print()

print(fake.random_letter())
print(fake.random_letters(8))
print(fake.year())
print(fake.cpf())
print(fake.rg())
print(fake.city())