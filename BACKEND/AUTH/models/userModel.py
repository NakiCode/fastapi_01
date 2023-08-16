from typing import Optional
from pydantic import BaseModel, Field, EmailStr, validator
from email_validator import validate_email, EmailNotValidError
from pydantic_extra_types.phone_numbers import PhoneNumber

class UserSchema(BaseModel):
    name: str = Field(..., min_length=4, max_length=32, description="Votre nom d'utilisateur")
    email: EmailStr 
    password: str = Field(..., min_length=6, regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$")
    phone: PhoneNumber

    @validator('email')
    def varify_email(cls, email):
        try:
            emailinfo = validate_email(email, check_deliverability=False)
            email = emailinfo.normalized
            return email
        except EmailNotValidError as e:
            return e
        
    class Config:
        schema_extre = {
            'Users': {
                'name':'kabika',
                'email': 'kabika07@gmail.com',
                'phone': '+25766320871',
                'password': 'NakiCode0707@'
            }
        }

class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    password: Optional[str]

    class Config:
        schema_extre = {
            'Users': {
                'name':'kabika',
                'email': 'kabika07@gmail.com',
                'phone': '+25766320871',
                'password': 'NakiCode0707@'
            }
        }

