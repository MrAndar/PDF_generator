from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Adding first page and header
    pdf.add_page()
    pdf.set_font(family="Arial", style="B", size=18)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(w=0, h=12, txt=f"{row["Topic"]}", align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    # Set footer
    pdf.ln(260)
    pdf.set_font(family="Arial", style="B", size=8)
    pdf.set_text_color(140, 140, 140)
    pdf.cell(w=0, h=12, txt=f"{row["Topic"]}", align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set footer
        pdf.ln(272)
        pdf.set_font(family="Arial", style="B", size=8)
        pdf.set_text_color(140, 140, 140)
        pdf.cell(w=0, h=12, txt=f"{row["Topic"]}", align="R", ln=1)


pdf.output("output.pdf")
