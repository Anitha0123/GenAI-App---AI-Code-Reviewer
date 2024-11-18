import streamlit as st
import google.generativeai as genai

# Configure the Generative AI API with the provided API key
genai.configure(api_key="AIzaSyByskqL-TltPyk0RAQ3j04sIJiAecmlBo8")

# Initialize the generative model
llm = genai.GenerativeModel("models/gemini-1.5-flash")
        
# Start a new chat session with the model
chat = llm.start_chat(history=[])

# Set the title of the Streamlit app
st.title(":thought_balloon: An AI Code Reviewer")

# Create a text area input for users to enter their Python code
user_prompt = st.text_area("Enter your Python code here....", height=100)

# Define a button to trigger the code review process
st.button("Generate")

# Check if the user has entered any code
if user_prompt:
        # Send a request to review the entered Python code
        response = chat.send_message(f"{user_prompt}")
        
        # Display the AI-generated code review results
        st.subheader("Code Review")
        st.write("Bug Report:")
        st.write(response.text)  # Output the response from the AI
        