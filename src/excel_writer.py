from openpyxl import Workbook, load_workbook

from config import OUTPUT_DIR


def write_invoice(fact):
    output = OUTPUT_DIR / "Facture_results.xlsx"
    exist = output.exists()
    if exist:
        wb = load_workbook(output)
        ws = wb.active
        ws.append(
            [
                fact["fecha"],
                fact["formato"],
                fact["emisor"],
                fact["total"],
                fact["numero"],
            ]
        )
        wb.save(output)
    else:
        print('The Excel file is being created, go check "outputs"')
        wb = Workbook()
        ws = wb.active
        ws.append(["Fecha", "Format", "Emisor", "Total", "Numero"])
        ws.append(
            [
                fact["fecha"],
                fact["formato"],
                fact["emisor"],
                fact["total"],
                fact["numero"],
            ]
        )

        wb.save(output)
    return True
