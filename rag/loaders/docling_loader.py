from pathlib import Path

from docling.document_converter import DocumentConverter


def load_documents(directory: str):
    converter = DocumentConverter()
    documents = []

    for file in Path(directory).glob("*"):
        if file.suffix.lower() not in [".pdf", ".txt", ".docx", ""]:
            continue

        result = converter.convert(str(file))

        text = result.document.export_to_markdown()

        documents.append({
            "content": text,
            "metadata": {
                "source": file.name,
                "path": str(file)
            }
        })

    return documents
