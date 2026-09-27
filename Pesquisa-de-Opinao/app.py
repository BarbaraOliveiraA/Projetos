"""
Pesquisa de Satisfação de Atendimento.
Autor: Barbara Oliveira
"""
#Variaveis de contadores
excelente = 0
bom = 0
ruim = 0

#Cadastro dos clientes (100 clientes)
for i in range (1,11):
    nome = input(f"Informe o nome do {i}º cliente: ")
    idade = input(f"Informe a idade do {i}º cliente: " )

    #Menu de opções
    opiniao = int (input ("Informe sua opinião sobre o grau de satisfacao ao atendiemto: \n" 
                            "1 - Execelente \n"
                            "2 - Bom \n" 
                            "3 - Ruim \n"))

    #Repete a pergunta enquanto o valor digitado for diferente de 1, 2 e 3
    while opiniao != 1 and opiniao != 2 and opiniao != 3:
        print("Opção inválida! Digite apenas 1, 2 ou 3.\n")
        opiniao = int(input(
            "Informe sua opinião sobre o grau de satisfação com o atendimento:\n"
            "1 - Excelente\n"
            "2 - Bom\n"
            "3 - Ruim\n"))
        
    #Soma +1 a opção escolhida para a contagem final
    match opiniao:
        case 1:
            excelente +=1
        case 2:
            bom +=1
        case 3: 
            ruim+=1

#Exibição final do relatorio contendo o total de opiniões Excelente e Ruim
print ("---Relatorio final (Excelente e Ruim)---")
print ("Total de opiniões Excelente: ", excelente)
print ("Total de opiniões Ruim: ", ruim)