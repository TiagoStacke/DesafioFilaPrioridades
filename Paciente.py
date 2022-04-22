class Paciente:
    def __init__(self, nome_paciente, tipo_sanguineo, data_nascimento):
        self.nome_paciente = nome_paciente
        self.tipo_sanguineo = tipo_sanguineo
        self.data_nascimento = data_nascimento
    def __str__(self):
        return self.nome_paciente, self.tipo_sanguineo, self.data_nascimento

    


