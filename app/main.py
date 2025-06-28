from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)



while True:
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='root',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("DataBase Connection Was Successfull")
        break
    except Exception as error:
        print("Connecting to Database Failed")
        print("Error: ",error)
        time.sleep(2)
app = FastAPI()
my_post=[{"title": "this is first title","content": "this is first content","id": 1},{"title": "this is second title","content": "this is second content","id": 2}]

def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p
def findex(id: int):
    for i,p in enumerate(my_post):
        if p['id'] ==id:
            return i        

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
