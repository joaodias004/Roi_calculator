import plotly.express as px
#Calculando retorno no investimento!
import streamlit as st

def calculando_lucro():
    lucro = total_lucro - total_custos
    return lucro

def calculando_ROI():
    roi = (total_lucro - total_custos) / total_custos * 100
    return roi

st.title("Calculadora de ROI")

try:
    total_custos = float(input("Qual foi o custo total do empreendimento?" ))
    total_lucro = float(input("Qual foi o lucro total?" ))
except:
    print("Por favor, insira apenas valores númericos.")
    exit()

if st.button("Calcular"):
    lucro = round(calculando_lucro(total_custos, total_lucro), 2)
    roi = round(calculando_ROI(total_custos, total_lucro), 2)

    st.write(f"O lucro total foi de: R${lucro}")
    st.write(f"O ROI de seu empreendimento foi: {roi}%")

    # Create a chart to display the ROI
    fig = px.bar(x=["ROI"], y=[roi])
    st.plotly_chart(fig)
    st.write(f"Para acessar o app em um navegador, use a URL: http://localhost:8501")

st.experimental_server.start(port=8501)