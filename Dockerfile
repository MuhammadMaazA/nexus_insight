# Use a slim Python image for efficiency and minimal size
# 'bookworm' refers to Debian 12, providing a stable base
FROM python:3.10-slim-bookworm

# Set the working directory inside the container
# All subsequent commands will operate relative to /app
WORKDIR /app

# Copy only the requirements file first to leverage Docker's build cache.
# If requirements.txt doesn't change, this step won't re-run.
COPY requirements.txt .

# Install Python dependencies. --no-cache-dir reduces image size.
# It's good practice to upgrade pip itself first.
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
# This copies the entire 'src' directory and the '.env.example'
# Your actual .env file will NOT be copied into the image for security
COPY src/ src/
COPY .env.example .env.example

# Set default environment variables for LangSmith and LLM API keys.
# These are placeholders and will be overridden at runtime by docker-compose.
ENV LANGCHAIN_TRACING_V2=true
ENV LANGCHAIN_PROJECT="Nexus Insight Agent Docker" 
ENV OPENAI_API_KEY="" 
ENV LANGCHAIN_API_KEY="" 

# Command to run your application when the container starts
# This specifies that your main script (src/main.py) should be executed
CMD ["python", "src/main.py"]
