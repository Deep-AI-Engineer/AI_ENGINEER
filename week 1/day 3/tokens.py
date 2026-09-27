import os 
from pathlib import Path 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API_KEY KAHA HAIN BHAI")

client = Groq(api_key = api_key)
model="openai/gpt-oss-20b"
role="user"

prompt1 = "hi!"
prompt2 = "Explain time travel in detail but under 100 words"
prompt3 = "Write a 1000 word essay on machine learning"

prompts = [prompt1,prompt2,prompt3]
for prompt in prompts:
    message = {
        "role":role,
        "content":prompt
    }
    messages=[message]
    response =client.chat.completions.create(model=model,messages=messages,max_tokens=5000)
    usage=response.usage
    print(f"prompt:{prompt} --> your tokens:{usage.prompt_tokens}completion_tokens:{usage.completion_tokens}total tokens:{usage.total_tokens}finsh Reason:{response.choices[0].finish_reason}")
    