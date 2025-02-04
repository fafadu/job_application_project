# THIS IS save_cover_letter.py
import os
from docx import Document
import pdfkit 
from fpdf import FPDF

# # Set the path to wkhtmltopdf
# PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")  
# 確保 `outputs/generated_cover_letters/` 目錄存在

OUTPUT_DIR = "outputs/generated_cover_letters"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_cover_letter(role, company, content):
    """
    Generate Cover Letter and save as Word (.docx) and PDF (.pdf)

    """
    filename = f"CL_Fafa_Jinghwa_{role}_{company}".replace(" ", "_")  # # Remove spaces in filename
    word_file = os.path.join(OUTPUT_DIR, filename + ".docx")
    pdf_file = os.path.join(OUTPUT_DIR, filename + ".pdf")

    # Create Word document
    doc = Document()
    doc.add_paragraph(content)
    doc.save(word_file)

    # Create  PDF document
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", "", 9)

  
    for line in content.split("\n"):
        pdf.multi_cell(0, 8,line, align="L")  # Multi-line support
        #pdf.multi_cell(w, h, txt, border=0, align='', fill=False)
        pdf.ln(0)  # Add small space between lines

    pdf.output(pdf_file)

    print(f"✅ Cover Letter saved as:\n- {word_file}\n- {pdf_file}")
    

