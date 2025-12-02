import os
import time
import platform
from datetime import datetime, timedelta

# Função de avisos gerais, limpa o terminal quando executada
def aviso(mensagem, atraso=0.5):
    """Função para gerar avisos diversos"""
    
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
      
# Função que valida a data fornecida pelo usuário.
def validar_data_viagem(data_str, horario_partida):
    """
    Retorna:
      - (datetime.date, None) se OK
      - (None, motivo_str) se inválida
    """
    # validar formatação
    try:
        data_viagem = datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        return None, "Data inválida! Use o formato dd/mm/aaaa."

    hoje = datetime.now()
    limite = hoje + timedelta(days=30)  # hoje + 30 dias à frente

    if data_viagem.date() < hoje.date():
        return None, "Data inválida: já passou."

    if data_viagem.date() > limite.date():
        return None, "Data inválida: deve estar nos próximos 30 dias."

    # Se for hoje, verificar horário da linha
    if data_viagem.date() == hoje.date():
        try:
            horario = datetime.strptime(horario_partida, "%H:%M").time()
        except ValueError:
            return None, "Horário da linha em formato inválido."

        data_hora_partida = datetime.combine(data_viagem.date(), horario)
        if data_hora_partida <= hoje:
            return None, "Ônibus já partiu."

    return data_viagem.date(), None   