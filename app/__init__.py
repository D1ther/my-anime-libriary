from flask import (
    Flask
)

app = Flask(__name__,
            template_folder='frontend/templates',
            static_folder='frontend/static')

app.secret_key = 'ndajjandbakjdakjdndandadandankdna'

from app.frontend.routes import *
from app.backend.routes import *

def main():
    app.run(port=5000, host='0.0.0.0', debug=True)