# Projeto Playlist de Música

> Projeto desenvolvido para a disciplina de **Estrutura de Dados** da **Fatec Rio Claro**.
 
O sistema permite gerenciar uma biblioteca pessoal de faixas, organizar músicas em filas de reprodução automáticas baseadas no "humor" (definido pelo BPM) e manter um histórico de reproduções.

## Estrutura do Projeto
```
├── main.py        # Menu e interação com o usuário
└── estrutura.py   # Classes de domínio e estruturas de dados
```

## Requisitos Técnicos
Todas as estruturas foram implementadas do zero com nós encadeados, **sem uso de `list`, `deque` ou qualquer estrutura built-in do Python.**

## Funcionalidades

O menu interativo oferece as seguintes operações:
| Opção | Descrição |
|-------|-----------|
| 1 | Adicionar música à biblioteca |
| 2 | Remover música pelo ID |
| 3 | Buscar música por ID ou Título |
| 4 | Listar toda a biblioteca |
| 5 | Montar filas de reprodução por humor |
| 6 | Reproduzir próxima música de uma fila |
| 7 | Exibir fila de humor sem remover |
| 8 | Exibir histórico de reproduções |
| 9 | Estatísticas gerais |
| 10 | Sair |

## Classificação por Humor (BPM)

As músicas são categorizadas automaticamente segundo os critérios:
- **Relaxar:** Até 80 BPM.
- **Focar:** 81 a 120 BPM.
- **Animar:** 121 a 160 BPM.
- **Treinar:** Acima de 160 BPM.

## Como Rodar
 
Pré-requisito: **Python 3.x**

1. **Clone o repositório**
```bash
git clone https://github.com/naumsarti/Projeto_Playlist.git
cd Projeto_Playlist
```

2. **Execute o script:**
```bash
python main.py
```
 
