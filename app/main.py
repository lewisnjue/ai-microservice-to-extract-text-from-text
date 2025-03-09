from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pathlib
import os
app = FastAPI()
BASE_DIR = pathlib.Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(BASE_DIR/'templates'))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/',response_class=HTMLResponse) # http get
async def home_View(request:Request):
    return  templates.TemplateResponse('home.html',{"request":request})

@app.post('/') # http post
async def home_detail_view():
    return {"hello": "world"}
