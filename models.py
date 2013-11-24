#!/usr/bin/python
# coding=utf8
import json
import datetime
from peewee import *
from bradenscale import db, app
from flask_peewee.rest import RestAPI

class Usuario(db.Model):
	ADMIN = 0
	ENFERMEIRO = 1

	email = CharField()
	senha = CharField()
	registo = DateTimeField(default=datetime.datetime.now)
	tipo = IntegerField()

class TokenAuth(db.Model):
	token = CharField(index=True)
	validade = DateTimeField()
	usuario = ForeignKeyField(Usuario, related_name='tokens')

class Enfermeiro(db.Model):
	email = CharField()
	cpf = CharField()
	nome = CharField()
	sexo = IntegerField()
	registo = DateTimeField(default=datetime.datetime.now)

class Sala(db.Model):
	numero = CharField()
	andar = CharField()

class ModeloAgendamento(db.Model):
	segunda = BooleanField(null=True, default=False)
	terca = BooleanField(null=True, default=False)
	quarta = BooleanField(null=True, default=False)
	quinta = BooleanField(null=True, default=False)
	sexta = BooleanField(null=True, default=False)
	sabado = BooleanField(null=True, default=False)
	domingo = BooleanField(null=True, default=False)
	periodoDias = IntegerField(null=True, default=0)

class Paciente(db.Model):
	nome = CharField()
	cpf = CharField()
	dataNasc = DateTimeField()
	sexo = IntegerField()
	enfermeiro = ForeignKeyField(Enfermeiro, related_name='pacientes', null=True)
	sala = ForeignKeyField(Sala, related_name='pacientes', null=True)
	modeloAgendamento = ForeignKeyField(ModeloAgendamento, null=True)

class AvaliacaoEscalaBraden(db.Model):
	paciente = ForeignKeyField(Paciente, related_name='avaliacoes')
	sala = ForeignKeyField(Sala, related_name='avaliacoes')
	enfermeiro = ForeignKeyField(Enfermeiro, related_name='avaliacoes')
	data = DateTimeField();
	status = IntegerField()
	percepcaoSensorial = IntegerField()
	umidade = IntegerField()
	atividade = IntegerField()
	mobilidade = IntegerField()
	nutricao = IntegerField()
	friccao = IntegerField()

restApi = RestAPI(app)
restApi.register(AvaliacaoEscalaBraden)
restApi.register(Sala)
restApi.setup()