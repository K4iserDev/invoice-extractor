from config import INPUT_DIR
from extractor import extract_invoice
from parser import date, format_detector, number, total, transmitter


def process(path):
    text = extract_invoice(path)
    formato = format_detector(text)
    factura = {
        "numero": ...,
        "fecha": ...,
        "emisor": ...,
        "total": ...,
        "formato": ...,
    }
    factura["emisor"] = transmitter(text, formato)
    factura["fecha"] = date(text, formato)
    factura["total"] = total(text, formato)
    factura["formato"] = formato
    factura["numero"] = number(text)
    return factura


if __name__ == "__main__":
    pdf_path = INPUT_DIR / "factura_es_01.pdf"
    resultado = process(pdf_path)
    print(resultado)
