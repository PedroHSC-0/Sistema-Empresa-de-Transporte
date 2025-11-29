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
        self.assentos = [False for i in range(20)]

    # Função que verifica se há assentos disponiveis dentro do ônibus
    def possui_assento_disponivel(self):
        if True in self.assentos: return True
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

# Função que cadastra uma nova linha, pedindo todos atributos para gerar uma nova instância da classe linha e armazená-la na lista "linhas_cadastradas". Funcionando
def cadastrar_linha(linhas_cadastradas):

    id_linha = 1

    while True:
        for linha in linhas_cadastradas:
            if linha.id == id_linha:
                id_linha = id_linha + 1
                continue
        break

    print("|========Cadastro de Linha========|\n")



    # Input de Dados
    while True:
        cidade_origem = str(input("Qual a cidade de origem da sua linha? "))
        if not cidade_origem:
            aviso("Entrada vazia")
            continue
        cidade_origem.strip()

        cidade_destino = str(input("Qual a cidade de destino da sua linha? "))
        if not cidade_destino:
            aviso("Entrada vazia")
            continue
        cidade_destino.strip()

        horario_partida = input("Qual o horário de partida da sua linha? ")
        if not horario_partida:
            aviso("Entrada vazia")
            continue
        try:
            valor = float(input("Qual o valor da passagem da sua linha? "))
            if valor < 0:
                aviso("Valor inválido")

        except ValueError:
            aviso("Entrada inválida")
            continue


        break

    # Gerando instância
    nova_linha = Linha(id_linha, cidade_origem, cidade_destino, horario_partida, valor)
    nova_linha.adicionar_onibus()
    linhas_cadastradas.append(nova_linha)

# Função que mostra todas as linhas e suas informações. Funcionando
def mostrar_linhas(linhas_cadastradas, todas=True, id_mostrar=None):
    if todas:
        if linhas_cadastradas:

            print("|--------------------------------------")
            for linha in linhas_cadastradas:
                valor_formatado = f"R${linha.valor:,.2f}".replace(".", ",")
                print(f"{linha.id}-) {linha.cidade_o} -> {linha.cidade_d}\n    Horário: {linha.horario_p} | Valor: {valor_formatado}")
                print("|--------------------------------------")
        else:
            aviso("Não há linhas cadastradas")

    else:
        for linha in linhas_cadastradas:
            if linha.id == id_mostrar:
                print("|--------------------------------------")
                valor_formatado = f"R${linha.valor:,.2f}".replace(".", ",")
                print(f"{linha.id}-) {linha.cidade_o} -> {linha.cidade_d}\n    Horário: {linha.horario_p} | Valor: {valor_formatado}")
                break

# Função para remover uma linha do sistema através do ID dado. Funcionando
def remover_linha(linhas_cadastradas):
    while True:
        print("|========Remoção De Linha========|")

        try:
            id_remover = int(input("Insira o ID da linha a ser removida: "))
            for linha in linhas_cadastradas:
                if id_remover == linha.id:
                    linhas_cadastradas.remove(linha)
                    break
            else:
                print("O id não pertence a nenhuma linha registrada")
                break
        except ValueError:
            aviso("Insira um valor válido")
            continue
        break

