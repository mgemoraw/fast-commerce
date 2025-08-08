from pydantic import BaseModel, Field
from typing import List


class User(BaseModel):
   username: str
   password: str


class Student(BaseModel):
    id:int
    name:str =  Field(None, title="name of student", max_length=10)
    subjects: List[str] = []

