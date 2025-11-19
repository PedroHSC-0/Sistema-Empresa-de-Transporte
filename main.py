import time
from funcoes import aviso, cadastrar_linha, remover_linha, alterar_linha, consultar_horario, reservar_assento, consultar_assento, ler_arquivo_reservas, linha, onibus

menu = """
|-------------SISTEMA DE TRANSPORTE DE PASSAGEIROS-------------|
|                                                              |
|  [1] - Inserir linha                                         |     
|  [2] - Remover linha                                         |
|  [3] - Alterar linha                                         |
|  [4] - Consultar horários                                    |
|  [5] - Sair                                                  |
|                                                              |
|--------------------------------------------------------------|
"""

# MAIN

linhas_cadastradas = []

viagem_marcadas = []

linha_teste = linha("Sao Paulo", "Campinas", "14:30", "55.00")

linhas_cadastradas.append(linha_teste)

busao = onibus(linha_b = linha_teste,data_p="10/10/2025")

viagem_marcadas.append(busao)


opcao = 0
while True:

    print(menu)
    try: 
        opcao = int(input())
    except:
        aviso("Tipo inválido de entrada")

    match opcao:
        case 1:
            cadastrar_linha()
        case 2:
            remover_linha()
        case 3:
            alterar_linha()
        case 4:
            consultar_horario()
        case 5:
            aviso("Saindo")
            break
        case _:
            print("DIgite uma opcao valida")
    
    
    break