# Função para alterar dados da linha (Cidade Destino e horários). Funcionando
def alterar_linha(linhas_cadastradas):
    print("|========Alteração de Linha========|")
    
    loop = True

    while loop:
        try: 
            id_linha = int(input("Insira o id da linha a ser alterada: "))

        except:
            aviso("Valor inválido")

        for linha in linhas_cadastradas:
            if linha.id == id_linha:
                try:
                    mostrar_linhas(linhas_cadastradas, todas=False, id_mostrar=id_linha)
                    opcao = int(input("""
|-------------------------Alterar Linha------------------------|
|                                                              |
|  [1] - Alterar cidade de origem                              |     
|  [2] - Alterar cidade de destino                             |
|  [3] - Alterar horário de partida                            |
|  [4] - Alterar valor da passagem                             |
|  [5] - Voltar para o menu principal                          |
|                                                              |
|--------------------------------------------------------------|
"""))           
                except:
                    aviso("Valor inválido")

                if opcao == 1:
                    cidade_origem = str(input())
                    if cidade_origem == "":
                        aviso("Insira algum valor")
                        continue
                    linha.cidade_o = cidade_origem
                    loop = False
                    break
                    
                elif opcao == 2:
                    cidade_destino = str(input())
                    if cidade_destino == "":
                        aviso("Insira algum valor")
                        continue
                    linha.cidade_d = cidade_destino
                    loop = False
                    break

                elif opcao == 3:
                    horario_partida = str(input())
                    if horario_partida == "":
                        aviso("Insira algum valor")
                        continue
                    linha.horario_p = horario_partida
                    loop = False
                    break

                elif opcao == 4:
                    try:
                        valor_passagem = float(input())

                    except:
                        aviso("Insira um valor válido")
                        continue

                    linha.valor = valor_passagem
                    loop = False
                    break

                elif opcao == 5:
                    aviso("Voltando ao menu principal")
                    return

        else:
            aviso("Id não encontrado")
            break

# Função que realiza reserva dos assentos de um ônibus (A função também é chamada dentro da função: consultar_horario)
def reservar_assento(linha):
    while True:    
        data = str(input("Insira o dia que você deseja reservar(EX: dd/mm/aaaa): ")).strip()

        if not data:
            aviso("Insira um valor válido")
            continue    
        
        #Procurando busao do assentos
        busao_achado = None
        for bus in linha.onibus:
            if bus.data_p == data:
                busao_achado = bus
                break
        
        
        if not busao_achado :
            print("Onibus não encontrado com a data mencionada!!!")
            continue

        print(f"\nÔnibus encontrado para a data: {busao_achado.data_p}")
        break


    #olhando todos os assentos do busao        
    if all(busao_achado.assentos):
        print("Não há assentos livres neste ônibus!")
        return    
  
    #mostrand0 os acentos do busu 
    print("\nAssentos disponíveis:")
    
    for idx, ocupado in enumerate(busao_achado.assentos):
        status = "Ocupado" if ocupado else "Livre"
        print(f"{idx+1:02d} - {status}")
  
            
    try:    
        #escolhendo assentos que sera reservado
        numero = int(input("\n Escolha o numero que sera reservado por voce:  "))
        if numero < 1 or numero > 20:
            print("Assento invalido")
            return 
        
        if busao_achado.assentos[numero-1]:
            print("Assento ja esta ocupado ")
            return 
        
    except ValueError:
        print("Entrada Invalida")
        return 
    
    #confirmando nossa reserva
    print(f"\n Assento {numero} esta disponvel")
    confirmar = input("Confirma este lugar da reserva (s/n): ").lower()
    
    
    if confirmar != 's':
        print("Reserva cancelada ")
        return 
    
    
    busao_achado.assentos[numero-1] = True
    
    salvar_reserva(linha, busao_achado.data_p, numero)
    
    #identificando janela ou corredor
    tipo = "Janela" if numero % 2 != 0 else "Corredor"
    
    print(f"Assento {numero} reservado com sucesso! {tipo} ")    
    
    print(f"Data da viagem: {busao_achado.data_p}\n")
    
    valor_formatado = f"R${linha.valor:,.2f}".replace(".", ",")
    print("------------------------------------------")
    print("          COMPROVANTE DE RESERVA          ")
    print("------------------------------------------")
    print(f"Linha: {linha.id}")
    print(f"Origem: {linha.cidade_o}")
    print(f"Destino: {linha.cidade_d}\n")
    print(f"Data da viagem: {busao_achado.data_p}")
    print(f"Horário de partida: {linha.horario_p}\n")
    print(f"Assento: {numero} ({tipo})")
    print(f"Valor da passagem: {valor_formatado}")
    print("------------------------------------------")
    print("      OBRIGADO POR VIAJAR CONOSCO!")
    print("------------------------------------------")
         
