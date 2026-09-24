import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API_KEY_ERROR")

client = Groq(api_key = api_key)

model = "openai/gpt-oss-20b"
role = "user"
content = "who is virat kohli?"

message = {"role":role, "content":content}
message = [message]
 
response = client.chat.completions.create(
    model=model,
    messages=message
)
answer=response.choices[0].message.content
    
print(answer)