from __future__ import annotations

import logging
from datetime import datetime
from typing import Any, Dict, List

from pymongo import MongoClient, ASCENDING
from pymongo.write_concern import WriteConcern
from pymongo.collection import Collection

from .config import AppConfig

logger = logging.getLogger(__name__)


class DatabaseClient:
    def __init__(self, config: AppConfig):
        self._config = config
        self._client = MongoClient(config.mongodb_uri, directConnection=False)
        self._db = self._client.get_database(
            config.database_name, write_concern=WriteConcern(w=config.write_concern)
        )
        self._collection: Collection = self._db[config.collection_name]
        self._ensure_indexes()
        logger.info("Connected to MongoDB %s", config.mongodb_uri)

    def _ensure_indexes(self) -> None:
        self._collection.create_index([("created_at", ASCENDING)])

    def insert_message(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload = {
            "message": payload.get("message", ""),
            "author": payload.get("author", "anonymous"),
            "created_at": datetime.utcnow(),
            "metadata": payload.get("metadata", {}),
        }
        result = self._collection.insert_one(payload)
        payload["_id"] = str(result.inserted_id)
        return payload

    def list_messages(self, limit: int) -> List[Dict[str, Any]]:
        cursor = self._collection.find().sort("created_at", -1).limit(limit)
        documents: List[Dict[str, Any]] = []
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            documents.append(doc)
        return documents

    def health(self) -> Dict[str, Any]:
        status = self._db.command("serverStatus")
        repl = status.get("repl", {})
        return {
            "ok": status.get("ok", 0) == 1,
            "setName": repl.get("setName"),
            "ismaster": repl.get("ismaster"),
            "secondary": repl.get("secondary"),
        }
