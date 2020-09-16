from pathlib import Path
import os

from pydantic import (
    BaseSettings,
    Field,
)

_PROJECT_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    project_dir: str = str(_PROJECT_DIR)
    debug: bool = True
    api_version: str = "v1"
    access_token_expire_minutes: int = 60 * 24 * 8
    auth_key: str = "test"
    api_key_gcp: str = "test"
    port: int = 8080
    model_name: str = "regression_pipeline_exp0"
    spacy_corpus: str = "pl_core_news_sm"
    sentence_min_length: int = 10

    class Config:
        env_file = os.path.join(_PROJECT_DIR, ".env")
        env_file_encoding = "utf-8"


# make settings available
settings = Settings(_env_file=os.path.join(_PROJECT_DIR, ".env"))
