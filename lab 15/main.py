from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

class ArticleRequest(BaseModel):
    title: str

class ArticleResponse(BaseModel):
    title: str
    summary: str


@app.get("/article/{title}", response_model=ArticleResponse)
def get_article_by_title(title: str):
    summary = wikipedia.summary(title)
    return {"title": title, "summary": summary}


@app.get("/search", response_model=ArticleResponse)
def search_article(query: str):
    page = wikipedia.page(query)
    return {"title": page.title, "summary": page.summary}


@app.post("/create", response_model=ArticleResponse)
def create_article(request: ArticleRequest):
    summary = wikipedia.summary(request.title)
    return {"title": request.title, "summary": summary}