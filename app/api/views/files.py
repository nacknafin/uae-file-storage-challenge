import os
import uuid
import shutil


from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

from app.types.files import FileData
from app.service.find_file import find_file_by_id
from settings import FILE_STORAGE_PATH


router = APIRouter()
files_metadata: list[FileData] = []


@router.post(
    path="",
    summary="Uploads files into storage"
)
def create_files(
    files: list[UploadFile] = File(description="Multiple files as UploadFile", default=[])
):
    '''
    Uploads file to a storage
    Parameters:
    - file: the file to be uploaded.

    Returns:
    - files_metadata: tuple which contains (file name, file id)
    '''

    for file in files:
        file_path = os.path.join(FILE_STORAGE_PATH, file.filename)

        try:
            with open(file_path, 'wb') as file_obj:
                shutil.copyfileobj(file.file, file_obj)

            file_name, file_type = os.path.splitext(file.filename)
            file_id = str(uuid.uuid4())
            file_size = os.stat(file_path).st_size
            file_created_at = os.path.getctime(file_path)

            files_metadata.append(FileData(
                id=file_id,
                name=file_name,
                file_type=file_type,
                size=file_size,
                created_at=file_created_at,
                path=file_path,
            ))
        except IOError:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": f"Successfully uploaded {[(file.filename, file_id) for file in files]}"}


@router.get(
    path="",
    summary="List all uploaded files ids with names"
)
async def get_files_list():
    """
    Returns a list of dictionaries, each representing an uploaded file with the following keys:
    - "id":  id of the file.
    - "name": file name.
    - "file_type": file type.
    """
    return [
        {
            "id": file_metadata.id,
            "name": file_metadata.name,
            "file_type": file_metadata.file_type,
        }
        for file_metadata in files_metadata
    ]


@router.get(
    path="/{file_id}",
    summary="Downloads file by set file id"
)
async def download_file(file_id: str):
    file_metadata =  find_file_by_id(file_id, files_metadata)
    if not file_metadata:
        raise HTTPException(status_code=404, detail="File not found")

    file_path = os.path.join(
        FILE_STORAGE_PATH,
        file_metadata.name + file_metadata.file_type
    )

    return FileResponse(file_path)


@router.head(
    path="/{file_id}",
    summary="Returns information about the file by file_id",
    response_model=FileData,
)
async def retrieve_file_info(file_id: str) -> FileData:
    file_metadata =  find_file_by_id(file_id, files_metadata)
    if not file_metadata:
        raise HTTPException(status_code=404, detail="File not found")
    return FileData(
                id=file_id,
                name=file_metadata.name,
                file_type=file_metadata.file_type,
                size=file_metadata.size,
                created_at=file_metadata.created_at,
                path=file_metadata.path,
            )
