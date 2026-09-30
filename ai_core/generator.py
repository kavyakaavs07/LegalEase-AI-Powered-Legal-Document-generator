from ai_core.gemini_generator import GeminiGenerator


class GeminiDocumentGenerator:
    """Generate legal documents using the configured AI provider."""

    def __init__(self):
        self.generator = GeminiGenerator()

    def generate(self, prompt: str) -> str:
        """Generate a legal document from a prompt."""
        return self.generator.generate(prompt)