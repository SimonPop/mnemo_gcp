from chinese_english_lookup import Dictionary
import dragonmapper

class InputHandler():
    def __init__(self) -> None:
        self.dictionary = Dictionary()

    def translate(self, pinyin: str):
        lookup = self.dictionary.lookup(pinyin)
        if lookup is not None:
            translation = lookup.definition_entries[0].definitions[0].split('(')[0]
        else:
            translation = "No translation available in lookup table."
        return translation

    def input_to_pinyin(self, input: str):
        if dragonmapper.transcriptions.is_pinyin(input):
            return input
        else:
            return dragonmapper.hanzi.to_pinyin(input)