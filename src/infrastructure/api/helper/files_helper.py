from fastapi import UploadFile
import tempfile

def read_document(upload: UploadFile):
    print("Reading document")
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp:
        temp.write(upload.file.read())
        temp_file_path = temp.name
    return temp_file_path


def valid_file(file: UploadFile):
    print("Validating file")
    ONE_MB_IN_KB = 1024
    LIMIT_SIZE_MB = 10
    print(file.size/ ONE_MB_IN_KB)
    kb_size = file.size / ONE_MB_IN_KB
    mb_size = kb_size / ONE_MB_IN_KB
    name = file.filename
    name = name.lower()
    
    if not name.endswith(".pdf"):
        raise ValueError("Only PDF files are allowed")
    
    if mb_size > LIMIT_SIZE_MB:
        raise ValueError(f"File size exceeds the limit of {LIMIT_SIZE_MB} MB")
    
    return read_document(file)