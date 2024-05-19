"""Zip information models."""

from pydantic.dataclasses import dataclass


@dataclass
class File:
    """A file in a zip."""

    name: str
    contents: bytes
    sha256_hash: str
