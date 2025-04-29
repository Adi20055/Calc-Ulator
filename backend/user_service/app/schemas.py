from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: Optional[bool] = None
    is_teacher: Optional[bool] = None

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    disabled: Optional[bool] = None
    is_teacher: Optional[bool] = None

    class Config:
        from_attributes = True

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Topic schemas
class TopicBase(BaseModel):
    name: str
    description: str
    subject: str
    difficulty: int
    estimated_time: float

    class Config:
        from_attributes = True

class TopicCreate(TopicBase):
    pass

class Topic(TopicBase):
    id: int

    class Config:
        from_attributes = True

# Progress schemas
class ProgressBase(BaseModel):
    status: str
    completion_date: Optional[datetime] = None
    score: Optional[float] = None

    class Config:
        from_attributes = True

class ProgressCreate(ProgressBase):
    topic_id: int

class Progress(ProgressBase):
    id: int
    student_id: int
    topic_id: int
    topic: Topic

    class Config:
        from_attributes = True

# Response schemas
class StudentProgress(BaseModel):
    student: User
    progress: List[Progress]

class TopicProgress(BaseModel):
    topic: Topic
    progress: List[Progress] 