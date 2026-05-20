import streamlit as st

st.set_page_config(page_title="Banco", page_icon="🏦")

if "usuarios" not in st.session_state:
    st.session_state.usuarios = {}
if "saldos" not in st.session_state:
    st.session_state.saldos = {}
if "historicos" not in st.session_state:
    st.session_state.historicos = {}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "usuario_atual" not in st.session_state:
    st.session_state.usuario_atual = ""
if "mensagem" not in st.session_state:
    st.session_state.mensagem = ""

st.title("Banco")
st.write("Bem-vindo ao banco. Use o formulário abaixo para acessar sua conta ou criar uma nova.")


def criar_conta(nome: str, senha: str):
    if not nome or not senha:
        st.session_state.mensagem = "Nome de usuário e senha são obrigatórios."
        return
    if nome in st.session_state.usuarios:
        st.session_state.mensagem = "Nome de usuário já existe. Escolha outro."
        return

    st.session_state.usuarios[nome] = senha
    st.session_state.saldos[nome] = 1000.00
    st.session_state.historicos[nome] = []
    st.session_state.mensagem = "Conta criada com sucesso! Faça login para continuar."


def login(nome: str, senha: str):
    if nome not in st.session_state.usuarios:
        st.session_state.mensagem = "Usuário não encontrado."
        return
    if st.session_state.usuarios[nome] != senha:
        st.session_state.mensagem = "Senha incorreta."
        return

    st.session_state.logged_in = True
    st.session_state.usuario_atual = nome
    st.session_state.mensagem = ""


def logout():
    st.session_state.logged_in = False
    st.session_state.usuario_atual = ""
    st.session_state.mensagem = "Você saiu da conta."


if not st.session_state.logged_in:
    acesso = st.radio("Acesso", ["Entrar", "Criar conta"], horizontal=True)
    with st.form("form_acesso"):
        nome_usuario = st.text_input("Nome de usuário")
        senha = st.text_input("Senha", type="password")
        enviado = st.form_submit_button("Enviar")

    if enviado:
        if acesso == "Entrar":
            login(nome_usuario.strip(), senha.strip())
        else:
            criar_conta(nome_usuario.strip(), senha.strip())

    if st.session_state.mensagem:
        st.info(st.session_state.mensagem)

else:
    st.success(f"Login realizado com sucesso! Olá, {st.session_state.usuario_atual}.")
    saldo_atual = st.session_state.saldos[st.session_state.usuario_atual]
    limite_saque = 500.00

    operacao = st.selectbox("Escolha a operação", ["Ver saldo", "Saque", "Depósito", "Ver Histórico", "Sair"])

    if operacao == "Ver saldo":
        st.write(f"Seu saldo atual é: R$ {saldo_atual:.2f}")

    elif operacao == "Saque":
        valor_saque = st.number_input("Digite o valor do saque", min_value=0.0, step=10.0, format="%.2f")
        if st.button("Realizar saque"):
            if valor_saque <= 0:
                st.error("Valor inválido. Digite um valor maior que zero.")
            elif valor_saque > saldo_atual:
                st.error("Erro: Saldo insuficiente.")
            elif valor_saque > limite_saque:
                st.error(f"Erro: O limite por saque é de R$ {limite_saque:.2f}.")
            else:
                st.session_state.saldos[st.session_state.usuario_atual] -= valor_saque
                st.session_state.historicos[st.session_state.usuario_atual].append(f"Saque: - R$ {valor_saque:.2f}")
                st.success(f"Saque de R$ {valor_saque:.2f} realizado!")

    elif operacao == "Depósito":
        valor_deposito = st.number_input("Digite o valor do depósito", min_value=0.0, step=10.0, format="%.2f")
        if st.button("Realizar depósito"):
            if valor_deposito <= 0:
                st.error("Valor inválido. Digite um valor maior que zero.")
            else:
                st.session_state.saldos[st.session_state.usuario_atual] += valor_deposito
                st.session_state.historicos[st.session_state.usuario_atual].append(f"Depósito: + R$ {valor_deposito:.2f}")
                st.success(f"Depósito de R$ {valor_deposito:.2f} realizado!")

    elif operacao == "Ver Histórico":
        historico_usuario = st.session_state.historicos[st.session_state.usuario_atual]
        if not historico_usuario:
            st.write("Nenhuma transação realizada.")
        else:
            st.write("HISTÓRICO")
            for operacao_texto in historico_usuario:
                st.write(f"- {operacao_texto}")

    elif operacao == "Sair":
        if st.button("Sair da conta"):
            logout()

    if st.session_state.mensagem:
        st.info(st.session_state.mensagem)
