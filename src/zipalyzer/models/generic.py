"""Model definitions."""

from pydantic import BaseModel


class Message(BaseModel):
    """A message."""

    detail: str
