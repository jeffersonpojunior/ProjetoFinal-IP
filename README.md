# Runner Recife (nome em definição)

<!-- ![Captura de Tela do Jogo](assets/screenshot.png) Adicionar imagem depois -->

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

/nomedojogo
│── assets/ # Imagens, sons e fontes utilizadas no jogo
│── src/ # Código-fonte principal
│ │── main.py # Arquivo principal que inicia o jogo
│ │── player.py # Classe do jogador com física e movimentação
│ │── obstacles.py # Geração procedural de obstáculos
│ │── items.py # Itens coletáveis com efeitos especiais
│ │── config.py # Configurações globais (resolução, FPS, etc)
│ │── game.py # Lógica principal do jogo (estados, loop principal)
│ │── menu.py # Menus e interface do usuário
│── docs/ # Documentação e relatórios
│── README.md # Este arquivo


## 🛠️ Ferramentas e Tecnologias

- **Pygame**: Biblioteca principal para desenvolvimento do jogo
- **Python 3.10+**: Versão do Python utilizada
- **Tiled**: Editor de mapas para criação de cenários (opcional)
- **Aseprite**: Editor de sprites (opcional)

## 👥 Divisão de Trabalho

| Membro               | Responsabilidades                          |
|----------------------|-------------------------------------------|
| Leonardo Ibiapina    | Implementação do player e movimentação    |
| Beatrice Litssa      | Obstáculos e lógica de colisão            |
| Jefferson Pereira    | Itens coletáveis e ajustes de dificuldade |
| Artur Bezerra        | Interface gráfica e sprites               |
| Luiz Felipe Barros   | Design de UI/UX e assets visuais          |
| Matheus Enrico       | Documentação e apresentação               |

## 📚 Conceitos Aplicados

### Programação Orientada a Objetos
- Classes bem definidas para Player, Obstacle, Item
- Herança de `pygame.sprite.Sprite`
- Encapsulamento de propriedades físicas

### Estruturas de Dados
- Listas para gerenciamento de sprites
- Dicionários para configurações do jogo
- Filas para geração procedural de obstáculos

### Padrões de Projeto
- 

## 🎮 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/ibiapleo/aprendendo-pygame.git
```
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Rode o jogo:
```bash
python src/main.py
```
