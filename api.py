#!/usr/bin/python
# coding=utf8
from flask.ext.restful import Resource, Api, reqparse, fields, marshal_with

from flaskext.uploads import *
from flask import request, jsonify, Response

import uuid
import log
import json
from models import *
from bradenscale import app, photos
import userResource

import base64

api = Api(app)

usuarios_fields = {
	'email': fields.String,
	'registo': fields.DateTime
}

DATETIME_FORMAT = '%Y-%m-%d'

def convertSelectToList(modelList):
	result = list()
	for model in modelList:
		result.append(model);
	return result

def listaJson(dictObject):
	return Response(json.dumps(dictObject), mimetype='application/json')

class Alive(Resource):
	def get(self):
		return 'Is Working'

class Login(Resource):
	def put(self, usuarioLogin):
		params = request.json;
		password = params['password']
		usuario = userResource.create(usuarioLogin, password, Usuario.ADMIN)
		if usuario is None:
			return "NOK", 409 #Conflict
		return "OK", 201 #Created

	def post(self, usuarioLogin):
		params = request.json;
		password = params['password']
		
		tokenLogin = userResource.login(usuarioLogin, password)
		
		if tokenLogin is None:
			return 'NOK', 401 #Unauthorized
		return jsonify(token=tokenLogin.token, validade='{:%m/%d/%Y %H:%M:%S}'.format(tokenLogin.validade))

class TokenRefresh(Resource):
	def post(self, tokenLogin):
		novaValidade = userResource.refreshToken(tokenLogin)
		return jsonify(validade='{:%m/%d/%Y %H:%M:%S}'.format(novaValidade))



class AllUsers(Resource):
	@marshal_with(usuarios_fields)
	def get(self):
		usuarios = list()
		for usu in Usuario.select():
			usuarios.append(usu);
		return usuarios

class EnfermeirosApi(Resource):
	def post(self, tokenLogin):
		userResource.byToken(tokenLogin)

		args = request.json
		nome = args['nome']
		cpf = args['cpf']
		sexo = args['sexo']
		email = args['email']
		senha = args['senha']

		usuario = userResource.create(email, senha, Usuario.ENFERMEIRO)
		enfermeiro = Enfermeiro.create(nome=nome, cpf=cpf, sexo=sexo, email=email, usuario=usuario)
		return jsonify(usuario=email, senha=senha)

class PacientesApi(Resource):
	def post(self, tokenLogin):
		userResource.byToken(tokenLogin)
		
		args = request.json
		nome = args['nome']
		cpf = args['cpf']
		sexo = args['sexo']
		dataNasc = args['dataNasc']
		dataNasc = datetime.datetime.strptime(dataNasc, DATETIME_FORMAT)
		
		paciente = Paciente.create(nome=nome, cpf=cpf, sexo=sexo, dataNasc=dataNasc)
		return jsonify(result="OK")
	def get(self, tokenLogin):
		pacientes = Paciente.select()
		listaResult = []
		for paciente in pacientes:
			tuplaPac = {}
			tuplaPac["nome"] = paciente.nome
			tuplaPac["cpf"] = paciente.cpf
			if paciente.sala is not None:
				sala = paciente.sala
				tuplaSala = {}
				tuplaSala["numero"] = sala.numero
				tuplaSala["andar"] = sala.andar
				tuplaPac["sala"] = tuplaSala
			listaResult.append(tuplaPac)

		return listaJson(listaResult)

api.add_resource(Alive,'/alive')
api.add_resource(AllUsers,'/user/')
api.add_resource(Login, '/user/<string:usuarioLogin>')
api.add_resource(TokenRefresh, '/user/<string:tokenLogin>/refreshToken')
api.add_resource(EnfermeirosApi, '/user/<string:tokenLogin>/enfermeiro')
api.add_resource(PacientesApi, '/user/<string:tokenLogin>/paciente')