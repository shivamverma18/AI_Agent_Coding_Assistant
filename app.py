import streamlit as st
import requests

st.title("AI Coding Assistant")

language = st.selectbox(
    "Select Language",
    ["Python", "JavaScript", "Java", "C++", "C", "Ruby", "Go"] 
)

topic = st.text_input("Enter the topic")

level = st.selectbox(
    "Select Level",
    ["Beginner", "Intermediate", "Advanced"]
)

API_URL = "http://127.0.0.1:8000"

def fetch_response(endpoint, payload):
    try:
        
        response = requests.post(f"{API_URL}/{endpoint}", json=payload)
        response_data = response.json()
        if "response" in response_data:
            return response_data["response"]
        else:
            st.error("Unexpected API Response Format!")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"API Request Failed: {e}")
        return None
    
if st.button("Explain"):
    explanation = fetch_response("explain", {"language": language, "topic": topic, "level": level})
    if explanation:
        st.write("## Explanation")
        st.write(explanation)
        
if st.button("Debug Code"):
    response = fetch_response("debug", {"language": language, "topic": topic, "level": level})
    if response:
        st.write("## Debugging:")
        st.write(response)
        
if st.button("Generate Code"):
    generate_code = fetch_response("generate", {"language": language, "topic": topic, "level": level})
    if generate_code:
        st.write("## Code Example:")
        st.code(generate_code, language=language.lower())
        
    