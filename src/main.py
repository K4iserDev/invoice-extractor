from config import INPUT_DIR
from excel_writer import write_invoice
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
    write_invoice(factura)
    return factura


if __name__ == "__main__":
    for pdf_path in INPUT_DIR.glob("*.pdf"):
        resultado = process(pdf_path)
        print(resultado)
