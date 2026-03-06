# Projeto ETL WePink - Ecossistema de BI

## 📝 2. Análise do Projeto
A presente análise justifica a escolha da empresa **WePink** como objeto de estudo para o desenvolvimento deste ecossistema de dados. O projeto foca na transição de um modelo de dados desestruturado para um ambiente de **Business Intelligence (BI)** robusto.

### 💡 Justificativa da Escolha
* **Cenário de Negócio**: A WePink foi selecionada por representar o modelo moderno de, onde o alto volume de vendas gerado por influenciadores digitais exige uma gestão de dados ágil e precisa.
* **Desafio de Dados**: Identificou-se que os dados originais em arquivos CSV apresentavam falta de integridade, como a ausência do faturamento total por venda e inconsistências de codificação (acentuação/UTF-8).

### 🎯 Objetivos da Solução
* **Integração Relacional**: O projeto foi desenhado para converter arquivos isolados de Clientes, Produtos e Vendas em um banco de dados **PostgreSQL** estruturado, respeitando as regras de integridade referencial.
* **Enriquecimento de Informação**: Implementação de uma lógica de **ETL** capaz de cruzar o ID do produto vendido com a tabela mestre de preços via *Stream Lookup*. Isso permitiu calcular o **montante total** de cada transação de forma automática.
* **Tomada de Decisão**: Consolidação dos dados no **BI**, transformando 1000 registros de vendas em indicadores visuais de faturamento e desempenho por categoria.

---

## 🛠️ Tecnologias Utilizadas
* **Apache Hop**: Programa para movimentar as informações. Ele retira os dados de um lugar (como uma planilha), faz as alterações e cálculos necessários e os envia para o destino final.
* **PostgreSQL**: Banco de dados.
* **DBeaver**:  Visualização e gerenciar o banco de dados.
* **Draw.io**: Criação fluxograma.
* **PowerBI**: Visualização de dados e Dashboards de BI.

---

## 📈 Destaques Técnicos do ETL
 **Cálculo em Tempo Real**: Uso do step *Calculator* para processar o `montante_total` (Preço x Quantidade) durante a carga de 1000 registros.
