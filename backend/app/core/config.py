# Config
# ilya_bisec
# Date: 25/08/2026 14:48

import os

class Settings:
    SECRET_KEY = "supersecret"
    ALGORITHM = "HS256"

    DB_URL = "postgresql://user:password@db:5432/aerokite"

    S3_ENDPOINT_URL = "http://minio:9000"
    S3_ACCESS_KEY = "minioadmin"
    S3_ACCESS_SECRET = "minioadmin"
    S3_BUCKET = "files"

settings = Settings()