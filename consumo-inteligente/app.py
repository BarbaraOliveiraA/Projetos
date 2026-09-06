#Programa de cálculo de consumo elétrico
#Autor: Barbara de Oliveira

#Entrada de Dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
horasDia = float(input("Digite o tempo de uso diário (em horas): "))

#Processamento
consumo_mensal = (potencia * horasDia * 30) / 1000  # Consumo mensal em kWh
custo_estimado = consumo_mensal * 0.50  # Custo estimado em reais (considerando R$ 0,50 por kWh)

#Saída de Dados
print(f"\nAparelho: {aparelho}")   
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")
print(f"Custo estimado: R$ {custo_estimado:.2f}")