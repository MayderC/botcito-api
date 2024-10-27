from application.lc_helper.handle_inputs import load_pdf, create_chuncks
from infrastructure.db.init_vector_db import get_mongo_collection
from adapter.mongo_repository import MongoRepository
class DocumentService():
    def __init__(self):
        self.mongo_repository = MongoRepository() 
        self.vector_repository = self.mongo_repository.VectorRepository()

    def get_document(self, document_id):
        return self.document_repository.get_document(document_id)

    async def save_document(self, temp_file_path, name):
        docs = load_pdf(temp_file_path)
        #for doc in docs: doc.metadata["source"] = name
        chunks = create_chuncks(docs, chunk_size=850, chunk_overlap=200)
        try:
            self.vector_repository.create(docs=chunks)
            await self.mongo_repository.create(name)
        except Exception as e:
            return {"message": "Error creating document"}

    def delete_document(self, document_id):
        return self.document_repository.delete_document(document_id)