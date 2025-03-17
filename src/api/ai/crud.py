import google.generativeai as genai

from src.config import settings


async def summarize(note_title: str):
    genai.configure(api_key=settings.env.GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Summarize the following note: {note_title}")

    return response.text
