from io import BytesIO
from typing import Annotated
from infrastructure.db.models.document import DocumentModel 
from application.services.documents_service import DocumentService
from fastapi import UploadFile, Response, Depends
from langchain_community.document_loaders import PyPDFLoader
from infrastructure.api.helper.files_helper import valid_file
import os

class DocumentsController:
    def __init__(self):
        self.document_service = DocumentService()

    async def save_document(self, request: UploadFile):

        temp_file_path = valid_file(request)
        await self.document_service.save_document(temp_file_path, request.filename)

        os.remove(temp_file_path)

        return Response(status_code=201, content="Document saved successfully")
    
    def get_document(self, request):
        #return self.documents_service.get(request)
        return "Document retrieved successfully"
    
    def delete_document(self, request):
        #self.documents_service.delete(request)
        return "Document deleted successfully"
    
    def list_documents(self):
        #return self.documents_service.list(request)
        return "Documents listed successfully"