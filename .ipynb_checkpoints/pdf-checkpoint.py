import PyPDF2
from PIL import Image
import os

def extract_first_page(pdf_path, output_folder):
  # Abre el archivo PDF
  with open(pdf_path, 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    page = reader.pages[0]

    # Extrae la imagen de la primera página
    x_object = page['/Resources']['/XObject'].getObject()
    for name, obj in x_object.items():
      if obj['/Subtype'] == '/Image':
        data = obj._data
        img = Image.frombytes("RGB", (obj['/Width'], obj['/Height']), data)
        img.save(os.path.join(output_folder, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page1.png"))

# Directorio con los PDFs
input_folder = "D:\STRU\Library\05_CODE\AISC\AISC_Design Guides"
output_folder = "D:\STRU\Library\05_CODE\AISC\PNG"

# Recorre todos los archivos PDF en el directorio
for filename in os.listdir(input_folder):
  if filename.endswith(".pdf"):
    pdf_path = os.path.join(input_folder, filename)
    extract_first_page(pdf_path, output_folder)