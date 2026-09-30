import sys
import os

# Add LegalEase project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from ai_core.generator import GeminiDocumentGenerator


generator = GeminiDocumentGenerator()

prompt = """
Create a simple employment agreement outline.

Include these sections:

1. Employer
2. Employee
3. Position
4. Start Date
5. Compensation
6. Responsibilities
7. Confidentiality
8. Termination

Keep it concise.
Do not provide legal advice.
"""

result = generator.generate(prompt)

print("\nGenerated Employment Agreement Outline:\n")
print(result)