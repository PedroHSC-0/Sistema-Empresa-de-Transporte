import os
import time
import platform

def aviso(mensagem, atraso=0.5):
    if platform.system().lower() == "windows":
        limpar = "cls"
    else:
        limpar = "clear"
    os.system(limpar)
    print(mensagem, end="", flush=True)
    for _ in range(3):
        time.sleep(atraso)
        print(".", end="", flush=True)

    time.sleep(atraso)
    os.system(limpar)

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
    
def consultar_horario(linhas_cadastradas):
    print("====Consulta de Horarios====")
        
    cidade = str(input("Para qual cidade voce quer ir?"))
    horario = str(input("Qual horario voce deseja consultar?"))
    
    for linha in linhas_cadastradas:
        if (linha.cidade_d == cidade and linha.horario_p == horario):
            print(f"O horario disponivel para a cidade {cidade} eh {linha.horario_p}")
            break
    else:
        print(f"Nenhuma linha encontrada para o destino {cidade} e nesse horario de {horario}")          
        
                
    """
    print("pessoa vai reservar pela linha e com isso vai receber as informações da passagem o numero do lugar e se é janela ou nao ")
        
    print("mostrando todos os horarios de todas as linhas possiveis")
        
    print("com isso a pessoa escolhe a linha e os outros dados e la ela compra a passagem")"""

def reservar_assento():
        pass

def consultar_assento(busao):
    print("====Conferindo Assentos Disponiveis====")
    
    cidade_d = str(input("Qual cidade de destino que voce ira viajar? "))
    horario = str(input("Qual o horario da sua viagem?"))
    data = str(input("Qual a data da sua viagem?"))
    
    #verificar 30 dias 
    
    #procurar onibus que correspondem as informações
    
    print("====Assentos Disponiveis====")
    livres = 0
    
    for i,ocupado in enumerate(busao.assento):#o i é o indice do assento e o ocupado é valor do assento 
        status = "Livre" if not ocupado else "Ocupado"# False,logo nao esta ocupado => Livre e True ,logo esta ocupado => Ocupado
        
        print(f"Assento {i+1}: {status}")#printando os assentos e seus status 
        
        if not ocupado:
            livres += 1#quantidade de assentos livres
            
    if livres == 0:
        print("\nNenhum assento disponível!")
        return
    
    resposta = int(input("Vai reservar assento(1-Sim/2-Nao)"))
    
    if resposta == 1:
        reservar_assento()

def ler_arquivo_reservas():
    pass
    
class linha:
    
    def __init__(self,cidade_d,cidade_o,horario_p,valor_p):
        self.cidade_d = cidade_d
        self.cidade_o= cidade_o
        self.horario_p = horario_p
        self.valor_p = valor_p

class onibus:
    
    def __init__(self,linha_b,data_p):
        self.linha = linha_b
        self.data_p = data_p
        self.assento = [False for i in range(20)]
