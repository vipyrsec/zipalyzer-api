"""Core information routes."""

from fastapi import APIRouter

from zipalyzer import __version__
from zipalyzer.constants import GIT_SHA
from zipalyzer.models import ServerMetadata

router = APIRouter(tags=["Metadata"])


@router.get("/", summary="Get the server's metadata")
async def metadata() -> ServerMetadata:
    """Get server metadata."""
    return ServerMetadata(
        version=__version__,
        server_commit=GIT_SHA,
    )
