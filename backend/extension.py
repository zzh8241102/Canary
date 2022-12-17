from flask_sqlalchemy import SQLAlchemy

import logging
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()
# //////////// config the logger //////////// #
logger = logging.getLogger('Canary')
# info level 的也可见
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('canary.log',backupCount=500)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
# //////////// config the logger //////////// #
