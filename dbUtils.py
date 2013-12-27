#!/usr/bin/python
# coding=utf8
from models import *
import random
#Cria as tabelas 
def create_tables():
	Usuario.create_table(True)
	TokenAuth.create_table(True)
	Enfermeiro.create_table(True)
	Sala.create_table(True)
	ModeloAgendamento.create_table(True)
	Paciente.create_table(True)
	AvaliacaoEscalaBraden.create_table(True)

DATETIME_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT_WITH_HOURS = '%Y-%m-%d %H:%M:%S'

def populateInit():

	usuario = Usuario.create(email="admin", senha="admin", tipo=Usuario.ADMIN)
	
	enf1 = criaEnf("Maria Enfermeira", "111111111", 1, "maria.enf@email.com")
	enf2 = criaEnf("Stella Enfermeira", "111111111", 1, "stella.enf@email.com")
	enf3 = criaEnf("Rose Enfermeira", "111111111", 1, "rose.enf@email.com")

	sala11a = criaSala(1, "11-A")
	sala11b = criaSala(1, "11-B")
	sala11c = criaSala(1, "11-C")
	sala12a = criaSala(1, "12-A")
	sala12b = criaSala(1, "12=B")
	sala21a = criaSala(2, "21-A")
	sala21b = criaSala(3, "21-B")
	sala22a = criaSala(4, "22-A")
	sala22b = criaSala(4, "22-B")
	
	pac1 = criaPac("Pedro Paciente", "111111111", 0, "1980-10-01", enf1, sala11a)
	pac2 = criaPac("Jose Paciente", "111111111", 0, "1980-10-01", enf1, sala11a)
	pac3 = criaPac("Gabriela Paciente", "111111111", 1, "1980-10-01", enf1, sala11b)
	pac4 = criaPac("Rafael Paciente", "111111111", 0, "1980-10-01", enf2, sala11c)
	pac5 = criaPac("Joao Paciente", "111111111", 0, "1980-10-01", enf2, sala11c)
	pac6 = criaPac("Carol Paciente", "111111111", 1, "1980-10-01", enf2, sala12a)
	pac7 = criaPac("Larissa Paciente", "111111111", 1, "1980-10-01", enf2, sala12a)
	pac8 = criaPac("Paulo Paciente", "111111111", 0, "1980-10-01", enf3, sala12b)

	pac1a = criaPac("Pedro Paciente", "111111111", 0, "1980-10-01", enf1, sala21a)
	pac2a = criaPac("Jose Paciente 2", "111111111", 0, "1980-10-01", enf1, sala21a)
	pac3a = criaPac("Gabriela Paciente 2", "111111111", 1, "1980-10-01", enf1, sala21a)
	pac4a = criaPac("Rafael Paciente 2", "111111111", 0, "1980-10-01", enf2, sala21b)
	pac5a = criaPac("Joao Paciente 2", "111111111", 0, "1980-10-01", enf2, sala21b)
	pac6a = criaPac("Carol Paciente 2", "111111111", 1, "1980-10-01", enf2, sala22a)
	pac7a = criaPac("Larissa Paciente 2", "111111111", 1, "1980-10-01", enf2, sala22a)
	pac8a = criaPac("Maria Paciente 2", "111111111", 1, "1980-10-01", enf3, sala22b)

	agend1 = criaAgendamento(segunda=True, quarta=True, sexta=True, domingo=True)
	agend2 = criaAgendamento(terca=True, quinta=True, sabado=True, segunda=True)
	agend3 = criaAgendamento(periodoDias=1)
	agend4 = criaAgendamento(periodoDias=2)

	pac1.modeloAgendamento = agend1
	pac2.modeloAgendamento = agend1
	pac3.modeloAgendamento = agend1
	pac4.modeloAgendamento = agend1
	pac5.modeloAgendamento = agend2
	pac6.modeloAgendamento = agend2
	pac7.modeloAgendamento = agend2
	pac8.modeloAgendamento = agend2
	pac1a.modeloAgendamento = agend3
	pac2a.modeloAgendamento = agend3
	pac3a.modeloAgendamento = agend3
	pac4a.modeloAgendamento = agend3
	pac5a.modeloAgendamento = agend4
	pac6a.modeloAgendamento = agend4
	pac7a.modeloAgendamento = agend4
	pac8a.modeloAgendamento = agend4

	pac1.save()
	pac2.save()
	pac3.save()
	pac4.save()
	pac5.save()
	pac6.save()
	pac7.save()
	pac8.save()
	pac1a.save()
	pac2a.save()
	pac3a.save()
	pac4a.save()
	pac5a.save()
	pac6a.save()
	pac7a.save()
	pac8a.save()
	
	criaPacienteBraden(pac1)
	criaPacienteBraden(pac2)
	criaPacienteBraden(pac3)
	criaPacienteBraden(pac4)
	criaPacienteBraden(pac5)
	criaPacienteBraden(pac6)
	criaPacienteBraden(pac7)
	criaPacienteBraden(pac8)

	criaPacienteBraden(pac1a)
	criaPacienteBraden(pac2a)
	criaPacienteBraden(pac3a)
	criaPacienteBraden(pac4a)
	criaPacienteBraden(pac5a)
	criaPacienteBraden(pac6a)
	criaPacienteBraden(pac7a)
	criaPacienteBraden(pac8a)




def criaEnf(nome, cpf, sexo, email):
	usuario = Usuario.create(email=email, senha=email, tipo=Usuario.ENFERMEIRO)
	enfermeiro = Enfermeiro.create(nome=nome, cpf=cpf, sexo=sexo, email=email, usuario=usuario)
	return enfermeiro

def criaPac(nome, cpf, sexo, dataNasc, enfermeiro, sala):
	dataNasc = datetime.datetime.strptime(dataNasc, DATETIME_FORMAT)
		
	paciente = Paciente.create(nome=nome, cpf=cpf, sexo=sexo, dataNasc=dataNasc, enfermeiro=enfermeiro)
	paciente.sala = sala
	paciente.save()

	return paciente

def criaSala(andar, numero):
	return Sala.create(numero=numero, andar=andar)

def criaAgendamento(**atributos):
	return ModeloAgendamento.create(**atributos);

def criaEscalaBraden(level, dia, paciente, sala, enfermeiro, status):
	params = {}
	params['paciente'] = paciente
	params['data'] = dia
	params['enfermeiro'] = enfermeiro
	params['sala'] = sala
	params['status'] = status

	levelMin = 1
	levelMax = 4
	if level == 'OTIMO':
		levelMax = 1
	if level == 'BOM':
		levelMax = 2
	if level == 'RUIM':
		levelMin = 2
		levelMax = 4
	if level == 'PESSIMO':
		levelMin = 3
		levelMax = 4

	params['percepcaoSensorial'] = random.randint(levelMin, levelMax)
	params['umidade'] = random.randint(levelMin, levelMax)
	params['atividade'] = random.randint(levelMin, levelMax)
	params['mobilidade'] = random.randint(levelMin, levelMax)
	params['nutricao'] = random.randint(levelMin, levelMax)
	params['friccao'] = random.randint(levelMin, levelMax)

	AvaliacaoEscalaBraden.create(**params);
		
def criaPacienteBraden(paciente):
	dia = datetime.datetime.strptime('2012-12-10 20:20:02', DATETIME_FORMAT_WITH_HOURS)
	for i in range(20):
		criaEscalaBraden(0, dia, paciente, paciente.sala, paciente.enfermeiro, 1)
		dia = dia + datetime.timedelta(days=2)


if __name__ == "__main__":
	create_tables()
	populateInit()