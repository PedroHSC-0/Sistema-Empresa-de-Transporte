import time
from funcoes import aviso, cadastrar_linha, remover_linha, alterar_linha, mostrar_linhas, consultar_horario, consultar_assento, ler_arquivo_reservas, gerar_relatorio

menu = """
|-------------SISTEMA DE TRANSPORTE DE PASSAGEIROS-------------|
|                                                              |
|  [1] - Inserir linha                                         |     
|  [2] - Remover linha                                         |
|  [3] - Alterar linha                                         |
|  [4] - Mostrar linhas                                        |
|  [5] - Consultar horários                                    |
|  [6] - Consultar Assentos                                    |
|  [7] - Ler reservas no arquivo                               |
|  [8] - Gerar relatório                                       |
|  [9] - Sair                                                  |
|                                                              |
|--------------------------------------------------------------|
"""

# MAIN


linhas_cadastradas = []

ler_arquivo_reservas(linhas_cadastradas)

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
            continue

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
            consultar_assento(linhas_cadastradas)
        case 7:
            ler_arquivo_reservas(linhas_cadastradas)
            aviso("", atraso=0.1)
        case 8:
            gerar_relatorio(linhas_cadastradas)
        case 9:
            aviso("Saindo", atraso=0.6)
            break
        case _:
            aviso("Digite uma opção válida", atraso=0.6)
    
