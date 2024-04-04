"""Model definitions."""

from pydantic import BaseModel


class ServerMetadata(BaseModel):
    """Metadata about the server."""

    version: str
    server_commit: str
