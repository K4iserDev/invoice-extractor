import re

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

def extract_invoice_num(pdf):
    print(repr(pdf))
    fecha = re.search(r"Fecha de emisión:\s*(\d{2}/\d{2}/\d{4})", pdf)
    if fecha is None:
        print("no se ha encontrado nada")
    else:
        print(fecha.group(1))
    cliente = re.search(r"TOTAL:\s*(\d+,\d+)", pdf)
    if cliente is None:
        print("no se ha encontrado nada")
    else:
        print(cliente.group(1))
    emisor = re.search(r"Emisor\n(.+)", pdf)
    if emisor is None:
        print("no se ha encontrado nada")
    else:
        print(emisor.group(1))


if __name__ == "__main__":
    pdf_path = INPUT_DIR / "factura_es_01.pdf"
    text = extract_invoice(pdf_path)
    format_detector(text)
    extract_invoice_num(text)
