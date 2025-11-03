from fastapi import APIRouter, HTTPException
from typing import List
from models.quiz import UserInputModel, QuestionResponseModel
from services.quiz_generator import generate_quiz_from_text
from services.url_parser import get_text_from_url

router = APIRouter()

@router.post("/generate", response_model=List[QuestionResponseModel])
async def generate_quiz(input_data: UserInputModel):
    if input_data.text:
        return generate_quiz_from_text(input_data.text)
    elif input_data.url:
        text = get_text_from_url(input_data.url)
        if not text:
            raise HTTPException(status_code=400, detail="Could not fetch content from the provided URL.")
        return generate_quiz_from_text(text)

    raise HTTPException(status_code=400, detail="Either text or a URL must be provided.")
