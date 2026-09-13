"""
Desconto progessivo de uma loja online
Autor: Barbara Oliveira
"""
# Entrada de dados
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Validação para informar sobre valores negativos serem inválidos
if valor_compra < 0:
    print("Erro: O valor da compra não pode ser menor que zero (0).")
else:
    # Definição do percentual de desconto
    if valor_compra < 200.0:
        pct_desconto = 0.05 
        #pct = abreviação de porcentagem
    elif valor_compra < 300.0:
        pct_desconto = 0.10
    else:
       pct_desconto = 0.15

# Processamento dos dados
valor_desconto = valor_compra * pct_desconto
valor_final = valor_compra - valor_desconto
porcentagem = int(pct_desconto * 100)

#Exibição dos valores
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f} ({porcentagem}%)")
print(f"Valor total a pagar: R$ {valor_final:.2f}")