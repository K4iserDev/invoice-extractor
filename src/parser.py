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


def date(pdf, formato):
    if formato == "es":
        fecha = re.search(r"Fecha de emisión:\s*(\d{2}/\d{2}/\d{4})", pdf)
    elif formato == "eng":
        fecha = re.search(r"Issue date:\s*(\d{4}-\d{2}-\d{2})", pdf)
    else:
        fecha = None

    if fecha is None:
        return None
    else:
        return fecha.group(1)


def transmitter(pdf, formato):
    if formato == "es":
        emisor = re.search(r"Emisor Cliente\n(.+?S\.[LA]\.)", pdf)
    elif formato == "eng":
        emisor = re.search(r"From Bill To\n(.+?(?:Ltd\.|Inc\.|LLC))", pdf)
    else:
        emisor = None

    if emisor is None:
        return None
    else:
        return emisor.group(1)


def total(pdf, formato):
    if formato == "es":
        total = re.search(r"TOTAL:\s*([\d.]+,\d+)", pdf)
    elif formato == "eng":
        total = re.search(r"TOTAL DUE:\s*\$?([\d,]+\.\d{2})", pdf)
    else:
        total = None

    if total is None:
        return None
    else:
        return total.group(1)


def number(pdf):
    numero = re.search(r"(?:Nº Factura|Invoice #):\s*([\w-]+)", pdf)
    if numero is None:
        return None
    else:
        return numero.group(1)


if __name__ == "__main__":
    pdf_path = INPUT_DIR / "factura_es_01.pdf"
    text = extract_invoice(pdf_path)
    formato = format_detector(text)
    """"
    print(formato)
    print(transmitter(text, formato))
    print(date(text, formato))
    print(total(text, formato))

    """
