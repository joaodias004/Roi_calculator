import plotly.express as px
import plotly.graph_objects as go
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
    total_custos = st.number_input("Qual foi o custo total do empreendimento?", format="%.2f")
    total_lucro = st.number_input("Qual foi o lucro total?", format="%.2f")
except:
    st.write(f"Por favor, insira um número")
    
if st.button("Calcular"):
    if total_custos and total_lucro:
        total_custos = float(total_custos)
        total_lucro = float(total_lucro)

        lucro = round(calculando_lucro(), 2)
        roi = round(calculando_ROI(), 2)

        st.write(f"O lucro total foi de: R${lucro}")
        st.write(f"O ROI de seu empreendimento foi: {roi}%")

        # Criando uma dashboard
        fig = go.Figure(go.Waterfall(
            name = "20", orientation = "v",
            measure = ["relative","relative", "total"],
            x = ["Vendas", "Gastos", "Lucro"],
            textposition = "outside",
            text = [f"+{total_lucro:.2f}", f"-{total_custos:.2f}", f"{lucro:.2f}"],
            y = [total_lucro, -total_custos, lucro],
            connector = {"line":{"color":"rgb(63, 63, 63)"}}
        ))

        fig.update_layout(
            title = f"Profit and Loss Statement (ROI: {roi:.2f}%)",
            showlegend = True
        )

        fig.update_layout(
                    title = "Profit and loss",
                    showlegend = True
                )

        st.plotly_chart(fig)

# Adicionando um divisor 
st.markdown("---")