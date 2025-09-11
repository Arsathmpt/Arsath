Age and Emotion Detection through Voice
This Streamlit application is designed to analyze a voice note (.mp3 or .wav) and predict the speaker's age and emotion based on a specific set of rules.

Core Features
Male Voice Processing: The model is designed to only process voices it identifies as male. If a female voice is uploaded, the application will display an error message and reject the input.

Conditional Analysis: The analysis performed depends on the predicted age of the speaker:

Below 60: The model only predicts the person's age.

Over 60: The model predicts the age, marks the person as a "Senior Citizen," and also predicts their emotion (e.g., Happy, Sad, Neutral).

Simulated ML Model: To focus on the application's logic, GUI, and rule-based system, the machine learning predictions (gender, age, emotion) are simulated. This demonstrates the complete functionality of the app without the need for a complex, pre-trained audio model.

Modern Dark UI: The application features a custom dark theme for an improved and more readable user experience.

How to Run the Project
Open a Terminal: Launch your command line tool (PowerShell, Command Prompt, etc.).

Activate Virtual Environment: Navigate to the main submission folder and activate the virtual environment:

# Navigate to the main folder
cd path/to/Nullclass Internship Submission

# Activate the environment
.\venv\Scripts\Activate.ps1

Navigate to Project Folder: Move into this project's directory:

cd "Voice Emotion Detection"

Install Requirements: Install the necessary Python libraries for audio processing:

pip install -r requirements.txt

Run the App: Start the Streamlit application:

streamlit run app.py

The application will open in your web browser, where you can upload an audio file for analysis.