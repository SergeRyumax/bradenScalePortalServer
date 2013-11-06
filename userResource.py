from models import *
from flask import abort
import log
import uuid
import datetime

ADMIN = 0
ENFERMEIRO = 1

def login(user, password):
	try:
		usuario = Usuario.get(Usuario.email == user)
		if usuario.senha != password:
			return None
		
		now = datetime.datetime.now()
		deleteQuery = TokenAuth.delete().where(TokenAuth.usuario==usuario).where(TokenAuth.validade<now)
		deleteQuery.execute()

		loop = True
		while loop:
			novoToken = str(uuid.uuid4())
			try:
				TokenAuth.get(TokenAuth.token==novoToken)
			except DoesNotExist, e:
				loop = False

		tokenValidade = datetime.datetime.now() + datetime.timedelta(days=2)
		token = TokenAuth.create(usuario=usuario, token=novoToken, validade=tokenValidade)

		log.d("Token Criado " + token.token)
	except DoesNotExist , e:
		return None;

	return token

def create(user, password, tipo):
	try:
		usuario = Usuario.get(Usuario.email == user)
		return
	except DoesNotExist , e:
		usuario = Usuario.create(email=user, senha=password, tipo=tipo)
		#validade = datetime.datetime.max
		#token = TokenAuth.create(usuario=usuario, token=user, validade=validade)
	return usuario

def byToken(token):
	try:
		tokenAuth = TokenAuth.get(TokenAuth.token==token)
		if (tokenAuth.validade - datetime.datetime.now()).days < 0:
			abort(401)
	except DoesNotExist , e:
		abort(401) 
	return tokenAuth.usuario

def refreshToken(token):
	usuarioToken = byToken(token);
	tokenValidade = datetime.datetime.now() + datetime.timedelta(days=2)
	update_query = TokenAuth.update(validade=tokenValidade).where(TokenAuth.token==token)
	update_query.execute() 
	return tokenValidade