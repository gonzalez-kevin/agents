import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from config import *

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <prompt>")
        sys.exit(1)
        
    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv[2:]
    messages = [types.Content(role = "User", parts = [types.Part(text = user_prompt)]),]

    content = client.models.generate_content(model = "gemini-2.0-flash-001", contents = messages, config = types.GenerateContentConfig(system_instruction = system_prompt))

    prompt = content.usage_metadata.prompt_token_count
    candidate = content.usage_metadata.candidates_token_count
    
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt}")
        print(f"Response tokens: {candidate}")
        print(content.text)
    else:
        print(content.text)


if __name__ == "__main__":
    main()
