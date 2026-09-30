from document.pdf_generator import generate_pdf


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

    output = generate_pdf(
        content,
        "generated/employment_agreement.pdf"
    )

    print(f"PDF document created: {output}")


if __name__ == "__main__":
    main()
