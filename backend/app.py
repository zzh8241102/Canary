    # //////////// app factory and runner //////////// #

from flask import Flask
from flask_cors import CORS
from extension import db
from flask_migrate import Migrate
import utils.config as config
from utils import add_apis,add_blueprints
from api import api_bp, api
from flask_jwt_extended import JWTManager
from controller.tag_controller import generate_basic_tags
# //////////// create app //////////// #
app = Flask(__name__)
app.config.from_object(config)
jwt = JWTManager(app)
db.init_app(app)
Migrate(app, db)
CORS(app, supports_credentials=True)
add_apis()
api.init_app(app)
add_blueprints(app)
# //////////// create app end //////////// #

if __name__ == 'main':
    app.run(debug=True, port=8000)
    
