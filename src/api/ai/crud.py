import requests
import pathlib
import textwrap
import google.generativeai as genai
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.deps import notes_list
from src.config import settings


async def summarize(session: AsyncSession):
    notes = await notes_list(session)
    if not notes:
        raise HTTPException(status_code=400,detail="No notes provided")

    text_to_summarize = "\n".join(notes)

    genai.configure(api_key=settings.env.GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Summarize the following notes: {text_to_summarize}")

    # payload = {
    #     "prompt": f"Summarize the following notes:\n{text_to_summarize}"
    # }
    # headers = {"Content-Type": "application/json"}
    # params = {"key": settings.env.GEMINI_API_KEY}

    # response = requests.post(settings.env.GEMINI_ENDPOINT,json=payload,headers=headers,params=params)

    # if response.status_code != 200:
    #     raise HTTPException(status_code=response.status_code,detail=response.text)
    #
    # result = response.json()
    # summary = result.get("candidates",[{}])[0].get("content",{}).get("parts",[{}])[0].get("text","No summary generated")

    return {"response": response.text}