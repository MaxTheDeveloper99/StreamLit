import streamlit as st
from deep_translator import GoogleTranslator

# Page title
st.title("Language Translator")

st.write("Enter English text and translate it into another language.")


# Text input
text = st.text_area(
    "Enter your English text:",
    placeholder="Type something in English..."
)


# Language selection
language = st.selectbox(
    "Translate to:",
    [
        "French",
        "Spanish",
        "German",
        "Italian",
        "Portuguese",
        "Dutch",
        "Arabic",
        "Chinese",
        "Japanese",
        "Korean"
    ]
)


# Language codes
language_codes = {
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Arabic": "ar",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko"
}


# Translate button
if st.button("Translate"):

    # Check if text was entered
    if text.strip() == "":
        st.warning("Please enter some text first.")

    else:
        # Get language code
        target_language = language_codes[language]

        try:
            # Translate the text
            translated_text = GoogleTranslator(
                source="en",
                target=target_language
            ).translate(text)

            # Display translation
            st.subheader("Translation")

            st.write(translated_text)

        except Exception as e:
            st.error(f"Something went wrong: {e}")