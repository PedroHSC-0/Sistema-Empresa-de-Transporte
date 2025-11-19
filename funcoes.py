import os
import time
import platform
from datetime import datetime, timedelta

# A classe linha possibilita que seja criada várias instâncias e que sejam guardadas em um lista de objetos do tipo Linha
# A classe tem o metodo adicionar onibus, ele gera uma lista de onibus vazios com datas de hoje até 30 dias adiante
class Linha:

    def __init__(self, id_linha, cidade_o, cidade_d, horario_p, valor):
        self.id = id_linha
        self.cidade_o = cidade_o
        self.cidade_d = cidade_d
        self.horario_p = horario_p
        self.valor = valor
        self.onibus = []

    def adicionar_onibus(self):
        hoje = datetime.today()

        for i in range(30):
            dia = (hoje + timedelta(days=i)).strftime("%d/%m/%Y")
            self.onibus.append(Onibus(dia))

# Classe para o objeto Onibus ser guardado dentro da lista de Onibus
class Onibus:
    def __init__(self, data_p):
        self.data_p = data_p
        self.assento = [True for i in range(20)]

    # Função que verifica se há assentos disponiveis dentro do ônibus
    def possui_assento_disponivel(self):
        if True in self.assento: return True
        return False

# Função para gerar avisos diversos
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

# Função que cadastra uma nova linha, pedindo todos atributos para gerar uma nova instância da classe linha e armazená-la na lista "linhas_cadastradas"
# FUNCIONAL
def cadastrar_linha(linhas_cadastradas):

    print("====Cadastro de Linha====")
    id_linha = len(linhas_cadastradas) + 1

    # Input de Dados
    while True:
        cidade_origem = str(input("Qual a cidade de origem da sua linha?"))
        if not cidade_origem:
            aviso("Entrada vazia")
            continue

        cidade_destino = str(input("Qual a cidade de destino da sua linha?"))
        if not cidade_destino:
            aviso("Entrada vazia")
            continue

        horario_partida = input("Qual o horário de partida da sua linha?")
        if not horario_partida:
            aviso("Entrada vazia")
            continue
        try:
            valor = float(input("Qual o valor da passagem da sua linha?"))
        except ValueError:
            aviso("Entrada inválida")
            continue

        break

    # Gerando instância
    nova_linha = Linha(id_linha, cidade_origem, cidade_destino, horario_partida, valor)
    nova_linha.adicionar_onibus()
    linhas_cadastradas.append(nova_linha)

# Função que mostra todas as linhas e suas informações
def mostrar_linhas(linhas_cadastradas):
    print("----------------------------")
    for linha in linhas_cadastradas:
        valor_formatado = f"R${linha.valor:,.2f}".replace(".", ",")
        print(f"{linha.id}-) {linha.cidade_o} -> {linha.cidade_d}\n    Horário: {linha.horario_p}| Valor: {valor_formatado}")
        print("----------------------------")

# Função para remover uma linha do sistema através do ID dado
def remover_linha(linhas_cadastradas):
    while True:
        print("====Remoção De Linha====")

        try:
            id_linha = int(input("Insira o ID da linha a ser removida: "))

        except ValueError:
            aviso("Insira um valor válido")
            continue

        for linha in linhas_cadastradas:
            if id_linha == linha.id:
                linhas_cadastradas.remove(linha)
                break
        else:
            print("O id não pertence a nenhuma linha registrada")
    
def alterar_linha(linhas_cadastradas):
    print("====Alteração de Linha====")

    return linhas_cadastradas
    
def consultar_horario(linhas_cadastradas):
    print("====Consulta de Horarios====")
        
    cidade = str(input("Para qual cidade voce quer ir?"))
    horario = str(input("Qual horario voce deseja consultar?"))
    
    for linha in linhas_cadastradas:
        if linha.cidade_d == cidade and linha.horario_p == horario:
            print(f"O horario disponivel para a cidade {cidade} é {linha.horario_p}")
            break
    else:
        print(f"Nenhuma linha encontrada para o destino {cidade} e nesse horario de {horario}")          

    """
    print("pessoa vai reservar pela linha e com isso vai receber as informações da passagem o numero do lugar e se é janela ou nao ")
        
    print("mostrando todos os horarios de todas as linhas possiveis")
        
    print("com isso a pessoa escolhe a linha e os outros dados e la ela compra a passagem")"""

def reservar_assento(linhas_cadastradas):
    pass

def consultar_assento(linhas_cadastradas, busao):
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
        reservar_assento(linhas_cadastradas)

def ler_arquivo_reservas():
    pass
