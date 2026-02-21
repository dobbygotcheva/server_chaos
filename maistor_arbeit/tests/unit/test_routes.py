import json
from unittest.mock import MagicMock

from app.api.config import AppConfig
from app.api.routes import create_routes


def build_app():
    from flask import Flask

    config = AppConfig(mongodb_uri="mongodb://example")
    db = MagicMock()
    db.list_messages.return_value = []
    db.insert_message.return_value = {"message": "hello"}

    app = Flask(__name__)
    app.register_blueprint(create_routes(config, db))
    return app, db


def test_list_messages_returns_ok():
    app, db = build_app()
    client = app.test_client()

    response = client.get("/api/v1/messages")

    assert response.status_code == 200
    data = response.get_json()
    assert data["count"] == 0
    db.list_messages.assert_called_once()


def test_create_message_calls_db_insert():
    app, db = build_app()
    client = app.test_client()

    response = client.post(
        "/api/v1/messages",
        data=json.dumps({"message": "hi"}),
        content_type="application/json",
    )

    assert response.status_code == 201
    db.insert_message.assert_called_once()
