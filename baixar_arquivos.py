import os
import requests
from bs4 import BeautifulSoup

def download_file(url, output_dir):
    # Define o nome local do arquivo com base na última parte da URL
    local_filename = os.path.join(output_dir, url.split('/')[-1])
    print(f"Baixando: {url}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Arquivo salvo em: {local_filename}")
    return local_filename

def download_files_from_directory(url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Filtos
    for link in soup.find_all('a'):
        href = link.get('href')
        if not href or href in ['../', '/', ''] or '?' in href:
            continue
        if not href.endswith('/'):
            file_url = url + href
            download_file(file_url, output_dir)

def main():
    urls_contabeis = [
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/",
        "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/"
    ]

    # Baixa os arquivos e cria uma pasta especifica
    for url in urls_contabeis:
        ano = url.rstrip('/').split('/')[-1]
        output_dir = os.path.join("demonstracoes_contabeis", ano)
        print(f"\nProcessando arquivos do ano: {ano}")
        download_files_from_directory(url, output_dir)

    operadoras_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/?C=N;O=A"
    response = requests.get(operadoras_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Procura o link e realiza o download
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.lower().endswith('.csv'):
            file_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/" + href
            output_dir = "operadoras"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            print(f"\nBaixando Dados Cadastrais das Operadoras Ativas:")
            download_file(file_url, output_dir)

if __name__ == "__main__":
    main()
