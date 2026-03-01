import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

# Inicializa o Faker para o Brasil
fake = Faker("pt_BR")

# --- 1. DEFININDO OS 30 PRODUTOS (WEPINK) ---
# Estrutura: [Nome, Categoria, Preço Custo, Preço Venda]
produtos_lista = [
    # Perfumaria
    ["Perfume Red", "Perfumaria", 80.00, 249.90],
    ["Perfume Gold", "Perfumaria", 85.00, 259.90],
    ["Perfume Virgin", "Perfumaria", 75.00, 239.90],
    ["Body Splash Vanilla", "Perfumaria", 25.00, 89.90],
    ["Body Splash Candy", "Perfumaria", 25.00, 89.90],
    ["Perfume de Bolso (Pocket)", "Perfumaria", 15.00, 49.90],
    # Skincare Facial
    ["Sérum 10 em 1", "Skincare Facial", 40.00, 149.90],
    ["Espuma de Limpeza", "Skincare Facial", 15.00, 69.90],
    ["Hidratante Facial Noturno", "Skincare Facial", 35.00, 119.90],
    ["Protetor Solar com Cor", "Skincare Facial", 30.00, 99.90],
    ["Água Micelar", "Skincare Facial", 12.00, 45.90],
    ["Máscara de Argila Rosa", "Skincare Facial", 18.00, 59.90],
    ["Sérum Vitamina C", "Skincare Facial", 38.00, 139.90],
    # Body Care
    ["Hidratante Corporal Iluminador", "Body Care", 22.00, 79.90],
    ["Esfoliante de Melancia", "Body Care", 20.00, 74.90],
    ["Óleo Corporal Bifásico", "Body Care", 25.00, 89.90],
    ["Creme para Mãos", "Body Care", 10.00, 34.90],
    ["Desodorante Serum", "Body Care", 14.00, 42.90],
    ["Manteiga Corporal Extra Hidratante", "Body Care", 28.00, 94.90],
    # Cabelos
    ["Shampoo de Crescimento", "Cabelos", 18.00, 59.90],
    ["Condicionador Selante", "Cabelos", 19.00, 62.90],
    ["Máscara de Reconstrução", "Cabelos", 25.00, 89.90],
    ["Óleo Reparador de Pontas", "Cabelos", 15.00, 54.90],
    ["Leave-in Protetor Térmico", "Cabelos", 17.00, 58.90],
    ["Tônico Capilar", "Cabelos", 22.00, 79.90],
    # Maquiagem
    ["Base Alta Cobertura", "Maquiagem", 35.00, 129.90],
    ["Corretivo Líquido", "Maquiagem", 20.00, 69.90],
    ["Gloss Labial com Volume", "Maquiagem", 15.00, 59.90],
    ["Blush Cremoso", "Maquiagem", 18.00, 64.90],
    ["Bruma Fixadora com Brilho", "Maquiagem", 20.00, 79.90],
]

df_produtos = pd.DataFrame(
    produtos_lista, columns=["Nome_Produto", "Categoria", "Preco_Custo", "Preco_Venda"]
)
df_produtos.index.name = "ID_Produto"
df_produtos.reset_index(inplace=True)
df_produtos["ID_Produto"] += 1

# --- 2. GERANDO CLIENTES COM FAKER (80 Clientes) ---
clientes_data = []
for i in range(1, 81):
    clientes_data.append(
        {
            "ID_Cliente": i,
            "Nome_Completo": fake.name(),
            "CPF": fake.cpf(),
            "Cidade": fake.city(),
            "Estado": fake.state_abbr(),
        }
    )
df_clientes = pd.DataFrame(clientes_data)

# --- 3. GERANDO VENDAS (1000 Vendas em 2025) ---
vendas_data = []
data_inicial = datetime(2025, 1, 1)

for i in range(1, 1001):
    prod = df_produtos.sample(n=1).iloc[0]
    cli = df_clientes.sample(n=1).iloc[0]

    data_venda = data_inicial + timedelta(
        days=random.randint(0, 364), hours=random.randint(8, 22)
    )
    qtd = random.choices([1, 2, 3, 5], weights=[70, 20, 7, 3])[0]

    vendas_data.append(
        {
            "ID_Venda": i,
            "Data_Venda": data_venda.strftime("%Y-%m-%d %H:%M:%S"),
            "ID_Cliente": cli["ID_Cliente"],
            "ID_Produto": prod["ID_Produto"],
            "Quantidade": qtd,
        }
    )

df_vendas = pd.DataFrame(vendas_data)

# --- 4. EXPORTAÇÃO ---
df_produtos.to_csv("produtos_wepink.csv", index=False)
df_clientes.to_csv("clientes_wepink.csv", index=False)
df_vendas.to_csv("vendas_wepink.csv", index=False)

print("Sucesso! Arquivos gerados para o ETL.")
