"""Routes for zip handling."""

from fastapi import APIRouter

from zipalyzer.files import get_zip_contents, process_zip_contents
from zipalyzer.models.zip_information import File

router = APIRouter(prefix="/zips", tags=["Zips"])


@router.get("/{path:path}", summary="Get zip information")
async def zip_info(path: str) -> list[File]:
    """Get zip information."""
    contents = await get_zip_contents(path)
    return process_zip_contents(contents)
