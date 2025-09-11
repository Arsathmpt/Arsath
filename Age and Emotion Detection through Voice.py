import streamlit as st
import numpy as np
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Voice Analysis",
    page_icon="🎙️",
    layout="wide"
)

# --- Custom Dark Theme CSS ---
st.markdown("""
<style>
    .stApp { background-color: #1E1E1E; color: #FFFFFF; }
    h1 { color: #00A9B7; }
    .stAlert, .st-emotion-cache-1629p8f { background-color: #2D2D2D; border-radius: 10px; padding: 15px; }
    .st-emotion-cache-79elbk { background-color: #2D2D2D; border-radius: 10px; }
    .stButton>button { background-color: #00A9B7; color: white; border-radius: 10px; border: none; padding: 10px 24px; }
    p, .stMarkdown { color: #E0E0E0; }
</style>
""", unsafe_allow_html=True)


def simulate_voice_analysis(audio_bytes):
    """
    Simulates the voice analysis process to demonstrate the application logic
    without requiring a trained audio model.
    """
    # Simulate gender detection
    genders = ["Male", "Female"]
    # We'll make it more likely to detect "Male" to fit the project requirements
    detected_gender = np.random.choice(genders, p=[0.8, 0.2])

    if detected_gender == "Female":
        return {"gender": "Female", "error": "Upload male voice."}

    # Simulate age detection if gender is Male
    ages = [25, 45, 65]
    detected_age = np.random.choice(ages)

    result = {"gender": "Male", "age": detected_age}

    # Simulate emotion detection only if the person is a senior citizen
    if detected_age > 60:
        emotions = ["Happy", "Sad", "Neutral", "Angry"]
        detected_emotion = np.random.choice(emotions)
        result["emotion"] = detected_emotion
        result["senior_status"] = "Senior Citizen"

    return result


# --- Main Application ---
st.title("Age and Emotion Detection from Voice 🎙️")
st.write(
    "This app simulates voice analysis based on the project rules. It will only process voices it identifies as 'Male'.")

uploaded_file = st.file_uploader("Upload a voice note (.mp3, .wav)...", type=["mp3", "wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/wav')

    if st.button("Analyze Voice"):
        with st.spinner("Analyzing voice..."):
            time.sleep(2)  # Simulate processing time
            analysis_result = simulate_voice_analysis(uploaded_file.getvalue())

            if "error" in analysis_result:
                st.error(analysis_result["error"])
            else:
                st.success("Analysis Complete!")
                st.subheader("Analysis Results")
                st.write(f"**Detected Gender:** {analysis_result['gender']}")
                st.write(f"**Predicted Age:** {analysis_result['age']}")

                if "senior_status" in analysis_result:
                    st.write(f"**Status:** {analysis_result['senior_status']}")
                    st.write(f"**Predicted Emotion:** {analysis_result['emotion']}")

