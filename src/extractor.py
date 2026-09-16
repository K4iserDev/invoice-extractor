import pdfplumber

from config import INPUT_DIR

pdf_path = INPUT_DIR / "invoice_us_01.pdf"


def extract_invoice(path):
    pages = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:  # In case we don´t know how many pages it has
            pages_text = page.extract_text()
            if pages_text:
                pages.append(pages_text)
            else:
                print("Please check your PDF, something is wrong")

    result = "\n".join(pages)
    return result


if __name__ == "__main__":
    text = extract_invoice(pdf_path)
    print(text)
