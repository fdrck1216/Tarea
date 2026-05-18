import os
from fpdf import FPDF

def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Datos del Sistema Web Personal", ln=True, align='C')
    pdf.ln(10)
    
    # Data
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Apellidos: Sornoza Loaiza", ln=True)
    pdf.cell(200, 10, txt="Nombres: Roger Federick", ln=True)
    pdf.cell(200, 10, txt="Link del sistema web (PythonAnywhere): https://rogersornoza.pythonanywhere.com", ln=True)
    pdf.cell(200, 10, txt="Link del Drive de la UTM (archivos fuente): [Reemplazar con Link del Drive]", ln=True)
    
    output_path = os.path.join(os.getcwd(), "Datos_Despliegue.pdf")
    pdf.output(output_path)
    print(f"PDF generado exitosamente en: {output_path}")

if __name__ == '__main__':
    create_pdf()
