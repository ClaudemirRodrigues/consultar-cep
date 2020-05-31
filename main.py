import requests
print()
print('\033[7;32;33mConsulta CEP\033[m')
print()

cep = input('Informe o CEP a ser consultado: ')

if len(cep) != 8:
    print('\033[31mFormato inválido!\033[m')
    exit()

request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

address_data = request.json()

if 'erro' not in address_data:
    print(f'\033[36mCEP: {address_data["cep"]}')
    print(f'Logradouro: {address_data["logradouro"]} {address_data["complemento"]}')
    print(f'Bairro: {address_data["bairro"]}')
    print(f'Cidade: {address_data["localidade"]}')
    print(f'UF: {address_data["uf"]}\033[m')
else:
    print(f'\033[31m{cep} CEP não cadastrado.\033[m')
