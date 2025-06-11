import os
# We no longer need load_dotenv() here because docker-compose handles
# injecting the environment variables directly into the container's environment.
# from dotenv import load_dotenv

from langchain_openai import ChatOpenAI # Adjust based on your chosen LLM provider
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- Optional: Print to verify env vars are loaded (remove after first run) ---
# These will now be loaded directly by Docker, not python-dotenv
print(f"Container's LANGCHAIN_API_KEY loaded: {'LANGCHAIN_API_KEY' in os.environ}")
print(f"Container's LANGCHAIN_PROJECT set to: {os.getenv('LANGCHAIN_PROJECT')}")
print(f"Container's LANGCHAIN_TRACING_V2 set to: {os.getenv('LANGCHAIN_TRACING_V2')}")
print(f"Container's OPENAI_API_KEY loaded: {'OPENAI_API_KEY' in os.environ}")
# --- End Optional Prints ---

# Initialize your LLM
# The API key is now directly in the container's environment from docker-compose
llm = ChatOpenAI(model="gpt-4o", temperature=0.7) # Or your chosen model

# Define a simple prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant for Nexus Insight."),
    ("user", "Tell me a very short, inspiring quote about insight and discovery.")
])

# Create a simple chain: Prompt -> LLM -> Output Parser
chain = prompt | llm | StrOutputParser()

print("\nRunning a simple LangChain test for Nexus Insight (Dockerized)...")
try:
    response = chain.invoke({}) # Invoke the chain
    print("\nLLM Response:")
    print(response)
    print("\n--- Check LangSmith for the trace! ---")
except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Please double-check your API keys in your host's .env file and your internet connection.")
    # Print environment variables if an error occurs to help debug
    print(f"DEBUG: OPENAI_API_KEY status: {'OPENAI_API_KEY' in os.environ}")
    print(f"DEBUG: LANGCHAIN_API_KEY status: {'LANGCHAIN_API_KEY' in os.environ}")
