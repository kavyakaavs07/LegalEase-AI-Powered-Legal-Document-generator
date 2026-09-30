from pathlib import Path


def generate_txt(content: str, output_path: str) -> str:
    """
    Save document content as a plain text file.

    Args:
        content: The document text.
        output_path: Where the TXT file should be saved.

    Returns:
        The path to the generated file.
    """

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        content,
        encoding="utf-8"
    )

    return str(path)