import requests
from bs4 import BeautifulSoup

url = 'https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes'

# É boa prática incluir headers para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')
    # Agora você navega no HTML usando soup.find() ou soup.find_all()
    print(soup.title.text)
else:
    print(f"Erro na requisição: {resposta.status_code}")