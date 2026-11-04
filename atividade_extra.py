import streamlit as st
import pandas as pd

from lista_hibrida import ListaHibrida

st.set_page_config(
    page_title="Lista Híbrida | Busca e Reordenação",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 Lista Híbrida — Busca e Reordenação")
st.caption(
    "Demonstração de uma estrutura com região ordenada, cauda não ordenada, "
    "busca binária, busca sequencial e intercalação."
)

# Cada sessão do navegador mantém sua própria estrutura de dados.
if "estrutura" not in st.session_state:
    st.session_state.estrutura = ListaHibrida(semente=42)
if "historico" not in st.session_state:
    st.session_state.historico = []

estrutura = st.session_state.estrutura

with st.sidebar:
    st.header("Controles")
    st.write("A estrutura começa com 1.024 inteiros distintos.")
    st.metric("Semente utilizada", estrutura.semente)
    if st.button("Reiniciar demonstração", use_container_width=True):
        st.session_state.estrutura = ListaHibrida(semente=42)
        st.session_state.historico = []
        st.rerun()

col1, col2, col3 = st.columns(3)
col1.metric("Região ordenada", f"{len(estrutura.regiao_ordenada):,}".replace(",", "."))
col2.metric("Cauda não ordenada", f"{len(estrutura.cauda)}/10")
col3.metric("Total de chaves", f"{estrutura.quantidade_total:,}".replace(",", "."))

st.divider()
aba_inserir, aba_buscar, aba_visualizar, aba_explicacao = st.tabs(
    ["➕ Inserir chave", "🔍 Buscar chave", "📊 Visualizar estrutura", "📘 Como funciona"]
)

with aba_inserir:
    st.subheader("Inserção na cauda")
    st.write(
        "Digite um inteiro que ainda não exista. Ele será colocado no final "
        "da cauda, sem ordenação."
    )
    with st.form("form_inserir", clear_on_submit=True):
        nova_chave = st.number_input(
            "Nova chave (número inteiro)",
            min_value=-2_000_000_000,
            max_value=2_000_000_000,
            value=1_000_001,
            step=1
        )
        enviar = st.form_submit_button("Inserir chave", type="primary")

    if enviar:
        sucesso, mensagem = estrutura.inserir(int(nova_chave))
        (st.success if sucesso else st.error)(mensagem)
        if sucesso and not estrutura.cauda:
            st.info("A região foi reorganizada e a cauda está vazia.")
        st.rerun()

    st.progress(len(estrutura.cauda) / estrutura.CAPACIDADE_CAUDA)
    st.caption(f"Espaços ocupados na cauda: {len(estrutura.cauda)} de 10.")
    if estrutura.cauda:
        st.write("**Ordem atual de chegada:**", estrutura.cauda)
    else:
        st.info("A cauda está vazia no momento.")

with aba_buscar:
    st.subheader("Busca de uma chave")
    chave_busca = st.number_input(
        "Qual inteiro você deseja procurar?",
        value=int(estrutura.regiao_ordenada[0]),
        step=1,
        key="chave_busca"
    )
    if st.button("Executar busca", type="primary"):
        resultado = estrutura.buscar(int(chave_busca))
        st.session_state.ultimo_resultado = resultado
        st.session_state.historico.insert(0, {
            "Chave": resultado.chave,
            "Resultado": "Encontrada" if resultado.encontrada else "Não encontrada",
            "Local": resultado.local,
            "Binária": resultado.iteracoes_binaria,
            "Sequencial": resultado.iteracoes_sequencial,
            "Total": resultado.total_iteracoes
        })

    if "ultimo_resultado" in st.session_state:
        resultado = st.session_state.ultimo_resultado
        if resultado.encontrada:
            st.success(f"Chave {resultado.chave} encontrada: {resultado.local}.")
        else:
            st.warning(f"Chave {resultado.chave} não encontrada nas duas regiões.")

        a, b, c = st.columns(3)
        a.metric("Iterações binárias", resultado.iteracoes_binaria)
        b.metric("Iterações sequenciais", resultado.iteracoes_sequencial)
        c.metric("Total de iterações", resultado.total_iteracoes)
        st.caption(
            "Cada iteração corresponde a uma comparação com um elemento "
            "durante o respectivo algoritmo."
        )

    if st.session_state.historico:
        st.markdown("**Histórico de buscas desta sessão**")
        st.dataframe(pd.DataFrame(st.session_state.historico), use_container_width=True)

with aba_visualizar:
    st.subheader("Estado atual da lista")
    st.write("**Região ordenada — início e fim**")
    esquerda, direita = st.columns(2)
    esquerda.write(estrutura.regiao_ordenada[:20])
    direita.write(estrutura.regiao_ordenada[-20:])
    st.caption("São exibidos os 20 primeiros e os 20 últimos valores para facilitar a leitura.")
    st.write("**Cauda não ordenada (ordem de inserção)**")
    st.write(estrutura.cauda if estrutura.cauda else "[] — vazia")
    st.metric("Reorganizações realizadas", estrutura.total_reorganizacoes)
    st.write("**Verificação das regras internas**")
    if estrutura.validar_invariantes():
        st.success("Todas as invariantes estão válidas: região ordenada, chaves únicas e cauda dentro do limite.")
    else:
        st.error("Foi identificada uma inconsistência na estrutura.")

with aba_explicacao:
    st.subheader("Componentes utilizados e onde aparecem")
    componentes = [
        ("st.set_page_config()", "Configura título, ícone e largura da página.", "app.py — início do arquivo"),
        ("st.title() / st.caption()", "Apresentam o título e o objetivo da aplicação.", "app.py — cabeçalho"),
        ("st.session_state", "Mantém a lista e o histórico entre interações.", "app.py — inicialização"),
        ("st.sidebar", "Agrupa controles de reinicialização.", "app.py — seção Controles"),
        ("st.columns() / st.metric()", "Organizam e mostram os indicadores da estrutura.", "app.py — indicadores"),
        ("st.tabs()", "Separa inserção, busca, visualização e explicação.", "app.py — criação das abas"),
        ("st.form() / st.number_input()", "Recebem a chave que será inserida.", "app.py — aba Inserir"),
        ("st.form_submit_button() / st.button()", "Disparam inserção e busca.", "app.py — abas Inserir e Buscar"),
        ("st.progress()", "Mostra a ocupação da cauda.", "app.py — aba Inserir"),
        ("st.success() / st.error() / st.warning()", "Dão retorno visual das operações.", "app.py — operações"),
        ("st.dataframe()", "Mostra o histórico de buscas.", "app.py — aba Buscar"),
        ("st.rerun()", "Atualiza a tela após uma operação.", "app.py — ações"),
    ]
    st.table(pd.DataFrame(componentes, columns=["Componente", "Função", "Local no código"]))

    st.subheader("Algoritmos principais")
    st.markdown("""
    - **Busca binária:** compara a chave com o elemento do meio e descarta
      metade do intervalo a cada passo. Complexidade: `O(log n)`.
    - **Busca sequencial:** percorre a cauda na ordem de chegada.
      Complexidade: `O(k)`, em que `k` é o tamanho da cauda (no máximo 10).
    - **Intercalação:** depois de ordenar a cauda, compara os menores elementos
      das duas sequências e monta uma única região ordenada. Custo linear
      em relação ao total de elementos envolvidos.
    """)

st.divider()
st.caption(
    "Atividade Extra — Lista Híbrida com Busca e Reordenação | "
    "Aplicação educacional para demonstração em sala."
)
