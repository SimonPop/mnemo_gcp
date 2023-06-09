from finding_mnemo.text_generation.generation.text_generator import TextGenerator
import re

class KeyPhraseHandler():
    def __init__(self):
        self.text_generator = TextGenerator(model_type="t5")

    @staticmethod
    def key_prhase_to_html(key_phrase: str, match: str, translation: str) -> str:
        return "<p>" + re.sub(f'({match}|{translation})', r'<b>\g<1></b>', key_phrase) + "</p>"

    def generate(self, match, translation, prompt) -> str:
        key_phrases = self.text_generator.generate(keywords=[match, translation], prompt=prompt)
        html_key_phrase = [self.key_prhase_to_html(key_phrase, match, translation) for key_phrase in key_phrases] 
        return html_key_phrase