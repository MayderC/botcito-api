from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.api.routes.documents_route import router as documents_router

app = FastAPI(title="Botcito API", version="0.1.0", description="A simple API to manage documents and LLms responses about them")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET", "DELETE"],
)


app.include_router(documents_router, prefix="/api")




