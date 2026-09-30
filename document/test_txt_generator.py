from document.txt_generator import generate_txt


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

    output = generate_txt(
        content,
        "generated/employment_agreement.txt"
    )

    print(f"TXT document created: {output}")


if __name__ == "__main__":
    main()
