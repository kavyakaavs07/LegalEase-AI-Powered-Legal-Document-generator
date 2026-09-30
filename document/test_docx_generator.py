from document.docx_generator import generate_docx


def main():
    content = """EMPLOYMENT AGREEMENT

Employer: Example Company
Employee: John Doe

Position: Software Developer

Compensation: $60,000 per year

Confidentiality:
The employee agrees to protect confidential company information.

Termination:
The employment relationship may be terminated according to applicable law.
"""

    output = generate_docx(
        content,
        "generated/employment_agreement.docx"
    )

    print(f"DOCX document created: {output}")


if __name__ == "__main__":
    main()
