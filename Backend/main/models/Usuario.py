from .. import db
import datetime as dt

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Usuario {self.username}>"
    
    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "active": self.active
        }
    
    @staticmethod
    def from_json(usuario_json):
        try:
            username = usuario_json.get("username")
            email = usuario_json.get("email")
            password = usuario_json.get("password")
            active = usuario_json.get("active")
            
            return Usuario(username=username, email=email, password=password, active=active)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Error al convertir JSON a Usuario: {e}")