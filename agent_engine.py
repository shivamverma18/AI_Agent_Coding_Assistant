import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 🔑 Set your OpenRouter API key
os.environ["OPENAI_API_KEY"] = "api-key-used"

# ✅ Initialize the model with OpenRouter base URL
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=os.environ["OPENAI_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)

# ---------------------------
# 🔍 Function: Explain Code
# ---------------------------
def explain_code(language: str, topic: str, level: str):
    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an AI coding tutor who explains code concepts clearly."),
            ("user", f"Explain the concept of {topic} in {language} for a {level} learner.")
        ])
        chain = prompt | llm
        response = chain.invoke({})
        return response.content
    except Exception as e:
        return f"Error generating explanation: {str(e)}"

# ---------------------------
# 💻 Function: Generate Code
# ---------------------------
def generate_code(language: str, topic: str, level: str):
    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert programmer."),
            ("user", f"Write a {level}-level {language} program for {topic}.")
        ])
        chain = prompt | llm
        response = chain.invoke({})
        return response.content
    except Exception as e:
        return f"Error generating code: {str(e)}"

# ---------------------------
# 🪲 Function: Debug Code
# ---------------------------
def debug_code(language: str, topic: str):
    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a coding assistant who debugs code."),
            ("user", f"Find and fix common bugs in {language} code related to {topic}.")
        ])
        chain = prompt | llm
        response = chain.invoke({})
        return response.content
    except Exception as e:
        return f"Error debugging code: {str(e)}"
