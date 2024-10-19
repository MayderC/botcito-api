

class DocumentsController:
    def __init__(self):
        pass

    def save_document(self, request):
        #self.documents_service.save(request)
        return "Document saved successfully"
    
    def get_document(self, request):
        #return self.documents_service.get(request)
        return "Document retrieved successfully"
    
    def delete_document(self, request):
        #self.documents_service.delete(request)
        return "Document deleted successfully"
    
    def list_documents(self):
        #return self.documents_service.list(request)
        return "Documents listed successfully"