from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime

class Todo(BaseModel):
    title: str = Field(..., min_length=20, max_length=555, description="Titre de votre todo")
    desc:  str = Field(..., max_length=1000, description="La description de votre todo")

    class Config:
        schema_extre = {
            'Todo': {
                'title':'Learn FastAPI',
                'desc': "Apprendre a développer rapidement ",
            }
        }
