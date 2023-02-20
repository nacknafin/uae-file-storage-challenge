from app.types.files import FileData

def find_file_by_id(file_id: str, files_metadata: list[FileData]):
    for file_metadata in files_metadata:
        if file_metadata.id == file_id:
            return file_metadata
    return None
