from models import *
#Cria as tabelas 
def create_tables():
	Usuario.create_table(True)
	TokenAuth.create_table(True)
	Enfermeiro.create_table(True)
	Sala.create_table(True)
	Paciente.create_table(True)
	ModeloAgendamento.create_table(True)
	AvaliacaoEscalaBraden.create_table(True)

if __name__ == "__main__":
	create_tables()