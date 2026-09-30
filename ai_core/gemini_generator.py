from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiGenerator:
    """Gemini-powered text generation for LegalEase."""

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:
        """Generate text using the configured Gemini model."""

        interaction = self.client.interactions.create(
            model=GEMINI_MODEL,
            input=prompt
        )

        return interaction.output_text