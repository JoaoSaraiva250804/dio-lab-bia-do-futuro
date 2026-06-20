import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL= “http://localhost:..... (5 numeros)/api/generate”
MODELO= “gpt-oss”

perfil = json.load(open(‘./data/perfil/investidor.json’))
transacoes = pd.read_csv(‘./data/transacoes.csv’)) 
historico = pd.read_csv(‘./data/historico_atendimento.csv’)) 
produtos = json.load(open(‘./data/produtos_financeiros.json’))

contexto = f “””
CLIENTE: {perfil [‘nome’]} {perfil [‘idade’]} anos, perfil {perfil [‘perfil investidor’]}
OBJETIVO: {perfil [‘objetivo_principal’]}
PATRIMÔNIO: R$ {perfil [‘patrimonio_total’]} | RESERVA: R$ {perfil[‘reserva_emergencia_atual’]}

TRANSAÇÕES RECENTES
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS
{json.dumps(produtos, indent=2, ensure_ascii=False)}
“””
SYSTEM_PROMPT = “””

“””

def perguntar(msg):
prompt = f “””
{SYSTEM_PROMPT }

CONTEXTO DO CLIENTE
{contexto}

Pergunta = {msg} “””

r = requests.post(OLLAMA_URL, json= {“model”: MODELO “prompt”: prompt “stream”: False})
return r.json()[‘response’]

st.title(“SophIA, Sua Agente Financeira ”)

if pergunta := st.chat_input(“Sua dúvida sobre finanças…)
st.chat_message(“user”).write(pergunta)
with st.spinner(“...”):
st.chat_message(“assistant”).write(perguntar(pergunta)
