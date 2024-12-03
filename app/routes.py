from flask import Blueprint, jsonify, request
from app import db
from app.models import Usuario

routes = Blueprint('routes', __name__)

#Rotas de usuários
@routes.route('/criarusuario', methods=['POST'])
def criarusuario():
    data = request.json
    print(data)
    novo_usuario = Usuario(nome=data['nome'], email=data['email'], senha=data['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201