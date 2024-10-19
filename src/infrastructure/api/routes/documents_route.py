from fastapi.routing import APIRouter
from fastapi import HTTPException
from infrastructure.api.controllers.documents_controller import DocumentsController


router = APIRouter(prefix="/documents", tags=["documents"])
documen_controller = DocumentsController()



@router.post("/")
async def save_document(request):
    try:
        return documen_controller.save_document(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str('Error saving document'))


@router.get("/{id}")
async def get_document(request):
    try:
        return documen_controller.get_document(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str('Error retrieving document'))


@router.delete("/")
async def delete_document(request):
    try:
        return documen_controller.delete_document(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str('Error deleting document'))


@router.get("/")
async def list_documents():
    try:
        return documen_controller.list_documents()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str('Error listing documents'))