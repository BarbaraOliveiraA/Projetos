# Cálculo de Consumo de Energia
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
---
Sobre o Projeto

O projeto desenvolvido em Python tem como objetivo auxiliar os usuários no monitoramento de gastos elétricos residenciais. O programa solicita o nome do aparelho, sua potência e o tempo diário de uso. Em seguida, calcula o consumo mensal e o custo estimado, exibindo os resultados finais ao usuário.

---

Fórmulas Utilizadas

O programa realiza apenas dois cálculos simples:

1. **Consumo mensal (kWh):** Multiplica a potência do aparelho pelas horas de uso diário e pelos 30 dias do mês, dividindo tudo por 1000. 
   (potencia * horasDia * 30) / 1000
2. **Custo estimado (R$):** Multiplica o consumo mensal encontrado pelo valor da tarifa de energia por kWh.
   consumo_mensal * 0.50 (considerando R$ 0,50 por kWh)

---

Como Rodar o Programa

1. Baixe os arquivos do projeto para o seu computador.
2. Abra o arquivo do código no seu editor (como o VS Code).
3. Execute o codigo no seu editor.