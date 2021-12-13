from fastapi import FastAPI
from encode import encode_word
app = FastAPI()


@app.get("/encode/{word}")
def read_item(word: str):
    return {"word": encode_word(word)}