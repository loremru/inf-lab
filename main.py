from fastapi import FastAPI
from encode import encode_word

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/encode/{word}")
def read_item(word: str):
    return {"word": encode_word(word)}