# Função para consultar horários das linhas, se encontrar, pergunta ao usuário
# Eu alterei a pesquisa, tirei a pergunta de horários pq n faz sentido perguntar o horário já que é só um horário por linha
def consultar_horario(linhas_cadastradas):
    print("|========Consulta de Horarios========|")

    while True:

        cidade = str(input("Para qual cidade voce quer ir? ")).strip()

        if not cidade:
            aviso("Insira um nome válido")
            continue

        cidade.strip()
        break
    
    # Percorre as linhas para encontrar a escolhida pelo usuário, e verifica se há assentos disponíveis no horário indicado,
    # E pergunta ao usuário se ele deseja realizar uma reserva
    
    linhas_encontradas = []
    
    for linha in linhas_cadastradas:
        # Encontrar a linha e o onibus
        if linha.cidade_d.lower() == cidade.lower():
            linhas_encontradas.append(linha)

    if not linhas_encontradas:
        aviso(f"Nenhuma linha encontrada para {cidade}")
        return

            # Se for encontrado, verifica se tem assentos disponíveis

    print("\nLinhas disponíveis:")
    print("-------------------------------------")
    for linha in linhas_encontradas:
        print(f"{linha.id}) {linha.cidade_o} -> {linha.cidade_d} | Horário: {linha.horario_p} | Valor: R${linha.valor:.2f}")
    print("-------------------------------------")
            
    #escolhendo qual linha sera reservada
    while True:
        try:
            id_escolhido = int(input("Qual o id dessa linha que voce quer viajar? "))
        except ValueError:
            aviso("Digite um numero valido")
            continue
        
        #procurando nossa linha por ai
        linha_selecionada = None
        for linha in linhas_encontradas:
            if linha.id == id_escolhido:
                linha_selecionada = linha
                break
            
        if not linha_selecionada:
            aviso("ID nao encontrado nas opcoes listadas")
            continue
        
        break


    #confirmação da reserva
    
    print(f"\nVoce escolheu a linha para {linha_selecionada.cidade_d} no horario {linha_selecionada.horario_p}.")
    
    escolha = input("Deseja fazer uma reserva? [s/n]: ").lower()

    if escolha != "s":
        aviso("Voltando ao menu.")
        return
    
    reservar_assento(linha_selecionada)  

    """
    print("pessoa vai reservar pela linha e com isso vai receber as informações da passagem o numero do lugar e se é janela ou nao ")
        
    print("mostrando todos os horarios de todas as linhas possiveis")
        
    print("com isso a pessoa escolhe a linha e os outros dados e la ela compra a passagem")"""

# Acho que essa função perdeu o sentido depois da criação da consultar_horario
def consultar_assento(linhas_cadastradas):
    print("====Conferindo Assentos Disponiveis====")
    
    cidade_d = str(input("Qual cidade de destino que voce ira viajar? ")).strip()
    
    if not cidade_d:
        aviso("Cidade inválida")
        return
    
    #buscando as linhas para esta cidade especifica 
    
    linhas_encontradas = []
    
    for linha in linhas_cadastradas:
        if linha.cidade_d.lower() == cidade_d.lower():
            linhas_encontradas.append(linha)
    
    if not linhas_encontradas:
        aviso("Nenhuma linha encontrada para esta cidade")
        return 
    
    print("\n Linhas Achadas \n")
    
    for linha in linhas_encontradas:
        print(f"{linha.id} {linha.cidade_o} -> {linha.cidade_d} | Horario: {linha.horario_p}")
    
    #escolhendo a linha da viagem
 
    try:
        id_escolhido = int(input("\n Digite o ID da linha desejada: "))
    except:
        aviso("ID digitado Invalido")
        return
        
    linha_escolhida = None

    for l in linhas_encontradas:
        if l.id == id_escolhido:
            linha_escolhida = l
            break
    
    if not linha_escolhida:
        aviso("Linha nao encontrada")
        return
    
    #pegando a data 

    data = input("Digite a data da viagem (dd/mm/aaaa): ").strip()
    
    busao = None
    
    for b in linha_escolhida.onibus:
        if b.data_p == data:
            busao = b
            break
    
    if not busao:
        aviso("Nenhum onibus encontrado para tal data")
        return 

    print("\n==== Assentos Disponíveis ====")
    livres = 0
    
    for i, ocupado in enumerate(busao.assentos):
        status = "Ocupado" if ocupado else "Livre"
        
        print(f"Assento {i+1}: {status}")
        if not ocupado:
            livres += 1

    if livres == 0:
        print("\nNenhum assentos disponível!")
        return

    # 6 - Perguntar se quer reservar
    try:
        resposta = int(input("\nVai reservar assentos? (1-Sim / 2-Não): "))
    except:
        aviso("Opção inválida")
        return

    if resposta == 1:
        reservar_assento(linha_escolhida)
            
