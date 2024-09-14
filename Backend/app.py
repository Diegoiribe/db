from flask_migrate import Migrate
from main import create_app, db
import os

app = create_app()

# Inicializa Flask-Migrate
migrate = Migrate(app, db)

# Poner la aplicación en el contexto antes de realizar cualquier operación
with app.app_context():
    # Crear todas las tablas (si es necesario)
    db.create_all()

if __name__ == '__main__':
    app.run(port=os.getenv("PORT"), debug=True)