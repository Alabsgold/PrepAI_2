import os
import json
from typing import List

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from models.quiz import QuestionResponseModel, MultipleChoiceQuestion, TrueFalseQuestion, DescriptiveQuestion

from dotenv import load_dotenv

load_dotenv()

# Set the API key from environment variable
google_api_key = os.getenv("GOOGLE_API_KEY")

class Quiz(BaseModel):
    questions: List[QuestionResponseModel] = Field(description="A list of quiz questions of different types.")

def generate_quiz_from_text(text: str) -> List[QuestionResponseModel]:
    """
    Generates a quiz from the given text using Google's Gemini LLM.
    """
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)

    parser = PydanticOutputParser(pydantic_object=Quiz)

    prompt = PromptTemplate(
        template="""
        You are an expert quiz maker. Given the following text, create a quiz with a mix of multiple-choice, true/false, and descriptive questions.

        For multiple-choice questions, provide a question, a list of 4 choices, the correct answer, and a brief explanation.
        For true/false questions, provide a statement, the correct boolean answer, and a brief explanation.
        For descriptive questions, provide a question, a correct answer, and a brief explanation.

        {format_instructions}

        Here is the text:
        {text}
        """,
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    chain = prompt | llm | parser

    try:
        quiz = chain.invoke({"text": text})
        return quiz.questions
    except Exception as e:
        # Handle potential errors during LLM call or parsing
        print(f"Error generating quiz: {e}")
        return []
