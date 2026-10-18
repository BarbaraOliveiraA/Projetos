from colorama import Fore, Style

#Função para retornar situação do nivel informado
def nivel_do_reservatorio(nivel):
    if nivel == "Nível 1":
        return "Muito Baixo (crítico)"
    elif nivel == "Nível 2":
        return "Baixo"
    elif nivel == "Nível 3":
        return "Médio"
    elif nivel == "Nível 4":
        return "Alto"
    elif nivel == "Nível 5":
        return "Muito alto (alerta)"

#Função para retornar a mensagem de acordo com a cor definida para o nivel inforamdo 
def cor_alerta(situacao):
    if situacao == "Muito Baixo (crítico)":
        print(Fore.RED + situacao + Style.RESET_ALL)
    elif situacao == "Baixo":
        print(Fore.YELLOW + situacao + Style.RESET_ALL)
    elif situacao == "Médio":
        print(Fore.GREEN + situacao + Style.RESET_ALL)
    elif situacao == "Alto":
        print(Fore.CYAN + situacao + Style.RESET_ALL)
    elif situacao == "Muito alto (alerta)":
        print(Fore.BLUE + situacao + Style.RESET_ALL)

# 1. Lista dos níveis do reservatório
niveis_reservatorio = [
    "Nível 1",  
    "Nível 2",  
    "Nível 3",  
    "Nível 4",  
    "Nível 5"   
]

# Escolha qual nível deseja testar [De 0 a 4]
nivel_atual = niveis_reservatorio[4]  

# Roda as funções e mostra o resultado na tela
situacao_atual = nivel_do_reservatorio(nivel_atual)
cor_alerta(situacao_atual)