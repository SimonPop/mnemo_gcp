import streamlit as st
from input_handler import InputHandler
from search_handler import SearchHandler

input_handler = InputHandler()
search_handler = SearchHandler()

def read_style():
    with open("style.html", 'r') as f:
        title_alignment = f.read()
    st.markdown(title_alignment, unsafe_allow_html=True)

def display_candidates(response, translation, pinyin):
    legend = ':tropical_fish: - Definitely Mnemo / :fish: - Not exactly Mnemo / :blowfish: - Barely Mnemo'
    matches, scores = search_handler.unpack(response)
    emojis = [SearchHandler.score2emoji(x) for x in scores]
    for index, (match, emoji) in enumerate(zip(matches, emojis)):
        st.write(f"{emoji} - {match}")
    st.info(legend)

read_style()

st.title(":tropical_fish: Finding Mnemo")

input_word = st.text_input("Mandarin word:")

if input_word:
    pinyin = input_handler.input_to_pinyin(input_word)
    response = search_handler.search(pinyin)
    translation = input_handler.translate(input_word)

    st.write(f"pinyin: {pinyin}")
    st.write(f"translation: {translation}")
    display_candidates(response, translation, pinyin)