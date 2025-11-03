from pydantic import BaseModel
from typing import List, Optional, Literal

class UserInputModel(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None

class MultipleChoiceQuestion(BaseModel):
    question_type: Literal["multiple_choice"]
    question_text: str
    choices: List[str]
    correct_answer: str
    explanation: str

class TrueFalseQuestion(BaseModel):
    question_type: Literal["true_false"]
    question_text: str
    correct_answer: bool
    explanation: str

class DescriptiveQuestion(BaseModel):
    question_type: Literal["descriptive"]
    question_text: str
    correct_answer: str
    explanation: str

QuestionResponseModel = MultipleChoiceQuestion | TrueFalseQuestion | DescriptiveQuestion
