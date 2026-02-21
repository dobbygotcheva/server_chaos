from __future__ import annotations

import logging
import os

from flask import Flask
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

from .config import load_config
from .db import DatabaseClient
from .routes import create_routes

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)


def create_app() -> Flask:
    config = load_config()
    app = Flask(__name__)
    CORS(app)

    db_client = DatabaseClient(config)
    routes = create_routes(config, db_client)
    app.register_blueprint(routes)

    if config.enable_metrics:
        PrometheusMetrics(app, group_by="endpoint")

    @app.route("/")
    def index() -> str:
        return "Cloud Native API running"

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
