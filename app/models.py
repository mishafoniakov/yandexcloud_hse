from pydantic import BaseModel, Field, field_validator, constr
from typing import Optional
import re

class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)

class Contact(BaseModel):
    email: str = Field(pattern=r'^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]{2}$')
    phone: Optional[str] = Field(None, pattern=r'^\d{7,10}$')

class SimpleResponse(BaseModel):
    message: str
    
class FeedBack(BaseModel):
    username: User
    feedback_text: str = Field(
        min_length=10,
        max_length=500)
    contact: Contact
    is_premium: bool
    
    @field_validator("feedback_text")
    def words_validator(value):
        regex = r"(редиск[a-яё]+|бяк[a-яё]+|козяв[a-яё]+)"
        if re.search(regex, value.lower()):
            raise ValueError("Использование недопустимых слов")
        return value