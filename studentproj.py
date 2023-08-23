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
        df = file1.readlines()
        data = str(df)

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=name,ln=1)
    pdf.set_font(family="Times", size=11, style="I")
    pdf.cell(w=50, h=8, txt=data,ln=1)

pdf.output("Output.pdf")

