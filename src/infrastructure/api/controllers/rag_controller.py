from application.services.llm_service import LlmService
import asyncio



class RagController():
    def __init__(self):
        self.rag_service = LlmService()

    async def search_vector(self, query: str):
        return await self.rag_service.search_vector(query)

    async def query_chat(self, query: str, vector_response):
        stream_generator = self.rag_service.query_chat(
            f"Eres un asistente, para contestar preguntas sobre el desarrollador Mayder,  contesta la pregunta :{query} con el contexto {vector_response} si no sabes la respuesta, puedes decir no se, si no entiendes la pregunta puedes decir no entiendo la pregunta, si el tema se sale de contexto, puedes decir que solo puedo hablar de Mayder por el momento"
        )
        try:
            async for stream in stream_generator:
                yield stream.content
                if stream.response_metadata.get('finish_reason') == 'stop':
                    break
        except asyncio.CancelledError:
            print("Streaming was cancelled")
        except Exception as e:
            print(f"Error in query_chat: {e}")
        finally:
            print("Stream closed from controller")