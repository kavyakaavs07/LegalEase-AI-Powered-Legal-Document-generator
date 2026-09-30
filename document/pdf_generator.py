from pathlib import Path

from fpdf import FPDF


def generate_pdf(content: str, output_path: str) -> str:
    """
    Save document content as a PDF file.

    Args:
        content: The document text.
        output_path: Where the PDF file should be saved.

    Returns:
        The path to the generated file.
    """

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    pdf = FPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    pdf.add_page()

    pdf.set_font(
        "Helvetica",
        size=11
    )

    for line in content.splitlines():
        if not line.strip():
            pdf.ln(6)
            continue

        pdf.cell(
            0,
            7,
            text=line,
            new_x="LMARGIN",
            new_y="NEXT"
        )

    pdf.output(str(path))

    return str(path)