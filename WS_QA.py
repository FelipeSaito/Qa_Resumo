# Automatizar a coleta de dados na web com requests e BeautifulSoup permite acessar páginas, extrair informações específicas e processá-las automaticamente.
# Isso é útil para testes de software (verificar se sites ou APIs estão funcionando), análise de dados (coletar preços, notícias, etc.) e monitoramento
# (acompanhar mudanças em sites em tempo real), sem precisar fazer isso manualmente.

import requests
from bs4 import BeautifulSoup

url = 'https://www.cnnbrasil.com.br/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    manchetes = soup.find_all('h3')

    print("Principais manchetes da CNN Brasil:")
    for m in manchetes[:5]:
        print(m.text.strip())
else:
    print(f'Falha ao acessar a página. Código de status: {response.status_code}')

url = 'https://www.coindesk.com/price/bitcoin'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    preco = soup.find('div', class_='price-large')

    if preco:
        print(f'\nPreço atual do Bitcoin: {preco.text.strip()}')
    else:
        print('Não foi possível encontrar o preço do Bitcoin.')
else:
    print(f'Falha ao acessar a página. Código de status: {response.status_code}')
