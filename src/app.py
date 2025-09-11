from config.database import create_app, db

app = create_app()

with app.app_context():
    db.create_all() 
    try:
        connection = db.engine.connect()
        print("[DEBUG] Conectado BD com sucesso!")
        connection.close()

    except Exception as e:
        print(f"[DEBUG] Erro ao conectar ao BD: {e}")

if __name__ == '__main__':
    app.run(debug=True)