import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Gemini configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

# Validate API key
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add it to the .env file."
    )

# Validate model
if not GEMINI_MODEL:
    raise ValueError(
        "GEMINI_MODEL is missing. "
        "Please add it to the .env file."
    )