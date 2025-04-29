from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
    is_teacher = Column(Boolean, default=False)  # New field for role-based access

    # Relationships
    progress = relationship("Progress", back_populates="student")

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    subject = Column(String)  # "calculus" or "linear_algebra"

    # Relationships
    progress = relationship("Progress", back_populates="topic")

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    topic_id = Column(Integer, ForeignKey("topics.id"))
    status = Column(String)  # "not_started", "in_progress", "completed"
    completion_date = Column(DateTime, nullable=True)
    score = Column(Float, nullable=True)  # For future quiz implementation

    # Relationships
    student = relationship("User", back_populates="progress")
    topic = relationship("Topic", back_populates="progress") 