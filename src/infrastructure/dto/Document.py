from pydantic import BaseModel

class DocumentDTO(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "example.pdf"
            }
        }