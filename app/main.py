from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional, List
from fastapi.responses import JSONResponse

app = FastAPI()


class Link(BaseModel):
    url: str
    text: str


class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None


class AnswerResponse(BaseModel):
    answer: str
    links: List[Link]


@app.post("/api/", response_model=AnswerResponse)
async def answer_question(request: QuestionRequest):
    # Dummy response for testing
    return {
        "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used..."
            }
        ]
    }
