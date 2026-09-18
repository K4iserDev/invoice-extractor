
A Python tool that extracts structured data from PDF invoices — Spanish and international formats — and exports the results to Excel. Built as a portfolio project to demonstrate practical, rule-based data extraction combined with clean project structure and testing against a varied dataset.

What it does
Reads the text content of a PDF invoice (pdfplumber).
Detects the format (Spanish vs. international) by scoring domain-specific markers found in the text (IVA, NIF, € vs. VAT, Tax ID, $, etc.) — not by language detection, since the goal is identifying the correct fiscal/formatting ruleset to apply, not the language.
Extracts key fields using regular expressions tailored to each format:
Invoice number
Issue date
Issuer / vendor name
Total amount
Writes each processed invoice as a new row in an Excel file (openpyxl), creating the file with headers on first run and appending rows on subsequent runs.

The pipeline processes every PDF found in data/input/ in a single run.

Project structure
invoice-extractor/
├── data/
│   ├── input/          # drop PDF invoices here
│   └── output/         # generated Excel file (git-ignored)
├── src/
│   ├── config.py        # base paths (project-root-relative, OS independent)
│   ├── extractor.py      # PDF → plain text
│   ├── parser.py         # format detection + field extraction (regex)
│   ├── excel_writer.py   # structured data → Excel row
│   └── main.py           # orchestrates the full pipeline
├── .env.example          # template for future OpenAI API key usage
├── requirements.txt
└── README.md
Setup
bash
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell

# source .venv/bin/activate       # macOS/Linux

pip install -r requirements.txt
Usage
Place one or more invoice PDFs in data/input/.
Run the pipeline from the project root:
bash
python src/main.py
Check data/output/Facture_results.xlsx for the extracted results.
Known limitations
Issuer name extraction relies on the invoice using a recognizable legal suffix (S.L., S.A., Ltd., Inc., LLC). Companies with other suffixes (e.g. S.L.U., GmbH) won't be captured correctly.
Field extraction is regex-based and deterministic — reliable and auditable for the formats it was built against, but it does not generalize to invoice layouts it hasn't seen. This is a deliberate trade-off for financial data: a missing field (None) is safer than a silently wrong one from a probabilistic model.
Tested against a synthetic dataset of ~60 invoices across two formats and ~25 countries; not validated against real-world scanned invoices.
Roadmap
Validation step: flag invoices with missing fields for manual review instead of silently writing incomplete rows.
LLM-based line-item categorization: classify invoice concepts (materials, services, etc.) using an LLM — a task suited to interpretation rather than exact extraction, where the risk profile of an LLM is acceptable.
LLM as a fallback, not a default: when regex extraction fails, attempt extraction via LLM as a last resort, clearly flagged as lower-confidence.
Coordinate-based text extraction: resolve multi-column PDF layouts (issuer/client side-by-side) using word positions instead of the current legal-suffix heuristic.
