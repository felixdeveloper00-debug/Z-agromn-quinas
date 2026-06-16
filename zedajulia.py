import streamlit as st

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(
    page_title="ZÉ AGROMÁQUINAS",
    page_icon="🌽",
    layout="wide"
)

# =========================
# ESTILO
# =========================

st.markdown("""
<style>

.main {
    background-color: #ffffff;
}

.titulo {
    text-align:center;
    font-size:75px;
    font-weight:900;
    color:#2E7D32;
    margin-bottom:0px;
}

.subtitulo {
    text-align:center;
    font-size:38px;
    color:#C9A227;
    font-style:italic;
    margin-top:-20px;
    margin-bottom:25px;
}

.produtos {
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:#444;
}

.rodape {
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# BANNER
# =========================

st.image("banner.png", use_container_width=True)

# =========================
# TÍTULO
# =========================

st.markdown("""
<div class="titulo">
ZÉ AGROMÁQUINAS
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitulo">
Há mais de 40 anos cultivando confiança
</div>
""", unsafe_allow_html=True)

# =========================
# PRODUTOS PRINCIPAIS
# =========================

st.markdown("""
<div class="produtos">
🌽 Silagem de Milho &nbsp;&nbsp;&nbsp; • &nbsp;&nbsp;&nbsp; 🌾 Milho a Granel
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================
# BOTÕES
# =========================

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "📱 Solicitar Orçamento no WhatsApp",
        "https://wa.me/556299517635"
    )

with col2:
    st.link_button(
        "📸 Instagram",
        "https://www.instagram.com/ze_agromaquinas"
    )

st.divider()

# =========================
# QUEM SOMOS
# =========================

st.header("Quem Somos")

st.write("""
A ZÉ AGROMÁQUINAS atua há mais de 40 anos atendendo produtores rurais
de Aragoiânia e toda a região.

Trabalhamos com silagem de milho e milho a granel,
oferecendo qualidade, confiança e compromisso com nossos clientes.

Nosso objetivo é fornecer produtos de excelência para auxiliar
o produtor rural em suas atividades diárias.
""")

st.divider()

# =========================
# GALERIA DE PRODUTOS
# =========================

st.header("Nossos Produtos")

col1, col2 = st.columns(2)

with col1:
    st.image("silagem.jpg", use_container_width=True)
    st.subheader("🌽 Silagem de Milho")

    st.write("""
    Silagem de alta qualidade,
    produzida para garantir excelente desempenho nutricional
    para bovinos de corte e leite.
    """)

with col2:
    st.image("milho.jpg", use_container_width=True)
    st.subheader("🌾 Milho a Granel")

    st.write("""
    Milho selecionado e armazenado adequadamente,
    ideal para alimentação animal e diversas aplicações rurais.
    """)

st.divider()

# =========================
# CONTATO
# =========================

st.header("Solicite seu orçamento")

with st.form("contato"):

    nome = st.text_input("Nome")

    telefone = st.text_input("Telefone")

    mensagem = st.text_area(
        "Mensagem"
    )

    enviar = st.form_submit_button("Enviar")

    if enviar:

        st.success(
            "Mensagem registrada! Entre em contato pelo WhatsApp para atendimento imediato."
        )

# =========================
# RODAPÉ
# =========================

st.markdown("""
<div class="rodape">

📍 Aragoiânia - GO

🚜 Atendimento em toda a região

📞 (62) 99517-635

📸 @ze_agromaquinas

🌽 ZÉ AGROMÁQUINAS

</div>
""", unsafe_allow_html=True)
