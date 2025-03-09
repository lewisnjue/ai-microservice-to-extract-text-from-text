from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/') # http get 
async def home_View():
    return {"hello":"world"}

@app.post('/') # http post 
async def home_detail_view():
    return {"hello": "world"}
