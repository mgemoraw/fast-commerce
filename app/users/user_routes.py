
from fastapi import APIRouter, Depends, HTTPException
from .schemas import Student

router = APIRouter()

@router.post("/students/", response_model=Student)
def create_student(student: Student):
    return student


@router.post("/students/{college}")
async def student_data(college:str, age:int, student:Student):
    retval={"college":college, "age":age, **student.dict()}
    return retval