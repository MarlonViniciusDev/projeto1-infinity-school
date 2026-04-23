import streamlit as st
import requests

historico = []

def buscar_cotacao(moeda_base, moeda_destino):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_base}-{moeda_destino}"
    resposta = requests.get(url)
    dados = resposta.json()
    chave = moeda_base + moeda_destino
    return float(dados[chave]['bid'])

def converter(valor, cotacao):
    return valor * cotacao

def registrar_historico(moeda, valor, resultado):
    historico.append({"moeda": moeda, "valor": valor, "resultado": resultado})

st.title("💱 Mini Conversor de Moedas")

moeda_base = st.text_input("Moeda base (ex: USD):", "USD").upper()
moeda_destino = st.text_input("Moeda destino (ex: BRL):", "BRL").upper()
valor = st.number_input("Valor para converter:", min_value=1.0, value=10.0)

if st.button("Converter"):
    cotacao = buscar_cotacao(moeda_base, moeda_destino)
    resultado = converter(valor, cotacao)
    registrar_historico(f"{moeda_base}-{moeda_destino}", valor, resultado)
    st.success(f"{valor} {moeda_base} valem {resultado:.2f} {moeda_destino}")

    st.markdown("---")
    st.subheader("Histórico de conversões")
    st.table(historico)