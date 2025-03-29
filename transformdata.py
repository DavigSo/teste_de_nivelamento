import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import zipfile


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

response = requests.get(url)
if response.status_code != 200:
    print(f"Erro ao acessar a página: {response.status_code}")
    exit()

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

pdf_links = []
for a in soup.find_all('a', href=True):
    href = a['href']
    if 'Anexo_I' in href or 'Anexo_II' in href:

        full_link = urljoin(url, href)
        pdf_links.append(full_link)


print("PDFs encontrados:")
for link in pdf_links:
    print(link)


for link in pdf_links:
    pdf_response = requests.get(link)
    if pdf_response.status_code == 200:
        filename = link.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(pdf_response.content)
        print(f"{filename} baixado com sucesso!")
    else:
        print(f"Falha ao baixar {link}: {pdf_response.status_code}")


# Anexar pdf em .zip
with zipfile.ZipFile('Anexos.zip', 'w') as zipf:

    zipf.write('Anexo_I.pdf')
    zipf.write('Anexo_II.pdf')

print("Arquivos compactados com sucesso em 'Anexos.zip'!")
