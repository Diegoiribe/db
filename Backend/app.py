from main import create_app, db
import os

def upgrade_database():
    with db.engine.connect() as connection:
        connection.execute("ALTER TABLE usuarios MODIFY COLUMN imagen LONGBLOB")
        print("Columna 'imagen' modificada a LONGBLOB")

app = create_app()

# Crear el contexto de la aplicación
with app.app_context():
    # Ejecutar la migración de la base de datos antes de iniciar el servidor
    try:
        upgrade_database()
        print("Migración ejecutada exitosamente")
    except Exception as e:
        print(f"Error al ejecutar la migración: {str(e)}")

    # Crear todas las tablas (si es necesario)
    db.create_all()

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(port=os.getenv("PORT"), debug=True)
