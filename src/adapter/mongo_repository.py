
from infrastructure.db.models.document import DocumentModel 
from langchain_mongodb import MongoDBAtlasVectorSearch
from infrastructure.db.init_vector_db import get_mongo_collection
from application.lc_helper.handle_inputs import get_embedding_function



class MongoRepository:

    async def create(self, name: str):
        doc = DocumentModel(name=name)
        await doc.insert()

    async def get(self, id):
        doc = await DocumentModel.objects.get(id=id)
        return doc

    async def delete(self, id):
        return await DocumentModel.objects.delete(id=id)
    
    async def list(self):
        return await DocumentModel.objects.all()
    

    class VectorRepository:
        def __init__(self):
            self.collection = get_mongo_collection()
            self.embedding_function = get_embedding_function()
            self.vector_search = MongoDBAtlasVectorSearch(collection=self.collection, embedding=self.embedding_function)
        
        def create(self, docs):
            return self.vector_search.from_documents(
                documents=docs,
                embedding=self.embedding_function,
                collection=self.collection
            )
        
        def retrieve(self, collection):
            return self.vector_search.retrieve(collection=collection)
        
        async def search(self, query):
            retrive = self.vector_search.as_retriever(
                search_type="similarity",
                search_kwargs={'k': 3}
            )
            return await retrive.ainvoke(query)