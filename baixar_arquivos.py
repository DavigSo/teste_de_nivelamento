import requests

base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
anos = ['2022', '2023']

for ano in anos:
    csv_url = f"{base_url}{ano}/demonstracoes_contabeis_{ano}.csv"
    print(f"Baixando: {csv_url}")
    response = requests.get(csv_url)
    if response.status_code == 200:
        with open(f'demonstracoes_contabeis_{ano}.csv', 'wb') as f:
            f.write(response.content)
        print(f"Arquivo demonstracoes_contabeis_{ano}.csv salvo com sucesso! ")
    else:
        print(f"Erro ao baixar o arquivo de {ano}: {response.status_code}")

csv_url_operadoras = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/operadoras_ativas.csv"
print(f"Baixando: {csv_url_operadoras}")
response = requests.get(csv_url_operadoras)
if response.status_code == 200:
    with open('operadoras_ativas.csv', 'wb') as f:
        f.write(response.content)
    print("Arquivo operadoras_ativas.csv salvo com sucesso!")
else:
    print(f"Erro ao baixar operadoras_ativas.csv: {response.status_code}")
