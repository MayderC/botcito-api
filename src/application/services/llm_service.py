from adapter.mongo_repository import MongoRepository
from application.lc_helper.handle_inputs import get_llm
import asyncio
class LlmService:
    def __init__(self):
        self.mongo_repository = MongoRepository() 
        self.vector_repository = self.mongo_repository.VectorRepository()

    async def search_vector(self, query):
        return await self.vector_repository.search(query)

    async def query_chat(self, query):
        llm = get_llm()
        stream_generator = llm.astream(query)
        try:
            async for stream in stream_generator:
                yield stream
                if stream.response_metadata.get('finish_reason') == 'stop':
                    break
        except asyncio.CancelledError:
            print("Streaming was cancelled")
        finally:
            await stream_generator.aclose()
            print("Stream closed from service")