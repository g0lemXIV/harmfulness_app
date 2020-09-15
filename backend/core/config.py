from pathlib import Path
from typing import Set
import os

from pydantic import (
    BaseSettings,
    Field,
)

_PROJECT_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    project_dir: str = str(_PROJECT_DIR)
    debug: bool
    api_version: str = 'v1'
    access_token_expire_minutes: int = 60*24*8
    auth_key: str
    api_key_gcp: str = Field(..., env='api_key_gcp')
    port: int = 8080
    model_name: str

    class Config:
        env_file = os.path.join(_PROJECT_DIR, '.env')
        env_file_encoding = 'utf-8'


# make settings avaliable
settings = Settings(_env_file=os.path.join(_PROJECT_DIR, '.env'))