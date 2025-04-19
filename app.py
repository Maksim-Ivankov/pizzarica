from flask import Flask
from flask_cors import CORS
from src.database.database import db

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://min:12345679@85.175.7.40:5439/min_db'
db.init_app(app)

# app.register_blueprint(admin_rout)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)