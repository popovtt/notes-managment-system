import google.generativeai as genai
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.deps import notes_list
from src.config import settings


async def summarize(note_title: str):
    # notes = await notes_list(session)
    # if not notes:
    #     raise HTTPException(status_code=400,detail="No notes provided")
    #
    # text_to_summarize = "\n".join(notes)

    genai.configure(api_key=settings.env.GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Summarize the following note: {note_title}")

    return response.text