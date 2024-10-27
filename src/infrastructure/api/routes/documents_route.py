from fastapi.routing import APIRouter
from fastapi import HTTPException, UploadFile
from infrastructure.api.controllers.documents_controller import DocumentsController


documen_controller = DocumentsController()

doc_router = APIRouter(prefix="/documents", tags=["documents"])


@doc_router.post("/")
async def save_document(request:UploadFile):
    try:
        return await documen_controller.save_document(request)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str('Error saving document'))


@doc_router.get("/{id}")
async def get_document(request):
    try:
        return documen_controller.get_document(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str('Error retrieving document'))


@doc_router.delete("/")
async def delete_document(request):
    try:
        return documen_controller.delete_document(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str('Error deleting document'))


@doc_router.get("/")
async def list_documents():
    try:
        return documen_controller.list_documents()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str('Error listing documents'))

