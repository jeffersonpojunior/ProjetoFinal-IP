# ReciRunner

Um jogo de corrida infinita com temática pernambucana desenvolvido em Pygame.

## 🧑‍💻 Membros da Equipe

- Luiz Felipe Barros <lfpab>
- Jefferson Pereira <jpoj>
- Leonardo Ibiapina <ljoi>
- Artur Bezerra <abs11>
- Matheus Enrico <mecsb>
- Beatrice Litssa <blqp>

## 🏗️ Arquitetura do Projeto

O projeto foi desenvolvido utilizando a biblioteca Pygame e segue uma estrutura modular para facilitar a manutenção e evolução do código.

- `nomedojogo/`
  - `assets/` → Imagens, sons e fontes utilizadas no jogo
  - `src/` → Código-fonte principal
    - `main.py` → Arquivo principal que inicia o jogo
    - `player.py` → Classe responsável pelo controle do jogador
    - `obstacles.py` → Classe para os obstáculos
    - `collectables.py` → Classe para os coletáveis
    - `config.py` → Configurações globais (resolução, FPS, etc)
    - `level.py` → Classe para criação do mapa principal
  - `docs/` → Documentação e relatórios
  - `README.md` → Este arquivo

## Capturas de Tela

![Captura do Menu Principal](assets/MENU.jpg)
![Captura do Jogo 1](assets/INGAME_1.jpg)
![Captura do Jogo 2](assets/INGAME_2.jpg)
![Captura do Game Over](assets/GAME_OVER.jpg)

## 🛠️ Ferramentas e Tecnologias

- **Pygame**: Biblioteca principal para desenvolvimento do jogo
- **Random**: Utilizado para gerar de forma aleatória os coletáveis, obstáculos e outros objetos do jogo.

## Divisão de Trabalho
- **[Leonardo Ibiapina]**: Implementação do player e movimentação, e criação da base do relatório
- **[Beatrice]**: Desenvolvimento dos obstáculos e lógica de colisão.
- **[Jefferson Pereira]**: Implementação dos itens coletáveis e ajustes de dificuldade.
- **[Artur Bezerra, Luiz Felipe Barros]**: Implementação de interface do jogo (sprites, etc).
- **[Matheus Enrico]**: Slides, apresentação e finalização do relatório.

## Conceitos Aplicados da Disciplina
- **Programação Orientada a Objetos**: Utilizada na organização do código, separando lógicas em classes como Player, Obstacle e Item.
- **Estruturas de Dados**: Listas para armazenar e gerenciar múltiplos obstáculos e itens simultaneamente.
- **Condicionais**: Utilizados para comparar valores dentro do jogo.
- **Laços de repetição**: Usados para gerar automações repetitivas dentro do jogo.

## Desafios e Erros Enfrentados
- Aprender a utilizar a ferramenta pygame
- Aprender e aplicar POO
- Organização do tempo para desenvolvimento
- Versionamento de código 

## 🎮 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/ibiapleo/aprendendo-pygame.git
```
2. Instale as dependências:
```bash
pip install pygame
```
3. Rode o jogo:
```bash
python src/main.py
```
