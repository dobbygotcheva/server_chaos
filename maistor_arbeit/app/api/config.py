import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class AppConfig:
    mongodb_uri: str
    database_name: str = "cloud_native"
    collection_name: str = "messages"
    default_limit: int = 50
    write_concern: str = "majority"
    service_name: str = "cloud-native-api"
    environment: str = os.getenv("ENVIRONMENT", "local")
    enable_metrics: bool = True
    version: str = os.getenv("APP_VERSION", "0.1.0")


def load_config() -> AppConfig:
    uri = os.getenv(
        "MONGODB_URI",
        "mongodb://localhost:27017,localhost:27018,localhost:27019/?replicaSet=rs0",
    )
    database = os.getenv("MONGODB_DATABASE", "cloud_native")
    collection = os.getenv("MONGODB_COLLECTION", "messages")
    limit = int(os.getenv("API_DEFAULT_LIMIT", "50"))
    write_concern = os.getenv("MONGO_WRITE_CONCERN", "majority")

    return AppConfig(
        mongodb_uri=uri,
        database_name=database,
        collection_name=collection,
        default_limit=limit,
        write_concern=write_concern,
    )
