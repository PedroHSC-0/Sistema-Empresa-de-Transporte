from modelo import Linha
from reservas import reservar_assento
from util import aviso, validar_data_viagem
from datetime import datetime, timedelta



# Função que cadastra uma nova linha, pedindo todos atributos para gerar uma nova instância da classe linha e armazená-la na lista "linhas_cadastradas". Funcionando
def cadastrar_linha(linhas_cadastradas):

    if linhas_cadastradas:
        id_linha = max(linhas_cadastradas.keys()) + 1
    else:
        id_linha = 1

    print("|========Cadastro de Linha========|\n")



    # Input de Dados
    while True:
        
        cidade_origem = str(input("Qual a cidade de origem da sua linha? ")).strip()
        if not cidade_origem:
            aviso("Entrada vazia")
            continue
       

        
        cidade_destino = str(input("Qual a cidade de destino da sua linha? ")).strip()
        if not cidade_destino:
            aviso("Entrada vazia")
            continue
        
       #garanti de que o horario sera no formato certo
        while True:
            horario_partida = input("Qual o horário de partida da sua linha? (HH:MM): ").strip()
            if not horario_partida:
                aviso("Entrada vazia")
                continue
            
            try:
                # Tenta converter para o formato HH:MM (ex: 14:30)
                datetime.strptime(horario_partida, "%H:%M")
                break # Sai do loop de horário se for válido
            except ValueError:
                
                aviso("Formato de horário inválido. Use HH:MM (Ex: 08:30 ou 17:00).")
                continue # Continua no loop de horário
            
        #garantia de colocar o valor da maneira certa
        while True:
            try:
                valor = float(input("Qual o valor da passagem da sua linha? "))
                if valor <= 0:
                    aviso("Valor inválido. O valor deve ser maior que zero.")
                    continue
                break # Sai do loop de valor se for válido
                
            except ValueError:
                aviso("Entrada inválida. Digite um valor numérico.")
                continue


        break

    # Gerando instância
    nova_linha = Linha(id_linha, cidade_origem, cidade_destino, horario_partida, valor)
    nova_linha.adicionar_onibus()
    
    # DEPOIS: Adiciona ao dicionário usando o ID como chave
    linhas_cadastradas[id_linha] = nova_linha
    
    
# Função que mostra todas as linhas e suas informações. Funcionando
def mostrar_linhas(linhas_cadastradas, todas=True, id_mostrar=None):
    if todas:
        if linhas_cadastradas:

            print("|--------------------------------------")
            for linha in linhas_cadastradas.values(): 
                valor_formatado = f"R${linha.valor:,.2f}".replace(".", ",")
                
                print(f"{linha.id}-) {linha.cidade_o} -> {linha.cidade_d}\n    Horário: {linha.horario_p} | Valor: {valor_formatado}")
                print("|--------------------------------------")
        else:
            aviso("Não há linhas cadastradas")

    else:
        if id_mostrar in linhas_cadastradas:
            linha = linhas_cadastradas[id_mostrar] # Acessa o objeto Linha diretamente

            print("|--------------------------------------")
            valor_formatado = f"R${linha.valor:,.2f}".replace(".", ",")
            print(f"{linha.id}-) {linha.cidade_o} -> {linha.cidade_d}\n    Horário: {linha.horario_p} | Valor: {valor_formatado}")
            


# Função para remover uma linha do sistema através do ID dado
def remover_linha(linhas_cadastradas):
    while True:
        print("|========Remoção De Linha========|")

        try:
            id_remover = int(input("Insira o ID da linha a ser removida: "))
            
            if id_remover in linhas_cadastradas:
                del linhas_cadastradas[id_remover]
                print(f"Linha com ID {id_remover} removida com sucesso!")
                break
            else:
                print("O id não pertence a nenhuma linha registrada")
                break
                
        except ValueError:
            aviso("Insira um valor válido")
            continue
        break
    

