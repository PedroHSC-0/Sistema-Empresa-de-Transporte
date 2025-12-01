from datetime import datetime, timedelta
from util import aviso


# Função pra gerar relatório       
def gerar_relatorio(linhas_cadastradas):
    """Funcao que gera o relatorio com opcao terminal ou txt"""
    
    menu2 = """
|--------------------------------|
| Como deseja gerar o relatório? |
|                                |
|-> [1] Terminal                 |
|-> [2] Arquivo de texto         |
|                                |
|--------------------------------|

"""
    tempo_agora = datetime.now()
    mensagem = ""

    # Escolha do formato
    while True:
        try:
            opcao = int(input(menu2))

            if opcao != "" and (opcao == 1 or opcao == 2): break

        except:
            aviso("Digite um valor válido")

    # Coleta de dados do relatório:
    # Valor arrecadado

    valor_arrecadado = 0
    for linha in linhas_cadastradas.values(): 
        valor_arrecadado = 0
        for onibus in linha.onibus:
            for assento in onibus.assentos:
                if assento == True:
                    valor_arrecadado = valor_arrecadado + linha.valor
        else:
            valor_formatado = f"R${valor_arrecadado:,.2f}".replace(".", ",")
            mensagem = mensagem + f"| {linha.id}-) {linha.cidade_o} -> {linha.cidade_d} | Valor arrecadado: {valor_formatado}"

    parte1 = f"""
|=============================================================|
| Relatório gerado em {tempo_agora.day}/{tempo_agora.month}/{tempo_agora.year} {tempo_agora.hour}:{tempo_agora.minute}:{tempo_agora.second}
|
| Valor arrecadado pelas linhas registradas:
|"""
    parte2 = """
|=============================================================|\n"""

    relatorio_final = parte1 + mensagem + parte2

    # --------------------------
    # 2. MATRIZ DE OCUPAÇÃO
    # --------------------------
    matriz = matriz_ocupacao(linhas_cadastradas)
    texto_matriz = formatar_matriz(matriz)

    relatorio_final += texto_matriz + "\n"

    # --------------------------
    # 3. SAÍDA FINAL
    # --------------------------

    if opcao == 1:
        print(relatorio_final)

    elif opcao == 2:
        try:
            with open("relatorios.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(relatorio_final)
            print("Relatório salvo com sucesso!")
        except Exception as e:
            print("Erro ao salvar relatório:", e)
            
            

        
def matriz_ocupacao(linhas_cadastradas):
    """Organizando as informações da matriz de ocupação"""
    dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

    matriz = []  

    for linha in linhas_cadastradas.values():
        # Para armazenar soma e quantidade de ônibus por dia
        soma_ocupacao = [0] * 7
        quantidade_onibus = [0] * 7

        for bus in linha.onibus:
        
            dia_semana = datetime.strptime(bus.data_p, "%d/%m/%Y").weekday()

            ocupados = sum(bus.assentos)# bus.assentos é uma lista de booleanos [True, False, ...]. sum() conta os True's (assentos ocupados)

            #sendo atualizadas soma e quantidade
            soma_ocupacao[dia_semana] += ocupados
            quantidade_onibus[dia_semana] += 1

        # Agora calcular percentual
        percentuais = []
        for i in range(7):
            if quantidade_onibus[i] == 0:
                percentuais.append(0.0)# 0% se não houve viagem naquele dia
            else:
                media = soma_ocupacao[i] / (quantidade_onibus[i] * 20)
                percentuais.append(round(media * 100, 2))

        # Montar linha da matriz
        matriz.append([linha.id, *percentuais])

    return matriz




def formatar_matriz(matriz):
    """Organizando a forma que a matriz sera imprimida"""
    dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

    texto = "\nMatriz de Ocupação Média (%) por Dia da Semana:\n"
    texto += "Linha | " + " | ".join(dias) + "\n"
    texto += "-" * 70 + "\n"

    for row in matriz:
        id_linha = str(row[0]).ljust(5)
        valores = " | ".join([f"{v:.2f}%".ljust(6) for v in row[1:]])
        texto += f"{id_linha} | {valores}\n"

    return texto
