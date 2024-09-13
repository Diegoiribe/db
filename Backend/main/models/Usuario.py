from .. import db
import datetime as dt
import base64

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, default=True)
    imagen = db.Column(db.LargeBinary)  # Columna para almacenar la imagen

    def __repr__(self):
        return f"<Usuario {self.username}>"
    
    def to_json(self):
        # Codificar la imagen en Base64 si existe
        imagen_base64 = base64.b64encode(self.imagen).decode('utf-8') if self.imagen else None
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "active": self.active,
            "imagen": imagen_base64  # Devolver la imagen como Base64
        }
    
    @staticmethod
    def from_json(usuario_json):
        try:
            username = usuario_json.get("username")
            email = usuario_json.get("email")
            password = usuario_json.get("password")
            active = usuario_json.get("active")
            imagen_base64 = usuario_json.get("imagen")
            
            # Decodificar la imagen de Base64 a bytes si existe
            imagen = base64.b64decode(imagen_base64) if imagen_base64 else None
            
            return Usuario(username=username, email=email, password=password, active=active, imagen=imagen)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Error al convertir JSON a Usuario: {e}")