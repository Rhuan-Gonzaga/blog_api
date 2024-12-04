from flask import Blueprint, jsonify, request
from app import db
from app.models import Usuario,Postagem

routes = Blueprint('routes', __name__)

#Rotas para criar um novo usuario
@routes.route('/criarusuario', methods=['POST'])
def criarusuario():
    data = request.json
    print(data)
    novo_usuario = Usuario(nome=data['nome'], email=data['email'], senha=data['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201

#Rota para acessar os dados do usuario levando em conta o ID
@routes.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id):
    usuario= Usuario.query.get_or_404(id)
    return jsonify({"id": usuario.id, "nome": usuario.nome, "email": usuario.email})

#Criando uma nova postagem 
@routes.route('/postagens', methods=['POST'])
def criar_postagem():
    data= request.json
    nova_postagem = Postagem(titulo=data['titulo'], conteudo=data['conteudo'],usuario_id=data['usuario_id'])
    print(nova_postagem)
    db.session.add(nova_postagem)
    db.session.commit()
    return jsonify({"mensagem": "Postagem criada com sucesso"}),201

#Obtendo postagem pelo id
@routes.route('/postagens/<int:id>', methods=['GET'])
def obter_postagem(id):
    postagem = Postagem.query.get_or_404(id)
    return jsonify({"id": postagem.id, "titulo": postagem.titulo, "conteudo": postagem.conteudo, "usuario_id": postagem.usuario_id})
