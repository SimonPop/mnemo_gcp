from docarray import Document, DocumentArray
from finding_mnemo.pairing.utils.ipa import convert_mandarin_to_ipa
# from finding_mnemo.text_generation.generation.text_generator import TextGenerator
from finding_mnemo.pairing.search.engine import Engine
from finding_mnemo.pairing.search.indexer import Indexer

class SearchHandler():

    def __init__(self):
        self.indexer = Indexer()
        documents = self.indexer.index()
        self.engine = Engine(documents)

    def search(self, word: str) -> dict:
        """Search the closest sounding word from given word.
        
        Args:
            word (str): Pinyin word.

        Returns:
            _type_: _description_
        """
        ipa: str = convert_mandarin_to_ipa(word)
        input = DocumentArray(Document(text=word, ipa=ipa))
        return self.engine.search(input).to_dict()
    
    def unpack(self, search_result: dict):
        matches = [match["text"] for x in search_result for match in x['matches'] ]
        scores = [match["scores"]["euclidean"]["value"] for x in search_result for match in x['matches'] ]
        return matches, scores

    @staticmethod
    def score2emoji(score: float):
        if score < 0.01:
            return ":tropical_fish:"
        elif score < 0.05:
            return ":fish:"
        else:
            return ":blowfish:"
        
