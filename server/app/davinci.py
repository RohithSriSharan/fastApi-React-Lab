import openai
from Test import products
import os
from dotenv import load_dotenv
from fastapi import APIRouter, Request

router = APIRouter()

load_dotenv()

# Set the API key
openai.api_key = os.getenv("OPEN_AI_KEY")

# Test the authentication
davinciPrompt = ""

@router.post('/davinciprompt')
async def promtreq(request: Request):
    response =await request.json()
    prompt = response["prompt"]
    print(prompt)
    global davinciPrompt
    davinciPrompt = prompt

    completions = openai.Completion.create(
        engine="text-curie-001",
        prompt=davinciPrompt,
        max_tokens=500,
    )

    front_end = completions["choices"][0]["text"]
    print(front_end)
    return front_end






