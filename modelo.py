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
        return False in self.assentos