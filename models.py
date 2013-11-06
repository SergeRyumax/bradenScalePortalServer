#!/usr/bin/python
# coding=utf8
import json
import datetime
from peewee import *
from bradenscale import db

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
	usuario = ForeignKeyField(Usuario)

class Sala(db.Model):
	numero = CharField()
	andar = CharField()

class Paciente(db.Model):
	nome = CharField()
	cpf = CharField()
	dataNasc = DateTimeField()
	sexo = IntegerField()
	sala = ForeignKeyField(Sala, related_name='pacientes', null=True)
	modeloAgendamento = IntegerField(null=True)

class ModeloAgendamento(db.Model):
	segunda = BooleanField(null=True)
	terca = BooleanField(null=True)
	quarta = BooleanField(null=True)
	quinta = BooleanField(null=True)
	sexta = BooleanField(null=True)
	sabado = BooleanField(null=True)
	domingo = BooleanField(null=True)
	periodoDias = IntegerField(null=True)

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