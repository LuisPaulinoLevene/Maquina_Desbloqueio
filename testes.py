import requests

# URL da API
url = "https://mozpayment.online/api/1.1/wf/pagamentorotativoemola"

# Carteira e valor fixos
carteira = '1715351739605x645998378212393000'
valor = '1'

# Solicitar os dados ao usuário
quem_comprou = input("Quem comprou: ")
numero = input("Digite o número: ")

# Dados para enviar
payload = {
    'carteira': carteira,
    'quem comprou': quem_comprou,
    'numero': numero,
    'valor': valor
}

# Enviar a solicitação POST com os dados
response = requests.post(url, data=payload)

# Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    print("Solicitação bem-sucedida!")
else:
    print("Erro:", response.status_code)