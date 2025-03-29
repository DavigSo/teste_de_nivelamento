import pdfplumber
import pandas as pd
import zipfile

# Aqui temos um exemplo onde resolvi juntar a lógica de extrair_tabale.py e a lógica para gerar csv

pdf_path = 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

all_tables = []


with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        tables = page.extract_tables()
        if tables:
            print(
                f"Tabelas encontradas na página {page_number}: {len(tables)}")
            all_tables.extend(tables)
        else:
            print(f"Nenhuma tabela encontrada na página {page_number}.")

if not all_tables:
    print("Nenhuma tabela foi extraída do PDF.")
else:

    # Execução do arquivo csv

    headers = all_tables[0][0]
    data = []

    # Coleta os dados de todas as tabelas, ignorando a primeira linha (cabeçalho)
    for table in all_tables:
        for row in table[1:]:

            if len(row) == len(headers):
                data.append(row)
            else:
                print(
                    f"Linha ignorada devido a número incorreto de colunas: {row}")

    df = pd.DataFrame(data, columns=headers)

    df.to_csv('Rol_Procedimentos.csv', index=False, encoding='utf-8')

    print("Dados salvos com sucesso no arquivo 'Rol_Procedimentos.csv'.")

nome = 'Davi Sousa'
nome_arquivo_zip = f'Teste_{nome}.zip'

arquivo_csv = 'Rol_Procedimentos.csv'

with zipfile.ZipFile(nome_arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(arquivo_csv)

print(f'Arquivo {nome_arquivo_zip} criado com sucesso.')
