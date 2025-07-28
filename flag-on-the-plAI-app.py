import streamlit as st
from gpt4all import GPT4All
import os
import urllib.request

# Model setup
MODEL_NAME = "ggml-gpt4all-j-v1.3-groovy.bin"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)

# URL to download the model
MODEL_URL = "https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin"

# Download model if not present
if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_DIR, exist_ok=True)
    st.info("Downloading GPT4All model (~4GB). This may take some time...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    st.success("Model downloaded successfully!")

# Load the model
try:
    model = GPT4All(model_name=MODEL_NAME, model_path=MODEL_DIR)
    model.open()
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

# Streamlit app UI
st.set_page_config(page_title="flag on the plAI")
st.title("🏁 flag on the plAI")
st.caption("By Ayaan Patel")
st.markdown("Enter a game incident and get the official ruling based on the sport's rulebook.")

sports = [
    "Cricket",
    "Basketball",
    "American Football",
    "Soccer",
    "Baseball",
    "Ice Hockey"
]

rulebook_snippets = {
    "Cricket": "Use the MCC Laws of Cricket for rulings.",
    "Basketball": "Use the NBA rules for rulings.",
    "American Football": "Use the NFL rules for rulings.",
    "Soccer": "Use the IFAB rules for rulings.",
    "Baseball": "Use the MLB rules for rulings.",
    "Ice Hockey": "Use the NHL rules for rulings."
}

sport = st.selectbox("Select the Sport", sports)
incident = st.text_area("Describe the Incident", placeholder="E.g., Player collided with another player while attempting to catch the ball.")

if st.button("Get Ruling"):
    if not incident.strip():
        st.warning("Please describe the incident.")
    else:
        context = rulebook_snippets.get(sport, "")
        prompt = f"""
You are an expert referee for {sport}. Refer to the key rules below:

{context}

Based on these rules, determine the correct ruling for the following incident:

Incident: "{incident}"

Provide:
1. A clear ruling
2. The reason behind the ruling
3. Which type of rule it relates to
"""

        with st.spinner("Analyzing the incident and consulting local rulebook snippets..."):
            try:
                response = model.prompt(prompt, max_tokens=300)
                st.success("Ruling Generated")
                st.markdown("### 🔖 Official Ruling")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred while generating the ruling: {str(e)}")

st.markdown("---")
st.caption("Local AI Referee — no internet required once installed.")
