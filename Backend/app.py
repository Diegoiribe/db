from main import create_app, db
import os

def upgrade_database():
    with db.engine.connect() as connection:
        connection.execute("ALTER TABLE usuarios MODIFY COLUMN imagen LONGBLOB")
        print("Columna 'imagen' modificada a LONGBLOB")

# Crear la aplicación
app = create_app()

# Crear el contexto de la aplicación
app.app_context().push()

if __name__ == '__main__':
    # Ejecutar la migración de la base de datos antes de iniciar el servidor
    try:
        upgrade_database()
        print("Migración ejecutada exitosamente")
    except Exception as e:
        print(f"Error al ejecutar la migración: {str(e)}")

    # Asegúrate de que las tablas existan
    db.create_all()
    
    # Iniciar el servidor Flask
    app.run(port=os.getenv("PORT"), debug=True)
