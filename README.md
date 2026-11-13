# Lista Híbrida — Busca e Reordenação

Projeto desenvolvido em **Python e Streamlit** para a implementação e visualização de uma estrutura de dados denominada Lista Híbrida, com operações de busca, inserção e reorganização de elementos.

A aplicação foi desenvolvida como parte de uma atividade acadêmica, permitindo acompanhar o funcionamento da estrutura e compreender as etapas executadas pelo algoritmo.

---

## 1. Integrantes do Grupo

| NOME | RA |
|---|---|
| Mateus Vitalino Jesus de Almeida | 12725148609 |
| Silas Silva Rocha | 12724163789 |
| Rodrigo Silva Santana | 12725143243 |
| Jeferson dos Santos Vieira | 12725161355 |
| José Leonardo de Almeida Santos | 12725217611 |

---

## 2. Funcionalidades Implementadas

O projeto contempla as seguintes operações:

- **Estrutura inicial:** criação de uma região principal ordenada com 1.024 números inteiros distintos.
- **Geração dos dados:** utilização de uma semente (`42` por padrão), garantindo a reprodução dos mesmos dados em diferentes execuções.
- **Cauda não ordenada:** armazenamento temporário de até 10 novos elementos.
- **Inserção:** inclusão de novos elementos no final da cauda, impedindo a inserção de chaves duplicadas.
- **Busca:** utilização da busca binária na região principal e da busca sequencial na cauda.
- **Contagem de operações:** registro individual das iterações de cada método de busca e do total de comparações.
- **Reorganização automática:** ao atingir 10 elementos na cauda, seus valores são ordenados e incorporados à região principal por meio de intercalação.
- **Testes automatizados:** verificação do funcionamento das principais operações da estrutura.

---

## 3. Organização dos Arquivos

O projeto está dividido em arquivos responsáveis pela interface, implementação da estrutura de dados, dependências e testes.

```text
projeto_lista_hibrida/
│
├── atividade_extra.py
├── lista_hibrida.py
├── requirements.txt
├── README.md
│
└── tests/
    └── test_lista_hibrida.py
```

**Responsabilidade dos arquivos:**

- `atividade_extra.py`: arquivo relacionado à aplicação e sua interface.
- `lista_hibrida.py`: implementação da estrutura de dados e das operações do algoritmo.
- `requirements.txt`: lista de dependências necessárias para executar o projeto.
- `README.md`: documentação e instruções de utilização.
- `tests/test_lista_hibrida.py`: testes automatizados para verificar o comportamento da implementação.

---

## 4. Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Desenvolvimento da lógica e das operações do algoritmo. |
| Streamlit | Construção da interface gráfica e interação com o usuário. |
| Unittest | Execução dos testes automatizados. |

**Requisito recomendado:** Python 3.10 ou superior.

---

## 5. Instalação e Execução

Para executar a aplicação localmente, siga as etapas abaixo.

### 5.1. Criar o ambiente virtual

Abra o terminal na pasta do projeto e execute:

```bash
python -m venv .venv
```

### 5.2. Ativar o ambiente virtual

Escolha o comando correspondente ao seu sistema operacional:

**Windows PowerShell:**
```bash
.venv\Scripts\Activate.ps1
```

**Windows CMD:**
```bash
.venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 5.3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5.4. Iniciar a aplicação

```bash
streamlit run app.py
```

Após a execução, o Streamlit disponibilizará um endereço local no terminal, normalmente:

`http://localhost:8501`

**Observação:** o comando de inicialização utiliza `app.py`. Caso o arquivo principal tenha outro nome, ajuste o comando de acordo com o nome correto do arquivo.

---

## 6. Execução dos Testes

Os testes automatizados podem ser executados diretamente pelo terminal, na pasta principal do projeto:

```bash
python -m unittest discover -s tests -v
```

A implementação possui testes para verificar:

- Geração e reprodução dos dados iniciais.
- Ausência de elementos duplicados.
- Inserção de novos valores.
- Funcionamento das buscas binária e sequencial.
- Contabilização das iterações.
- Reorganização após a décima inserção.
- Preservação dos dados durante a intercalação.

---

## 7. Componentes da Interface Streamlit

A interface utiliza diferentes recursos do Streamlit para apresentar os dados, receber informações e permitir a interação com o algoritmo.

| Componente | Finalidade |
|---|---|
| `st.set_page_config` | Define as configurações da página. |
| `st.title`, `st.caption`, `st.write` | Apresentam títulos, descrições e textos. |
| `st.session_state` | Mantém os dados durante a sessão. |
| `st.sidebar` | Organiza os controles na barra lateral. |
| `st.columns`, `st.metric` | Apresentam indicadores em colunas. |
| `st.tabs` | Organiza o conteúdo em abas. |
| `st.form`, `st.number_input` | Permitem inserir informações. |
| `st.form_submit_button`, `st.button` | Executam ações solicitadas pelo usuário. |
| `st.progress` | Demonstra o nível de ocupação da cauda. |
| `st.success`, `st.error`, `st.warning`, `st.info` | Exibem mensagens de retorno. |
| `st.dataframe`, `st.table` | Apresentam os dados em tabelas. |
| `st.rerun` | Atualiza a interface. |
| `st.divider` | Separa visualmente as seções. |

A aplicação também possui uma aba chamada **Como funciona**, na qual são apresentados os componentes utilizados, suas finalidades e suas respectivas localizações no código-fonte.

---

## 8. Funcionamento do Algoritmo

### 8.1. Contagem de iterações

O algoritmo contabiliza uma iteração a cada comparação realizada com um elemento durante a busca.

- **Busca binária:** cada comparação com o elemento central da região ordenada representa uma iteração.
- **Busca sequencial:** cada elemento examinado na cauda representa uma iteração.

Quando a chave é encontrada na região principal, a busca é encerrada sem percorrer a cauda.

Caso não seja encontrada, a busca continua sequencialmente pelos elementos armazenados nela.

A aplicação apresenta separadamente as iterações de cada busca e o total de comparações realizadas.

### 8.2. Processo de reorganização

A reorganização acontece quando a cauda atinge sua capacidade máxima de 10 elementos.

O processo ocorre em três etapas:

1. **Ordenação:** os elementos armazenados na cauda são colocados em ordem crescente.
2. **Intercalação:** os elementos da cauda são combinados com a região principal, também ordenada, mantendo a sequência crescente.
3. **Atualização:** após a intercalação, todos os elementos passam a fazer parte da região principal e a cauda fica vazia.

Esse procedimento mantém a organização da estrutura e permite que as próximas buscas continuem utilizando a busca binária na região principal.

---

## 9. Objetivo do Projeto

O objetivo é aplicar conceitos de estruturas de dados e algoritmos de busca, demonstrando como combinar diferentes estratégias para realizar consultas e inserções de maneira organizada.

A interface desenvolvida em Streamlit permite acompanhar as operações, visualizar os dados e observar o comportamento da estrutura durante as inserções, buscas e reorganizações.


