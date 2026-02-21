from __future__ import annotations

import logging
from http import HTTPStatus
from typing import Any, Dict

from flask import Blueprint, jsonify, request

from .config import AppConfig
from .db import DatabaseClient

logger = logging.getLogger(__name__)


def create_routes(config: AppConfig, db_client: DatabaseClient) -> Blueprint:
    bp = Blueprint("api", __name__)

    @bp.route("/api/v1/messages", methods=["GET"])
    def list_messages() -> Any:
        limit = request.args.get("limit", type=int) or config.default_limit
        limit = min(max(limit, 1), 500)
        logger.debug("Listing messages limit=%s", limit)
        messages = db_client.list_messages(limit=limit)
        return jsonify({"data": messages, "count": len(messages)})

    @bp.route("/api/v1/messages", methods=["POST"])
    def create_message() -> Any:
        payload: Dict[str, Any] = request.get_json(force=True) or {}
        inserted = db_client.insert_message(payload)
        return jsonify(inserted), HTTPStatus.CREATED

    @bp.route("/healthz", methods=["GET"])
    def healthcheck() -> Any:
        db_status = db_client.health()
        status = HTTPStatus.OK if db_status.get("ok") else HTTPStatus.SERVICE_UNAVAILABLE
        return jsonify({"status": "ok" if status == HTTPStatus.OK else "error", "db": db_status}), status

    @bp.route("/readyz", methods=["GET"])
    def readiness() -> Any:
        return jsonify({"status": "ready", "service": config.service_name})

    return bp
