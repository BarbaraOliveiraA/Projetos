# Sistema de Classificação de Consumo de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## Sobre o Projeto

O projeto desenvolvido em Python tem como objetivo classificar o perfil de consumo de água de um imóvel e informar sobre seu consumo. O programa solicita o tipo de imóvel (Apartamento, Casa ou Comercial) e o consumo mensal em metros cúbicos (m³). Em seguida, valida as informações e aplica as regras de negócio de saneamento, exibindo a classificação e a mensagem correspondente ao usuário.

---

## Tecnologias Utilizadas

* Python — Linguagem principal do projeto.
* Estruturas de Repetição (while True) — Para validação contínua de dados.
* Estruturas de Decisão (match-case e if/elif/else) — Para seleção de opções e aplicação das regras de negócio.

---

##  Regras o e Classificação

| Tipo de Imóvel | Faixa de Consumo ($m^3$) | Mensagem Exibida|
| :--- | :--- | :--- |
| Comercial              | Qualquer valor      | Tarifa comercial aplicada – consulte o plano corporativo. |
| Apartamento            | Menor que 10\,m³    | Consumo econômico – excelente controle de água! |
| Apartamento / Casa     | Até 25\,³           | Consumo moderado – dentro do padrão residencial. |
| Outros casos           | Acima de 25\,m³     | Consumo excessivo – adote medidas de economia e verifique vazamentos.|

---

##  Como Rodar o Programa

### Pré-requisitos
Ter o Python 3.10 ou superior instalado em sua máquina.

### Passos para Execução
1. Baixe os arquivos do projeto para o seu computador.
2. Abra o arquivo do código no seu editor (como o VS Code).
3. Execute o codigo no seu editor.