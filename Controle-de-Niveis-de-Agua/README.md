# Controle de Níveis de Água
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## Sobre o Projeto
O projeto desenvolvido em Python tem como objetivo exibir mensagens de alerta com cores diferentes de acordo com o nível de água do reservatório escolhido. O programa analisa o nível do reservatório selecionado, logo em seguida esse nível será analisado na função `nivel_do_reservatorio` para retornar a situação, e logo depois essa situação passará na função `cor_alerta` para definir a cor de acordo com a progressão de risco.

---

# Níveis de progressão de risco

| Nível | Situação | Cor / Código Hex |
| :--- | :--- | :--- |
| Nível 1 | Muito Baixo (crítico) | `#FF0000` 🟥 Vermelho |
| Nível 2 | Baixo                 | `#FFFF00` 🟨 Amarelo |
| Nível 3 | Médio                 | `#00FF00` 🟩 Verde |
| Nível 4 | Alto                  | `#00FFFF` 🟦 Ciano |
| Nível 5 | Muito Alto (alerta)   | `#0000FF` 🟦 Azul |

---

## Como Rodar o Programa

1. Baixe os arquivos do projeto para o seu computador.
2. Abra a pasta do projeto no seu editor (como o VS Code).
3. Verifique se a biblioteca Colorama está instalada no seu editor
4. Execute o codigo no seu editor.