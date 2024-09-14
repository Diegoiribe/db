from flask_migrate import Migrate
from main import create_app, db
import os

app = create_app()

# Inicializa Flask-Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    # Asegúrate de que las tablas existan antes de iniciar el servidor
    db.create_all()
    app.run(port=os.getenv("PORT"), debug=True)