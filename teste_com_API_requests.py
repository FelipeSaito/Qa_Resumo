# teste_com_API_requests é um tipo de teste que serve para verificar se uma API está funcionando corretamente.
# Geralmente faz uma requisição para a API, confirma se a resposta tem um status corretos e também verifica se o JSON retornado possui certas informações (como uma chave específica)

import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

assert response.status_code == 200, f"Erro: Status code {response.status_code}"

data = response.json()

assert "name" in data, "Erro: A chave 'name' não está presente nos dados JSON"

print("Teste da API realizado com sucesso!")
