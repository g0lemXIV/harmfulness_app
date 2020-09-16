import secrets
from typing import Optional

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

from backend.core import settings
from backend.core.messages import AUTH_REQ, NO_API_KEY

api_key_handler = APIKeyHeader(name="token", auto_error=False)


def validate_request(header: Optional[str] = Security(api_key_handler)):
    if header is None:
        raise HTTPException(status_code=400, detail=NO_API_KEY, headers={})
    if not secrets.compare_digest(header, str(settings.auth_key)):
        raise HTTPException(status_code=401, detail=AUTH_REQ, headers={})
    return True
