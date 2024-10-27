from fastapi import APIRouter
from infrastructure.api.controllers.rag_controller import RagController
from fastapi.responses import StreamingResponse
from fastapi.background import BackgroundTasks


rag_router = APIRouter(prefix="/rag", tags=["rag"])


rag_controller = RagController()


@rag_router.get("/query/")
async def query(q: str):
    try:
        vector_response = await rag_controller.search_vector(q)
        stream_generator = rag_controller.query_chat(q, vector_response)
        return StreamingResponse(stream_generator, media_type="text/event-stream")
    except Exception as e:
        print(e)
        return {"message": "Error querying chat"}
    finally:
        print("Query chat finished")