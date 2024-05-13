import requests

# URL da API
url = "https://mozpayment.online/api/1.1/wf/pagamentorotativoemola"

# Dados para enviar
payload = {
    'carteira': '1715351739605x645998378212393000',
    'quem comprou': 'Luis',
    'numero': '873702247',
    'valor': '1'
}

# Enviar a solicitação POST com os dados
response = requests.post(url, data=payload)

# Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    print("Solicitação bem-sucedida!")
else:
    print("Erro:", response.status_code)