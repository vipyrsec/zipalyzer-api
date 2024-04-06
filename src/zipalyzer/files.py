"""Handle files and file contents."""

from hashlib import sha256
from io import BytesIO
from urllib.parse import unquote
from zipfile import ZipFile

import httpx

from zipalyzer.models.zip_information import File


async def get_zip_contents(path: str) -> dict[str, bytes]:
    """Get zip contents."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url=unquote(path))
    zip_file = ZipFile(BytesIO(response.content))
    return {name: zip_file.read(name) for name in zip_file.namelist()}


def process_zip_contents(files: dict[str, bytes]) -> list[File]:
    """Process zip file contents."""
    return [
        File(
            name=name,
            contents=contents,
            sha256_hash=sha256(contents).hexdigest(),
        )
        for name, contents in files.items()
    ]
