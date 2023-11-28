from fpdf import FPDF
import glob
from pathlib import Path
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")

filenames = glob.glob("TextStudent/*txt")

for file in filenames:
    pdf.add_page()
    filepath = Path(file).stem
    name = filepath.title()
    with open(file, "r") as file1:
        content = file1.read()

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=name,ln=1)
    pdf.set_font(family="Times", size=11, style="I")
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("Output.pdf")
