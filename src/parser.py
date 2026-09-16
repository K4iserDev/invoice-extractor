from config import INPUT_DIR
from extractor import extract_invoice


def format_detector(detect):
    print("Detecting format...")
    count_eng = 0
    count_esp = 0
    lower = detect.lower()
    eng = ["sales tax", "vat", "tax id", "ein", "$"]
    esp = ["iva", "nif", "cif", "€"]
    for text_eng in eng:
        English = text_eng in lower
        if English:
            count_eng += 1
    for text_esp in esp:
        Spanish = text_esp in lower
        if Spanish:
            count_esp += 1
    if count_esp > count_eng:
        print("The text it´s in Spanish")
        return "es"
    elif count_eng > count_esp:
        print("The text it´s in English")
        return "eng"
    else:
        print("We have not been able to recognize the format.")
        return None


if __name__ == "__main__":
    pdf_path = INPUT_DIR / "invoice_us_01.pdf"
    text = extract_invoice(pdf_path)
    format_detector(text)
