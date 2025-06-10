#  Processador de Clientes

Sistema automatizado para leitura, validação, limpeza e análise de dados de clientes. Desenvolvido para facilitar o tratamento de arquivos em `.csv`, `.xlsx` ou `.json`, o sistema gera relatórios organizados, destaca CPFs inválidos e aplica filtros inteligentes com base em critérios de valor, status e data.

---

##  Funcionalidades

- ✅ Leitura de arquivos nos formatos: `.csv`, `.xlsx`, `.json`
- ✅ Validação de colunas obrigatórias (`Nome`, `CPF`, `Data`, `Valor`, `Status`, `Tipo de Contrato`)
- ✅ Limpeza e normalização de dados (remoção de duplicatas, padronização de nomes, limpeza de CPF)
- ✅ Conversão automática de datas
- ✅ Filtros:
  - Clientes **inadimplentes** com valor > 1000
  - Clientes **cancelados** com valor > 4000 e ano de contrato 2025
- ✅ Geração de **resumo por tipo de contrato** (`count`, `sum`)
- ✅ Exportação de relatórios organizados em Excel
- ✅ Destaque visual em vermelho para **CPFs inválidos**
- ✅ Ajuste automático da largura das colunas no Excel
- ✅ Sistema de **log** completo (`.log`) com erros, avisos e status de cada operação

---
## Como usar 
# 1. Clone o repositório
git clone https://github.com/urtTarzan/projeto_analise_exel_completo
cd projeto_analise_exel_completo

# 2. Instale as dependências
`pip install pandas openpyxl`  
ou  
`python -m pip install pandas openpyxl`

# 3. Coloque os arquivos de entrada na pasta arquivos/brutos/ 
`PS(os arquivos devem conter as colunas de nomes especificas pois esse é só um exemplo baseado em dados ficticios)`

# 4. Execute o programa
`python main.py`



## Observações  
O sistema cria automaticamente as pastas necessárias (arquivos/, relatorios/ etc.)

Caso a pasta arquivos/brutos/ esteja vazia, o processo será interrompido com aviso no console e no log.

Todos os logs são registrados em:
📁 relatorios/processamento.log

### Feito com 💻 por Matheus silva Sousa Oliveira / urtTarzan
