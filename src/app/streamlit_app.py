import streamlit as st
from input_handler import InputHandler
from search_handler import SearchHandler
from summary_table import SummaryTable
from key_phrase_handler import KeyPhraseHandler
from style import STYLE

input_handler = InputHandler()
search_handler = SearchHandler()
key_phrase_handler = KeyPhraseHandler()

def read_style():
    st.markdown(STYLE, unsafe_allow_html=True)

def display_candidates(response, translation, pinyin):
    legend = ':tropical_fish: - Definitely Mnemo / :fish: - Not exactly Mnemo / :blowfish: - Barely Mnemo'
    matches, scores = search_handler.unpack(response)
    emojis = [SearchHandler.score2emoji(x) for x in scores]

    for index, (match, emoji) in enumerate(zip(matches, emojis)):
        key = f"generator_{index}"

        with st.expander(f"{emoji} - {match}"):
            with st.form(key=key):
                prompt = st.text_input("Key-phrase prompt: ", value="It is said that ")
                submit = st.form_submit_button(":sparkles: Generate key-phrase!")

            if submit:
                html_key_phrases = key_phrase_handler.generate(match, translation, prompt)
                for index_2, html_key_phrase in enumerate(html_key_phrases):
                    st.markdown(html_key_phrase, unsafe_allow_html=True)

    st.info(legend)

read_style()

st.title(":tropical_fish: Finding Mnemo")

input_word = st.text_input("Mandarin word:")

if input_word:
    pinyin = input_handler.input_to_pinyin(input_word)
    response = search_handler.search(pinyin)
    translation = input_handler.translate(input_word)

    summary = SummaryTable(input_word, pinyin, translation)
    st.markdown(summary, unsafe_allow_html=True)

    display_candidates(response, translation, pinyin)