from math import fabs
from turtle import title
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()
@app.get('/')
def about():
    return {'My Name is Aoun'}

@app.get('/blog')
def unpublished(limit,published:bool,sort:Optional[str]):
    if published:
        return {'data':f'{limit} published blogs from data'}
    else:
        return {'data',f'{limit} unpublished'}

@app.get('/blog/{id}')
def show(id: int):
    return {"Aoon": id}


@app.get('/blog/{id}/commints')
def commints(id):
    return {"Aoon": {'1','2'}}


class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]
@app.post('/blog')
def creat_blog(request:Blog):
    return {f'bloger was created with user title {request.title}'}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")