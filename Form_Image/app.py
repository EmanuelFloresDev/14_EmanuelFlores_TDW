# Crea la aplicación Flask y ejecuta el servidor en modo desarrollo
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)