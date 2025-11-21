from flask import Flask
from config import Config
from models import init_db
from routes import main_bp

app = Flask(__name__)
app.config.from_object(Config)

# Đăng ký blueprint
app.register_blueprint(main_bp)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)