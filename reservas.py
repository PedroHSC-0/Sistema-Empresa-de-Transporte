from util import aviso
from datetime import datetime, timedelta


def registrar_falha(linha_original, motivo, nome="reservas_nao_realizadas.txt"):
    """Funcao que registra as falhas no arquivo"""
    with open(nome, "a", encoding="utf-8") as arq:
        arq.write(f"{linha_original} -> Motivo: {motivo}\n")            
        
        
        
            

def ler_arquivo_reservas(linhas_cadastradas):
    """Função que realiza a leitura de arquivos txt com reservas"""
    
    nome_entrada = "reservas.txt"
    nome_falhas = "reservas_nao_realizadas.txt"

    try:
        with open(nome_entrada, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de reservas não encontrado. Nenhuma reserva carregada.")
        return

    for linha in linhas:
        original = linha.strip()
        if not original:
            continue

        # Novo formato do enunciado: CIDADE, HORÁRIO, DATA, ASSENTO
        partes = [p.strip() for p in original.split(",")]

        if len(partes) != 4:
            registrar_falha(original, "Formato inválido (esperado: cidade, horário, data, assento)", nome_falhas)
            continue

        cidade, horario, data_txt, assento_txt = partes

        # Validar assento
        try:
            assento = int(assento_txt)
        except:
            registrar_falha(original, "Assento não é número", nome_falhas)
            continue

        # Encontrar a linha
        linha_encontrada = None
        for l in linhas_cadastradas.values(): 
            if l.cidade_d.lower() == cidade.lower() and l.horario_p == horario:
                linha_encontrada = l
                break

        if not linha_encontrada:
            registrar_falha(original, "Linha não encontrada (cidade + horário)", nome_falhas)
            continue

        # Validar data
        try:
            data_dt = datetime.strptime(data_txt, "%d/%m/%Y")
        except:
            registrar_falha(original, "Data inválida (use dd/mm/aaaa)", nome_falhas)
            continue

        hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        limite = hoje + timedelta(days=29)

        if data_dt < hoje:
            registrar_falha(original, "Data já passou", nome_falhas)
            continue

        if data_dt > limite:
            registrar_falha(original, "Data fora do intervalo de 30 dias", nome_falhas)
            continue

        # Procurar ônibus
        bus_encontrado = None
        for bus in linha_encontrada.onibus:
            if bus.data_p == data_txt:
                bus_encontrado = bus
                break

        if not bus_encontrado:
            registrar_falha(original, "Ônibus para essa data não existe", nome_falhas)
            continue

        # Validar assento
        if not (1 <= assento <= 20):
            registrar_falha(original, "Assento fora do limite (1 a 20)", nome_falhas)
            continue

        if bus_encontrado.assentos[assento - 1]:
            registrar_falha(original, "Assento já ocupado", nome_falhas)
            continue

        # Aplicar reserva
        bus_encontrado.assentos[assento - 1] = True
        print(f"Reserva aplicada: {cidade}, {horario}, {data_txt}, Assento {assento}")

    print("Reservas carregadas.")

     
     
     
def salvar_reserva(linha, data, assento):
    """Funcao que salva as reservas no txt"""
    nome_arquivo = "reservas.txt"

    try:
        with open(nome_arquivo, "a", encoding="utf-8") as arq:
            arq.write(f"{linha.cidade_d}, {linha.horario_p}, {data}, {assento}\n")

    except Exception as e:
        print(f"Erro ao salvar reserva: {e}")
        
        
        
        

def reservar_assento(linha,busao_achado):
    """Função que realiza reserva dos assentos de um ônibus (A função também é chamada dentro da função: consultar_horario)"""    
    
    # Conferir se há assentos livres
    if all(busao_achado.assentos):
        print("Não há assentos livres neste ônibus!")
        return

    print("\nAssentos disponíveis:")
    for idx, ocupado in enumerate(busao_achado.assentos):
        status = "Ocupado" if ocupado else "Livre"
        
        print(f"{idx+1:02d} - {status}")

    # Escolha do assento
    try:
        numero = int(input("\nEscolha o número do assento: "))

        if numero < 1 or numero > 20:
            print("Assento inválido")
            return
        
        if busao_achado.assentos[numero - 1]:
            print("Assento já está ocupado")
            return

    except ValueError:
        print("Entrada inválida")
        return

    # Confirmação
    print(f"\nAssento {numero} está disponível.")
    confirmar = input("Confirmar reserva? (s/n): ").lower()

    if confirmar != 's':
        print("Reserva cancelada.")
        return

    # Reservando o assento
    busao_achado.assentos[numero - 1] = True
    salvar_reserva(linha, busao_achado.data_p, numero)

    tipo = "Janela" if numero % 2 != 0 else "Corredor"

    print(f"\nAssento {numero} reservado com sucesso! ({tipo})\n")

    valor_formatado = f"R${linha.valor:,.2f}".replace(".", ",")
    print("------------------------------------------")
    print("          COMPROVANTE DE RESERVA          ")
    print("------------------------------------------")
    print(f"Linha: {linha.id}")
    print(f"Origem: {linha.cidade_o}")
    print(f"Destino: {linha.cidade_d}")
    print(f"Data da viagem: {busao_achado.data_p}")
    print(f"Horário de partida: {linha.horario_p}")
    print(f"Assento: {numero} ({tipo})")
    print(f"Valor da passagem: {valor_formatado}")
    print("------------------------------------------")
    print("      OBRIGADO POR VIAJAR CONOSCO!")
    print("------------------------------------------")