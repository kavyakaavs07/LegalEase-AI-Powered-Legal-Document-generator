from fastapi import APIRouter, HTTPException

from google.genai import errors

from ai_core.generator import GeminiDocumentGenerator
from legalEaseAPI.schemas import GenerateRequest, GenerateResponse


router = APIRouter()

generator = GeminiDocumentGenerator()


@router.post("/generate", response_model=GenerateResponse)
def generate_document(request: GenerateRequest):
    try:
        document = generator.generate(request.prompt)

        return GenerateResponse(
            document=document
        )

    except errors.APIError as exc:
        if exc.code == 429:
            raise HTTPException(
                status_code=429,
                detail="Gemini API quota exceeded. Please try again later."
            )

        raise HTTPException(
            status_code=502,
            detail="Gemini API request failed."
        )