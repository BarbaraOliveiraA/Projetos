#Programa de consumo de água
#Autor: Barbara Oliveira

while True:
    #Menu de opções
    print("--Consumo de água-- ")
    imovel = input("Informe o tipo de imovel a partir de uma das opções a seguir: \n1 - Apartamento \n2 - Casa \n3 - Comercial  \n")

    #Seleção de tipo de imovel
    match imovel:
        case "1" | "Apartamento" | "APARTAMENTO" :
            tipo_imovel = "Apartamento"
            break
        case "2" | "Casa" | "CASA":
            tipo_imovel = "Casa"
            break
        case "3" | "Comercial" | "COMERCIAL":
            tipo_imovel = "Comercial"
            break
        case _:
            print ("ATENÇÂO: Opção invalida. Tente novamente!")

while True:
    #Entrada e leitura de consumo

    consumo_m = float(input("Informe o consumo mensal de água em metros cúbicos (m³): "))
    if consumo_m <0:
        print ("Valor negativo não permitido. Tente novamente.")
    else:    
        print ("Valor informado valido.")
        break

#Mensagem para usuário após analise de dados inseridos
if tipo_imovel == "Comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo_imovel == "Apartamento" and consumo_m < 10:
    print ("Consumo econômico – excelente controle de água!")

elif (tipo_imovel == "Apartamento" or tipo_imovel == "Casa") and consumo_m <= 25:
    print ("Consumo moderado – dentro do padrão residencial.")

else:
    print ("Consumo excessivo – adote medidas de economia e verifique vazamentos.")