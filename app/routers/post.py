from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..database import engine, SessionLocal, get_db
from typing import List

router=APIRouter(prefix="/posts", tags=['Posts'])

@router.get("/", response_model=List[schemas.PostResponse])
def get_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    # cursor.execute("""SELECT * FROM posts""")
    # posts=cursor.fetchall()
    return posts

@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id=%s """,(str(id)))
    # post=cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
    return post
    
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING * """,(post.title, post.content, post.published))
    # new_post=cursor.fetchone()
    # conn.commit()
    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id=%s RETURNING *""",(str(id),))
    # deleted_post=cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}")
def put_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute(""" UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING * """,(post.title, post.content, post.published, str(id)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    posts=post_query.first()
    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()