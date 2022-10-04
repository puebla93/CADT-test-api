"""CADT test APP.
"""

from flask import Flask
from flask_cors import CORS

from api import api_bp as api_router


API_VERSION = "v1"
app = Flask("CADT test API")
app.register_blueprint(api_router, url_prefix=f"/api/{API_VERSION}")
CORS(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
