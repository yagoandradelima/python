import requests
from bs4 import BeautifulSoup

# URL do site Sofascore que queremos fazer o scraping
url = 'https://www.sofascore.com/'

# Fazendo a requisição HTTP
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Criando o objeto BeautifulSoup com o conteúdo da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Agora você pode usar métodos do BeautifulSoup para encontrar e extrair os dados desejados
    # Aqui está um exemplo de como você pode encontrar todos os elementos <a> na página
    links = soup.find_all('a')

    # Iterando sobre os links encontrados
    for link in links:
        # Extraindo o texto e o URL de cada link
        link_text = link.text
        link_url = link['href']

        # Imprimindo os resultados
        print(f'Texto do link: {link_text}')
        print(f'URL do link: {link_url}')
else:
    print('Falha ao fazer a requisição HTTP')