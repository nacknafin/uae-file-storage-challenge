from datetime import date
from typing import Optional

from pydantic import BaseModel


class FileData(BaseModel):
    id: str
    name: str
    file_type: str
    size: Optional[int] = None
    created_at: Optional[date] = None
    path: Optional[str] = None