# Função para alterar dados da linha (Cidade Destino e horários).
def alterar_linha(linhas_cadastradas):
    print("|========Alteração de Linha========|")
    
    while True: 
        try: 
            id_linha = int(input("Insira o id da linha a ser alterada: "))
        except:
            aviso("Valor inválido")
            continue

        
        if id_linha not in linhas_cadastradas:
            aviso("Id não encontrado")
            break # Se não encontrar, sai do loop de alteração

        #
        linha = linhas_cadastradas[id_linha] 
        
        # O objeto 'linha' agora está pronto para ser alterado
        
        
        while True:
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
            except ValueError: # Trata erro se digitar algo que não é número na opção
                aviso("Opção inválida. Digite um número de 1 a 5.")
                continue # Volta ao menu de opções

            if opcao == 1:
                cidade_origem = str(input("Nova cidade de origem: ")).strip()
                if not cidade_origem:
                    aviso("Insira algum valor")
                    continue
                linha.cidade_o = cidade_origem
                aviso("Cidade de origem alterada com sucesso!")
                return # Sai da função após a alteração
                
            elif opcao == 2:
                cidade_destino = str(input("Nova cidade de destino: ")).strip()
                if not cidade_destino:
                    aviso("Insira algum valor")
                    continue
                linha.cidade_d = cidade_destino
                aviso("Cidade de destino alterada com sucesso!")
                return 

            elif opcao == 3:
                horario_partida = str(input("Novo horário de partida (hh:mm): ")).strip()
                if not horario_partida:
                    aviso("Insira algum valor")
                    continue
                linha.horario_p = horario_partida
                aviso("Horário de partida alterado com sucesso!")
                return

            elif opcao == 4:
                try:
                    valor_passagem = float(input("Novo valor da passagem: "))
                    if valor_passagem < 0:
                         aviso("O valor deve ser positivo.")
                         continue

                except ValueError:
                    aviso("Insira um valor válido")
                    continue

                linha.valor = valor_passagem
                aviso("Valor da passagem alterado com sucesso!")
                return

            elif opcao == 5:
                aviso("Voltando ao menu principal")
                return
            
            else:
                aviso("Opção inválida.")
                continue
        
        

# Função para consultar horários das linhas, se encontrar, pergunta ao usuário
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
    
    for linha in linhas_cadastradas.values(): 
        # Encontrar a linha e o onibus
        if linha.cidade_d.lower() == cidade.lower():
            linhas_encontradas.append(linha)

    if not linhas_encontradas:
        aviso(f"Nenhuma linha encontrada para {cidade}")
        return

    print("\nLinhas disponíveis:")
    print("-------------------------------------")
    for linha in linhas_encontradas:
        print(f"{linha.id}) {linha.cidade_o} -> {linha.cidade_d} | Horário: {linha.horario_p} | Valor: R${linha.valor:.2f}")
    print("-------------------------------------")
            
    #escolhendo o id da linha que ocorrera a viagem
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


    #confirmaçao da linha escolhida e o horario

    print(f"\nVoce escolheu a linha para {linha_selecionada.cidade_d} no horario {linha_selecionada.horario_p}.")
    print("")
    
    #emendando a funcao de consultar assento
    consultar_assento(linha_selecionada)
    
    


def consultar_assento(linha):
    print("\n==== Conferindo Assentos Disponíveis ====")

    # Escolher a data do ônibus
    while True:
        
        data = input("Digite a data da viagem (dd/mm/aaaa) ou 'sair' para voltar: \n").strip()
        if not data:
            print("Entrada vazia. Digite uma data ou 'sair' para voltar.\n")
            continue

        if data.lower() in ('q', 'sair', 'voltar', 'cancelar'):
            print("Operação cancelada. Voltando ao menu.\n")
            return

        data_validada, motivo = validar_data_viagem(data, linha.horario_p)

        if data_validada is not None:
            # sucesso: data_validada é um datetime.date - podemos seguir
            break

        # data inválida: mostrar motivo e perguntar se quer tentar outra
        print(f"\n{motivo}\n")
        tentar = input("Deseja tentar outra data? (s/n): \n").strip().lower()
        if tentar != 's':
            print("Operação cancelada. Voltando ao menu.\n")
            return

    busao = None
    for b in linha.onibus:
        if b.data_p == data:
            busao = b
            break

    if not busao:
        aviso("Nenhum ônibus encontrado para esta data\n")
        return
    
    print("\n==== Assentos Disponíveis ====")
    livres = 0
    
    for i, ocupado in enumerate(busao.assentos):
        status = "Ocupado" if ocupado else "Livre"
        print(f"Assento {i+1}: {status}")
        if not ocupado:
            livres += 1

    if livres == 0:
        print("\nNenhum assento disponível!")
        return

    # Perguntar se quer reservar
    try:
        resposta = int(input("\nVai reservar assentos? (1-Sim / 2-Não): "))
    except:
        aviso("Opção inválida")
        return

    if resposta == 1:
        #emendando a funcao reservar assento de uma vez
        reservar_assento(linha,busao)