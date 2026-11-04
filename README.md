# Lista Híbrida — Busca e Reordenação

Aplicação educacional em Python + Streamlit para a atividade extra descrita no PDF.

## O que o projeto implementa

- Região ordenada inicial com 1.024 inteiros distintos.
- Geração reprodutível usando uma semente (`42` por padrão).
- Cauda não ordenada com capacidade máxima de 10 chaves.
- Inserção no final da cauda e rejeição de chaves repetidas.
- Busca binária na região principal, seguida de busca sequencial na cauda.
- Contagem separada das iterações e total.
- Na décima inserção, ordenação da cauda e intercalação com a região principal.
- Testes automatizados.
- Interface visual com componentes Streamlit identificados na aba “Como funciona”.

## Estrutura de arquivos

```text
projeto_lista_hibrida/
├── app.py
├── lista_hibrida.py
├── requirements.txt
├── README.md
└── tests/
    └── test_lista_hibrida.py
```

## Executar localmente

Recomendado: Python 3.10 ou superior.

No terminal, dentro da pasta do projeto:

```bash
python -m venv .venv
```

Ativar o ambiente:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Windows CMD: `.venv\Scripts\activate.bat`
- Linux/macOS: `source .venv/bin/activate`

Instalar dependências:

```bash
pip install -r requirements.txt
```

Iniciar a aplicação:

```bash
streamlit run app.py
```

O Streamlit exibirá um endereço local no terminal, normalmente `http://localhost:8501`.

## Executar os testes

Na raiz do projeto:

```bash
python -m unittest discover -s tests -v
```

Os testes verificam geração, reprodutibilidade, unicidade, inserção, buscas,
contagem, reorganização na décima inserção e preservação dos dados.

## Publicar gratuitamente no Streamlit Community Cloud

1. Crie um repositório público no GitHub.
2. Envie todos os arquivos desta pasta para a raiz do repositório.
3. Acesse https://share.streamlit.io/ e entre com sua conta GitHub.
4. Selecione **Create app**.
5. Escolha o repositório, a branch e o arquivo principal `app.py`.
6. Clique em **Deploy**.
7. Aguarde a instalação das dependências e a publicação.
8. Copie o link público gerado e teste-o em uma janela anônima.

O endereço público só existe depois que você realizar a publicação na sua conta.
Não é possível criar esse link sem acesso autorizado ao seu GitHub/Streamlit.

## Componentes Streamlit usados

| Componente | Para que serve |
|---|---|
| `st.set_page_config` | Configuração da página |
| `st.title`, `st.caption`, `st.write` | Textos e títulos |
| `st.session_state` | Estado da sessão |
| `st.sidebar` | Barra lateral |
| `st.columns`, `st.metric` | Indicadores em colunas |
| `st.tabs` | Abas da aplicação |
| `st.form`, `st.number_input` | Entrada de dados |
| `st.form_submit_button`, `st.button` | Ações |
| `st.progress` | Ocupação da cauda |
| `st.success`, `st.error`, `st.warning`, `st.info` | Mensagens de retorno |
| `st.dataframe`, `st.table` | Tabelas |
| `st.rerun` | Atualização da interface |
| `st.divider` | Separação visual |

A aba “Como funciona” também apresenta a função de cada componente e sua localização
no código-fonte.

## Decisões de implementação e pontos para explicar

### Contagem de iterações

Uma iteração é contabilizada a cada comparação com um elemento da região ou da cauda.
Na busca binária, cada comparação com o elemento do meio conta uma iteração.
Na busca sequencial, cada elemento examinado conta uma iteração.

Se a chave for encontrada na região ordenada, a busca termina ali e a cauda não
é percorrida. Se não for encontrada na região ordenada, a busca continua na cauda.

### Reorganização

A cauda é ordenada e depois intercalada com a região principal. A intercalação
percorre as duas sequências ordenadas e escolhe, a cada passo, o menor próximo
elemento. Ao final, a cauda é esvaziada.

### Observação para a apresentação

O PDF exige demonstração presencial e que cada aluno explique o código sem usar IA.
Use este projeto como material de estudo: execute os testes, faça inserções e buscas,
abra `lista_hibrida.py` e pratique explicar cada método com suas próprias palavras.
Não afirme que publicou no Streamlit até ter realizado o deploy e testado o link.

## Checklist em relação ao enunciado

- [x] 1. Região inicial reprodutível com semente.
- [x] 2. Inserção no final da cauda e rejeição de repetidas.
- [x] 3. Busca binária seguida de busca sequencial.
- [x] 4. Iterações por busca, total e local encontrado.
- [x] 5. Reorganização automática na décima inserção e cauda vazia.
- [x] 6. Testes automatizados.
- [x] 7. Aplicação Streamlit, componentes destacados e explicação dos trechos.
- [ ] 8. Publicar no Streamlit Cloud, demonstrar presencialmente e responder ao professor.
- [ ] 9. Cada integrante estudar e explicar individualmente.

Os itens 8 e 9 dependem de ações e da apresentação dos alunos; o código não consegue
substituir essas etapas.
