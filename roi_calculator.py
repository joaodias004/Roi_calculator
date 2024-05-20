#Calculando retorno no investimento!
def calculando_lucro():
    lucro = total_lucro - total_custos
    return lucro

def calculando_ROI():
    roi = (total_lucro - total_custos) / total_custos * 100
    return roi

try:
    total_custos = float(input("Qual foi o custo total do empreendimento?" ))
    total_lucro = float(input("Qual foi o lucro total?" ))
except:
    print("Por favor, insira apenas valores númericos.")
    exit()

lucro = round(calculando_lucro(), 2)
roi = round(calculando_ROI(), 2)

calculando_lucro()
calculando_ROI()


print(f"O lucro total foi de: R${lucro}")
print(f"o ROI de seu empreendimento foi: {roi}%")