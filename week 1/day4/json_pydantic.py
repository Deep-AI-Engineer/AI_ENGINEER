import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API key kaha hain bhai")

client = Groq(api_key = api_key)

model = "openai/gpt-oss-20b"
role="user"

#structure 

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()

response_fromat={
    "type":"json_object"
}

system_prompt=f""" Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""

message_system={
    "role":"system",
    "content": system_prompt
}

text="Hello My name is deepanshu. Yesterday i broke up with my girlfriend deepanshi I have an iphone which is not working at all. My address is noida. My email is deep@gmail.com. My contact number is 910001"
prompt=f"""
This is a customer ticket. please extract the personal information from this. 
{text}
"""

message={
    "role":role,
    "content": prompt
}

message=[message_system,message]
response =client.chat.completions.create(model=model,messages=message,response_format=response_fromat)

answer = response.choices[0].message.content
print(answer)
