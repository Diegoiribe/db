from flask_restful import Resource
from flask import request, jsonify
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
        
        # Manejar el envío de archivos (imagen)
        if 'imagen' in request.files:
            imagen_file = request.files['imagen']
            usuario.imagen = imagen_file.read()  # Convertir la imagen a binario
        
        # Obtener datos del cuerpo de la solicitud (JSON)
        data = request.form or request.get_json()  # Usar request.form para manejar archivos e info juntos
        usuario.username = data.get("username", usuario.username)
        usuario.email = data.get("email", usuario.email)
        usuario.password = data.get("password", usuario.password)
        usuario.active = data.get("active", usuario.active)
        
        db.session.commit()
        return usuario.to_json(), 201

class Usuarios(Resource):
    
    def get(self):
        usuarios = db.session.query(UsuarioModel).all()
        return jsonify([usuario.to_json() for usuario in usuarios])
    
    def post(self):
        # Manejar imagen
        imagen_file = request.files.get('imagen')
        imagen_binaria = imagen_file.read() if imagen_file else None
        
        # Manejar otros datos del formulario o JSON
        data = request.form or request.get_json()
        usuario = UsuarioModel(
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password"),
            active=data.get("active", True),  # Valor por defecto a True
            imagen=imagen_binaria  # Almacenar la imagen binaria si existe
        )
        
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
