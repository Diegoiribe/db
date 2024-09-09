from flask_restful import Resource
from flask import json, request, jsonify
from .. import db
from main.models import UsuarioModel


class Usuario(Resource):
        
        def get(self, id):
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            return usuario.to_json()
        
        def delete(self, id):
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            db.session.delete(usuario)
            db.session.commit()
            return '', 204
        
        def put(self, id):
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            data = request.get_json()
            usuario.username = data.get("username")
            usuario.email = data.get("email")
            usuario.password = data.get("password")
            usuario.active = data.get("active")
            db.session.commit()
            return usuario.to_json(), 201

class Usuarios(Resource):
    
    def get(self):
        usuarios = db.session.query(UsuarioModel).all()
        return jsonify([usuario.to_json() for usuario in usuarios])
    
    def post(self):
        data = request.get_json()
        usuario = UsuarioModel(**data)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
    
