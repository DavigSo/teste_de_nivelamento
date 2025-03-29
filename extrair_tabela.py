import pdfplumber

pdf_path = 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'


all_tables = []

# abrir e extrair tabelas
with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        tables = page.extract_tables()
        if tables:
            print(
                f"Tabelas encontradas na página {page_number}: {len(tables)}")
        else:
            print(f"Nenhuma tabela encontrada na página {page_number}.")
        all_tables.extend(tables)

# Encontrar tabelas e printar a primeira
if all_tables:
    print("Primeira tabela extraída:")
    for row in all_tables[0]:
        print(row)
else:
    print("Nenhuma tabela foi extraída.")