# Função que realiza a leitura de arquivos txt com reservas
def ler_arquivo_reservas(linhas_cadastradas):
    nome_arquivo = "reservas.txt"
    
    try:
        with open(nome_arquivo,"r",encoding = "utf-8") as arquivo:
            linhas = arquivo.readlines()
            
    except FileNotFoundError:
        print("Arquivo de reservas nao encontrado.Nenhuma reserva carregada")
        return 
        
    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        
        
        try:
            id_linha,data,assentos = linha.split(";")#quebrando nossa linha em pedaços
            id_linha = int(id_linha)
            assentos = int(assentos)
            
        except:
            print(f"Linha invalida do arquivo: {linha}")
            continue
        
        #na busca da linha correta
        
        linha_encontrada = None
        
        for l in linhas_cadastradas:
            if l.id == id_linha:
                linha_encontrada = l
                break
            
        if not linha_encontrada:
            print(f"Linha {id_linha} não encontrada no sistema. Ignorando reserva.")
            continue
        
        # Procurando o ônibus correto pela data dentro da linha que achamos
        onibus_encontrado = None
        for bus in linha_encontrada.onibus:
            if bus.data_p == data:
                onibus_encontrado = bus
                break
            
        if not onibus_encontrado:
            print(f"Ônibus da data {data} não existe na linha {id_linha}.")
            continue
        
        # Verificar se o assentos é válido
        if 1 <= assentos <= 20:
            onibus_encontrado.assentos[assentos - 1] = True
        else:
            print(f"Assento fora do limite: {assentos}")

    print("Reservas carregadas com sucesso!")
     
def salvar_reserva(linha, data, assentos):
    nome_arquivo = "reservas.txt"

    try:
        with open(nome_arquivo, "a", encoding="utf-8") as arq:
            arq.write(f"{linha.id};{data};{assentos}\n")

    except Exception as e:
        print(f"Erro ao salvar reserva: {e}")

# Função pra gerar relatório       
def gerar_relatorio(linhas_cadastradas):
    
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
    for linha in linhas_cadastradas:
        valor_arrecadado = 0
        for onibus in linha.onibus:
            for assento in onibus.assentos:
                if assento == True:
                    valor_arrecadado = valor_arrecadado + linha.valor
        else:
            valor_formatado = f"R${valor_arrecadado:,.2f}".replace(".", ",")
            mensagem = mensagem + f"| {linha.id}-) {linha.cidade_o} -> {linha.cidade_d} | Valor arrecadado: R${valor_formatado}"

    parte1 = f"""
|=============================================================|
| Relatório gerado em {tempo_agora.day}/{tempo_agora.month}/{tempo_agora.year} {tempo_agora.hour}:{tempo_agora.minute}:{tempo_agora.second}
|
| Valor arrecadado pelas linhas registradas:
|"""
    parte2 = """|
|=============================================================|\n\n"""

    if len(linhas_cadastradas) == 0:
        conteudo = f"{parte1}\n| Nenhuma Linha Cadastrada\n{parte2}"
    else:
        conteudo = f"{parte1}\n{mensagem}\n{parte2}"

    if opcao == 1:
        print(conteudo)
        
    elif opcao == 2:
        try:
            with open("relatorios.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(conteudo)
            print("Relatório salvo com sucesso!")
        except Exception as e:
            print("Erro ao salvar relatório:", e)