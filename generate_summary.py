from dotenv import load_dotenv

load_dotenv()  # load all the nevironment variables
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## getting the summary based on Prompt from Google Gemini Pro
def generate_summary(transcript_text, user_prompt):
    
    default_prompt = "As a YouTube Video summarizer, your task is to analyze the transcript text provided and condense the key points into a concise summary of no more than 250 words. Your summary should highlight the most important aspects of the video in bullet points."
    
    # validation
    if user_prompt!="":
        default_prompt += " Below is additional specific instructions to customize the summary further, if it contradicts, override above instructions."
        
    updated_prompt = default_prompt + "\n" + user_prompt + "\n" + "Please proceed to summarize the given text accordingly."
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(updated_prompt + transcript_text)
    return response.text
