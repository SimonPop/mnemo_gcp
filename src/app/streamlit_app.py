import streamlit as st
from input_handler import InputHandler
from search_handler import SearchHandler
from summary_table import SummaryTable
from key_phrase_handler import KeyPhraseHandler
from style import STYLE

@st.cache_resource(show_spinner="Loading Models...")
def load_handlers():
    input_handler = InputHandler()
    search_handler = SearchHandler()
    key_phrase_handler = KeyPhraseHandler()
    return (
        input_handler,
        search_handler,
        key_phrase_handler
    )
    
def read_style():
    st.markdown(STYLE, unsafe_allow_html=True)

def display_candidates(response, translation, pinyin):
    legend = ':tropical_fish: - Definitely Mnemo / :fish: - Not exactly Mnemo / :blowfish: - Barely Mnemo'
    matches, scores = search_handler.unpack(response)
    emojis = [SearchHandler.score2emoji(x) for x in scores]

    for index, (match, emoji) in enumerate(zip(matches, emojis)):
        key = f"generator_{index}"

        with st.expander(f"{emoji} - {match}"):
            prompt = st.text_input("Key-phrase prompt: ", value="It is said that ", key=key + "_text")            
            submit = st.button(":sparkles: Generate key-phrase!", key=key + "_button")     
            if submit:
                html_key_phrases = key_phrase_handler.generate(match, translation, prompt)
                for index_2, html_key_phrase in enumerate(html_key_phrases):
                    st.markdown(html_key_phrase, unsafe_allow_html=True)

    st.info(legend)

read_style()

input_handler, search_handler, key_phrase_handler = load_handlers()

st.title(":tropical_fish: Finding Mnemo")

placeholder = st.empty()

input_word = placeholder.text_input("Mandarin word:")
click_random = st.button(label="Random word")

if click_random:
    input_word = placeholder.text_input("Mandarin word:", value=input_handler.random_value(), key=1)

if input_word:
    pinyin = input_handler.input_to_pinyin(input_word)
    response = search_handler.search(pinyin)
    translation = input_handler.translate(input_word)

    summary = SummaryTable(input_word, pinyin, translation)
    st.markdown(summary, unsafe_allow_html=True)

    display_candidates(response, translation, pinyin)