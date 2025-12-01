
from linhas import (
    cadastrar_linha, mostrar_linhas, remover_linha,
    alterar_linha, consultar_horario
)

from reservas import ler_arquivo_reservas
from relatorios import gerar_relatorio
from util import aviso



menu = """
|-------------SISTEMA DE TRANSPORTE DE PASSAGEIROS-------------|
|                                                              |
|  [1] - Inserir linha                                         |     
|  [2] - Remover linha                                         |
|  [3] - Alterar linha                                         |
|  [4] - Mostrar linhas                                        |
|  [5] - Consultar horários e Assentos                         |
|  [6] - Ler reservas no arquivo                               |
|  [7] - Gerar relatório                                       |
|  [8] - Sair                                                  |
|                                                              |
|--------------------------------------------------------------|
"""

# MAIN


linhas_cadastradas = {}

opcao = 0
aviso("Iniciando Sistema", atraso=0.4)
while True:
    print(menu)
    while True:
        try:
            opcao = input()
            if opcao:
                opcao = int(opcao)
                break
        except:
            aviso("Tipo inválido de entrada")
            break

    match opcao:
        case 1:
            cadastrar_linha(linhas_cadastradas)
            aviso("Linha cadastrada com sucesso")
        case 2:
            remover_linha(linhas_cadastradas)
            aviso("Linha removida com sucesso")
        case 3:
            alterar_linha(linhas_cadastradas)
            aviso("Linha alterada com sucesso")
        case 4:
            mostrar_linhas(linhas_cadastradas)
        case 5:
            consultar_horario(linhas_cadastradas)
        case 6:
            ler_arquivo_reservas(linhas_cadastradas)
            aviso("", atraso=0.1)
        case 7:
            gerar_relatorio(linhas_cadastradas)
        case 8:
            aviso("Saindo", atraso=0.6)
            break
        case _:
            aviso("Digite uma opção válida", atraso=0.6)
    