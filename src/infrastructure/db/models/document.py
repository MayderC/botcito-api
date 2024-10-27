from bson import ObjectId
from pydantic import  Field
from typing import Optional
from beanie import Document, Indexed


class DocumentModel(Document):
    id : Optional[str] = Field(None, alias="_id") # type: ignore
    name: Indexed(str, unique=True) # type: ignore

    class Settings:
        collection = "documents"
    
    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "name": "example.pdf"
            }
        }
