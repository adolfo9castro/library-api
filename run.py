from app import create_app

# Crear la aplicación Flask desde la fábrica
app = create_app()

app.run(host="0.0.0.0", port=5000)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)