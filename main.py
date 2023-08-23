import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")

print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit='mm',format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, invoice_dt  = filename.split("-")

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50, h=8, txt=f"invoice_nr{invoice_nr}", ln=1) # ln is to create break line

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {invoice_dt}")

    pdf.output(f"PDFs/{filename}.pdf")
