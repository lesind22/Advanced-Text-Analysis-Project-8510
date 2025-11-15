# PDF To text (for JET)

import os
from pathlib import Path
from pdfminer.high_level import extract_text

PDF_FOLDER = "JET PDFs"
TXT_FOLDER = "JET txt files"
os.makedirs(TXT_FOLDER, exist_ok=True)

pdf_files = list(Path(PDF_FOLDER).glob("*.pdf"))
print(f"Found {len(pdf_files)} PDFs.")

for pdf_file in pdf_files:
    print(f"Processing: {pdf_file}")
    text = extract_text(pdf_file)
    txt_path = Path(TXT_FOLDER) / (pdf_file.stem + ".txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Converted {pdf_file} to {txt_path}") 