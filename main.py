import os
from dotenv import load_dotenv
from urllib.parse import urlparse
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import weaviate
from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
import time

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
WEAVIATE_URI = os.getenv("WEAVIATE_URI")

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

def parse_weaviate_uri(uri):
    """Parse and validate the Weaviate URI."""
    parsed = urlparse(uri)
    if not parsed.hostname:
        raise ValueError(f"Invalid WEAVIATE_URI: {uri}")
    return {
        "http_host": parsed.hostname,
        "http_port": parsed.port or 8080,
        "grpc_host": parsed.hostname,
        "grpc_port": 50051,
    }

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    try:
        # MongoDB connection
        with MongoClient(MONGO_URI) as mongo_client:
            db = mongo_client["star_rise"]
            mongo_client.admin.command("ping")
            logger.info("✅ Connected to MongoDB")

            # Weaviate connection with retry logic
            weaviate_config = parse_weaviate_uri(WEAVIATE_URI)
            max_retries = 10
            retry_delay = 1.5
            weaviate_client = None

            for attempt in range(max_retries):
                try:
                    with weaviate.connect_to_custom(
                        **weaviate_config,
                        http_secure=False,
                        grpc_secure=False,
                        auth_credentials=None,
                    ) as client:
                        if client.is_ready():
                            logger.info("✅ Connected to Weaviate")
                            weaviate_client = client
                            break
                        else:
                            logger.warning(f"Weaviate not ready (attempt {attempt + 1}/{max_retries}), retrying...")
                except Exception as e:
                    logger.warning(f"Retry {attempt + 1}/{max_retries} failed: {e}")
                time.sleep(retry_delay)  # Synchronous sleep

            if weaviate_client is None:
                raise weaviate.exceptions.WeaviateConnectionError("Weaviate is not ready after multiple retries!")

            yield  # Yield control back to FastAPI

    except ConnectionFailure as e:
        logger.error(f"❌ MongoDB connection failed: {e}")
        raise
    except weaviate.exceptions.WeaviateConnectionError as e:
        logger.error(f"❌ Weaviate connection failed: {e}")
        raise

# Assign lifespan to FastAPI app
app = FastAPI(lifespan=app_lifespan)

@app.get("/")
async def root():
    return {"message": "Star Rise Campaign System is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
