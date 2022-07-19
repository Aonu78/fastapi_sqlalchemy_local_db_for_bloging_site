# from http.client import HTTPException
from sqlite3 import dbapi2
from turtle import title
from fastapi import FastAPI, Depends,HTTPException,status,Response
from sqlalchemy.orm import Session
from fastapi import FastAPI
import schemas, models
from database import SessionLocal, engine
app = FastAPI()

models.Base.metadata.create_all(engine) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/")
def create(title,body):
    return {title:"tile",body:"body"}

@app.post('/blog/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session =Depends(get_db)):
    new_blog = models.Blog(title= request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    db.close()
    return new_blog

@app.get('/blog')
def all_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def show(id,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog not with id {id} not found...')
        # responc{'details':f'blog not with id {id} not found...'}
    return blog

@app.delete('/blog/{id}')
def destroy(id,db:Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return 'done' 

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'detail with id {id} not found')
    blog.update(request)
    db.commit()
    return {'updated'}