from datetime import date

from pydantic import BaseModel


class FileData(BaseModel):
    id: str
    name: str
    file_type: str
    size: int | None
    created_at: date | None
    path: str | None
