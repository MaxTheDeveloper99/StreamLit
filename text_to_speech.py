import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

# Page title
st.title("Translator & Text to Speech")

st.write(
    "Enter English text, choose a language, and the app will "
    "translate the text and convert the translation to speech."
)

# Text input
text = st.text_area(
    "Enter your English text:",
    placeholder="Type something in English..."
)

# Language selection
language = st.selectbox(
    "Choose a language:",
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

# Convert button
if st.button("Translate & Speak"):

    # Check if the user entered text
    if text.strip() == "":
        st.warning("Please enter some English text first.")

    else:
        # Get the selected language code
        target_language = language_codes[language]

        try:
            # Translate the English text
            translated_text = GoogleTranslator(
                source="en",
                target=target_language
            ).translate(text)

            # Display the translation
            st.subheader("Translation")

            st.write(translated_text)

            # Convert translated text to speech
            speech = gTTS(
                text=translated_text,
                lang=target_language
            )

            # Save the speech as an MP3 file
            speech.save("translated_speech.mp3")

            # Success message
            st.success("Translation and speech generated successfully!")

            # Play the audio
            st.subheader("🔊 Speech")

            st.audio("translated_speech.mp3")

        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )