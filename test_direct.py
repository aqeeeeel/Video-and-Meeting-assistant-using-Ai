import os
import time
from dotenv import load_dotenv
from langchain_ollama import ChatOllama  # <-- Updated import

load_dotenv()

# Initialize Ollama with your local model
llm = ChatOllama(
    model="llama3.2",  # Make sure you ran 'ollama run llama3' at least once
    temperature=0.3
)

start_time = time.time()
response = llm.invoke("Say hello in one sentence.")
end_time = time.time()

print(f"Llama Response: {response.content}")
print(f"⏱️ Time taken: {end_time - start_time:.2f} seconds")