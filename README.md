# Sistema de Transporte de Passageiros

Este é um sistema de gerenciamento de linhas de ônibus e reservas de assentos, implementado em Python. Ele permite o cadastro, alteração e remoção de rotas, a consulta de assentos em datas futuras e a geração de relatórios de ocupação e arrecadação.

| Detalhes do Projeto | |
| :--- | :--- |
| **Contribuintes** | Pedro Francisco Sousa Silva, Pedro Henrique Silva Costa |
| **Orientador** | Guido Pantuza |
| **Linguagem** | Python 3 |

---

## Funcionalidades Principais

O sistema é baseado em **Linhas** (rotas fixas) e **Ônibus** (instâncias de viagem para cada dia).

* **Cadastro Completo de Linhas:** Inserção, remoção e alteração de rotas com **Cidade de Origem**, **Cidade de Destino**, **Horário de Partida (HH:MM)** e **Valor da Passagem**.
* **Gestão de Frota:** Cada linha gera automaticamente ônibus para os **próximos 30 dias**, cada um com 20 assentos.
* **Consulta e Reserva de Assentos:** Permite ao usuário buscar viagens para uma cidade e realizar a reserva, verificando a disponibilidade em tempo real e gerando um **Comprovante de Reserva**.
* **Validação de Viagem:** O sistema garante que reservas sejam feitas apenas para datas futuras, dentro do limite de **30 dias** e respeitando o horário de partida no dia atual.
* **Relatórios Gerenciais:** Geração de relatórios de arrecadação total e **Matriz de Ocupação Média (%) por Dia da Semana**, com opção de saída no terminal ou em arquivo TXT.
* **Persistência de Reservas:** As reservas realizadas são salvas em **`reservas.txt`** e podem ser **carregadas** na inicialização do sistema através da opção de menu.

---

## Estrutura do Código (Módulos)

O projeto é modularizado para melhor organização e manutenção:

| Módulo | Responsabilidade |
| :--- | :--- |
| `main.py` | Loop principal do sistema e menu de navegação. |
| `modelo.py` | Contém as classes **`Linha`** e **`Onibus`**, que definem a estrutura de dados. |
| `linhas.py` | Funções de **CRUD** (Cadastro, Remoção, Alteração) e consulta de linhas. |
| `reservas.py` | Lógica de **leitura** de reservas (`reservas.txt`), registro de falhas e **aplicação** de novas reservas. |
| `relatorios.py` | Lógica para **gerar relatórios** e calcular a **Matriz de Ocupação** (média percentual por dia da semana). |
| `util.py` | Funções de uso geral: avisos na tela, limpeza de terminal e **validação de data/hora**. |

---

## Tecnologias e Dependências

O sistema utiliza exclusivamente bibliotecas nativas do Python:

* **`datetime` e `timedelta`:** Gestão de tempo, datas e o limite de 30 dias para as viagens.
* **`os` e `platform`:** Usadas para garantir a compatibilidade da limpeza de terminal (`cls` ou `clear`) em diferentes sistemas operacionais.
* **`time`:** Usada para criar pausas controladas e simular atrasos nos avisos.

---

## Como Executar

Para rodar o sistema, você precisa ter o **Python 3** instalado em sua máquina.

1.  **Baixe os Arquivos:** Certifique-se de que todos os arquivos do projeto (ex: `main.py`, `modelo.py`, `linhas.py`, etc.) estão no mesmo diretório.
2.  **Abra o Terminal:** Navegue até o diretório onde os arquivos estão salvos.
3.  **Execute:** Utilize o comando para rodar o script principal:

    ```bash
    python main.py
    ```

### Guia de Uso Rápido

O programa opera através de um menu interativo:

1.  **Comece em `[1] - Inserir linha`:** Crie as rotas (linhas) do sistema.
2.  **Utilize `[5] - Consultar horários e Assentos`:** Este é o fluxo de reserva. Após escolher a linha e a data, você será direcionado para a tela de assentos e poderá confirmar a reserva.
3.  **Use `[6] - Ler reservas no arquivo`:** Carrega as reservas salvas anteriormente em `reservas.txt`.
4.  **Finalize com `[7] - Gerar relatório`:** Obtenha as métricas de arrecadação e ocupação.
