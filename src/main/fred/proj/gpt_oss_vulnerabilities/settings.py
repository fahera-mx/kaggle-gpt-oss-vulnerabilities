import os

# Settings for OpenAI API
FRD_OPENAI_API_KEY = os.environ.get("FRD_OPENAI_API_KEY")
FRD_OPENAI_BASE_URL = os.environ.get(
    "FRD_OPENAI_BASE_URL",
    default="https://api.openai.com/v1"
)
FRD_OPENAI_DEFAULT_MODEL = os.environ.get(
    "FRD_OPENAI_DEFAULT_MODEL",
    default="openai/gpt-oss-20b"
)
if "openrouter" in FRD_OPENAI_BASE_URL and not FRD_OPENAI_DEFAULT_MODEL.endswith(":free"):
    print("Warning: Using OpenRouter with a non-free model.")
