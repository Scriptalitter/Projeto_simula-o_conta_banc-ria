import streamlit as st

st.set_page_config(page_title="Orçamento de PC", page_icon="🐰", layout="wide")


st.title(' Orçamento de PC')

valor_disponivel = st.number_input("💰 Valor disponível para montagem (R$)", min_value=0.0, value=5000.0, step=100.0)

st.markdown("## 🛒 Digite o valor de cada peça")

col1, col2, col3 = st.columns(3)
componentes = [
    "🔌 Placa-mãe", "🧠 Memória RAM", "⚡ Processador",
    "🎮 Placa de vídeo", "💾 Armazenamento (SSD/HDD)", "🔋 Fonte",
    "📦 Gabinete", "❄️ Cooler", "🖥️ Monitor",
    "⌨️🖱️ Teclado+Mouse", "🪟 Sistema operacional", "🎧 Outros periféricos"
]
valores = {}

for i, nome in enumerate(componentes):
    with [col1, col2, col3][i % 3]:
        valores[nome] = st.number_input(nome, min_value=0.0, value=0.0, step=50.0, format="%.2f")

total = sum(valores.values())
restante = valor_disponivel - total

st.markdown("---")
col_a, col_b, col_c = st.columns(3)
col_a.metric("💰 Total dos componentes", f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col_b.metric("💵 Saldo (orçamento - total)", f"R$ {restante:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

if total > valor_disponivel:
    col_c.error(f"⚠️ Excedeu o orçamento em R$ {total - valor_disponivel:,.2f}")
else:
    col_c.success(f"✅ Dentro do orçamento! Sobrou R$ {restante:,.2f}")

if valor_disponivel > 0:
    percent = min(100, (total / valor_disponivel) * 100)
    st.progress(percent / 100)
    st.caption(f"📈 {percent:.1f}% do orçamento utilizado")
else:
    st.warning("Defina um orçamento disponível > 0 para ver a proporção.")