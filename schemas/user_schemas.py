from pydantic import BaseModel, EmailStr, Field
# from models.user import UserRole


# Register request body
#
# Example:
# {
#   "name":"Pardeep",
#   "email":"abc@gmail.com",
#   "password":"123456"
# }
class UserCreate(BaseModel):
    name: str = Field(min_length=2,max_length=80)
    email: EmailStr
    password: str = Field(
        min_length=6,
        max_length=72
    )

# Login request body
#
# Example:
# {
#   "email":"abc@gmail.com",
#   "password":"123456"
# }
class Login(BaseModel):
    email: EmailStr
    password: str


# Response schema
class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        from_attributes = True
