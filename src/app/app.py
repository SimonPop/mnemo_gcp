from fastapi import FastAPI
from docarray import Document, DocumentArray

from src.pairing.search.engine import Engine
from src.pairing.search.indexer import Indexer

from src.pairing.utils.ipa import convert_mandarin_to_ipa

app = FastAPI()

indexer = Indexer()
documents = indexer.index()

engine = Engine(documents)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/search/{word}/")
def search(word: str):
    """Search the closest sounding word from given word.
    
    Args:
        word (str): Pinyin word.

    Returns:
        _type_: _description_
    """
    ipa: str = convert_mandarin_to_ipa(word)
    input = DocumentArray(Document(text=word, ipa=ipa))
    return engine.search(input).to_dict()