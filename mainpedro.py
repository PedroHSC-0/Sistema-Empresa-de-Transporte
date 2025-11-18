import funcoes
import time

def cadastrar_linha():
            print("====Cadastro de Linha====")
            
            cidade_d = input("Qual a cidade de destino da sua linha?")
            cidade_o = input("Qual a cidade de origem da sua linha?")
            horario_p = input("Qual o horario de partida da sua linha?")
            valor_p = input("Qual o valor da passagem da sua linha?")
            
            nova_linha = linha(cidade_d, cidade_o, horario_p, valor_p)
            
            return nova_linha

def remover_linha():
    print("====Remoção De Linha====")
    
def alterar_linha():
    print("====Alteração de Linha====")
    
class linha:
    
    def __init__(self,cidade_d,cidade_o,horario_p,valor_p):
        self.cidade_d = cidade_d
        self.cidade_o= cidade_o
        self.horario_p = horario_p
        self.valor_p = valor_p
        
            
        def consultar_horario(self):
            print("====Consulta de Horarios====")
            
            cidade = str(input("Para qual cidade voce quer ir?"))
            
            for i in linhas_cadastradas:
                if cidade == self.cidade_d:
                    print("Os horarios disponiveis para esta cidade sao")            
                   
            print("pessoa vai reservar pela linha e com isso vai receber as informações da passagem o numero do lugar e se é janela ou nao ")
            
            print("mostrando todos os horarios de todas as linhas possiveis")
            
            print("com isso a pessoa escolhe a linha e os outros dados e la ela compra a passagem")

        def reservar_assento():
            pass

        def consultar_assento():
            print("infomar cidade destino")
            print("horario e data e data tem que ser inferior a 30 dias contados do dia atual")
            
            resposta = input(int("Vai reservar assento(1-Sim/2-Nao)"))
            
            if resposta ==1 :
                reservar_assento()

        
    
    
        def ler_arquivo_reservas():
            pass


"""
Linhas:
-Cidade de Origem
-Cidade de Destino
-Horário de partida (hora:minuto)
-Valor da passagem

Onibus:
-Data da partida (dia/mês/ano)
-Assentos disponíveis
"""


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

linhas_cadastradas.append(cadastrar_linha)


opcao = 0
while True:
    
    match opcao:
        case 1:
            cadastrar_linha()
        case 2:
            remover_linha()
        case 3:
            alterar_linha()
        case _:
            print("DIgite uma opcao valida")
    
    
    break
