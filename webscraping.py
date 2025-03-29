import requests

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)


if response.status_code == 200:
    html_content = response.text
    print(html_content)
else:
    print(f"Erro ao acessar a página: {response.status_code}")
