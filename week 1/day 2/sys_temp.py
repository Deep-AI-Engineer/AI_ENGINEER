import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
if not api_key:
 raise ValueError("API KEY KAHA HAI BHAI")

client = Groq(api_key = api_key)

model = "openai/gpt-oss-20b"
role ="user"
content = "suggest a name for my clothing company"

message_system={
    "role":"system", 
    "content":"you are a brand manager who suggests name for my company name should be in one word  suggest only one name "
}
message = {
          "role": "user",
          "content":content
         }

message = [message_system,message]
response = client.chat.completions.create(model=model,messages = message,temperature = 0)

answer = response.choices[0].message.content
print(answer)