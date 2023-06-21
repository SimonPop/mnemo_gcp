from docarray import Document, DocumentArray
from finding_mnemo.pairing.utils.ipa import mandarin_ipa_to_en, convert_mandarin_to_ipa
# from finding_mnemo.text_generation.generation.text_generator import TextGenerator
from finding_mnemo.pairing.search.engine import Engine
from finding_mnemo.pairing.search.indexer import Indexer

class SearchHandler():

    def __init__(self):
        self.indexer = Indexer()
        documents = self.indexer.index()
        self.engine = Engine(documents, n_limit=1000)

    def search(self, word: str) -> DocumentArray:
        """Search the closest sounding word from given word.
        
        Args:
            word (str): Pinyin word.

        Returns:
            _type_: _description_
        """
        ipa: str = convert_mandarin_to_ipa(word)
        input = DocumentArray(Document(text=word, ipa=mandarin_ipa_to_en(ipa)))
        return self.engine.search(input)
    
    def unpack(self, search_result: DocumentArray, word: str):
        print(word, convert_mandarin_to_ipa(word), mandarin_ipa_to_en(convert_mandarin_to_ipa(word)))
        distances = self.engine.get_distance(search_result, mandarin_ipa_to_en(convert_mandarin_to_ipa(word)))
        docs_dict = search_result.to_dict()
        print([(x['tags']['ipa'], d) for d, x in zip(distances, docs_dict[0]["matches"])])
        # scores = [match["scores"]["euclidean"]["value"] for x in docs_dict for match in x['matches']]
        matches = [match["text"] for x in docs_dict for match in x['matches'] ]

        # Sort by distance
        sorted_matches = [x for _,x in sorted(zip(distances,matches))]
        sorted_distances = sorted(distances)
        return sorted_matches[:10], sorted_distances[:10]

    @staticmethod
    def score2emoji(score: float):
        if score <= 0.34:
            return ":tropical_fish:"
        elif score <= 0.5:
            return ":fish:"
        else:
            return ":blowfish:"
        
