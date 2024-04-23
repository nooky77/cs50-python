from fpdf import FPDF

def main():
    name = input("Name: ").strip()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 32)
    pdf.cell(0, 30, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.image("./shirtificate.png", w=pdf.epw)
    pdf.set_font('helvetica', 'B', 25)
    pdf.set_text_color(255,255,255)
    pdf.multi_cell(0, -250, txt=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()