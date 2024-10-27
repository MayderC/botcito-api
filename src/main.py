from infrastructure.db.init_mongo import init_mongo, get_mongo_client_with_motor
from infrastructure.api.routes.documents_route import  doc_router
from infrastructure.api.routes.rag_route import rag_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request

import dotenv
import os

dotenv.load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = get_mongo_client_with_motor()
    print("Connecting to MongoDB")
    await init_mongo(client)
    yield
    client.close()



app = FastAPI(title="Botcito API", version="0.1.0", 
              description="A simple API to manage documents and LLms responses about them",
              lifespan=lifespan)


white_list = ["/docs", "/openapi.json", "/rag/query/"]

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    print(request.url.path)
    path = request.url.path
    if path in white_list:
        response = await call_next(request)
        return response

    api_key = request.headers.get("x-api-key")
    print(request.headers)
    print(request.url.path)
    # and if route is not /docs
    if not (api_key == os.getenv("X_API_KEY")):
        return JSONResponse(status_code=403, content={"message": "Invalid API Key"})
    response = await call_next(request)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("ALLOW_ORIGIN")],
    allow_methods=["POST", "GET", "DELETE"],
)






app.include_router(doc_router)
app.include_router(rag_router)





