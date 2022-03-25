"""
It will be responsible for everithing related to PDF.
"""
from io import BytesIO
from .data_functions import get_data

from PyPDF2 import PdfFileReader, PdfFileWriter

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from .constants import PAGE_SIZE
from .constants import FONT, FONT_SIZE, FONT_COLOR
from .constants import TEMPLATE_FILE, ID_CARDS_DIR


def create_info_canvas(student):
    packet = BytesIO()
    can = canvas.Canvas(packet, PAGE_SIZE)

    can.setFont(FONT, FONT_SIZE)
    can.setFillColor(FONT_COLOR)

    id = student['ID']
    name = student['NOMBRES']
    last_name = student['APELLIDOS']
    doc_number = student['ESTUDIANTE_DOCUMENTO']
    doc_type = student['TIPO_DOCUMENTO']
    rh = student['RH']
    profile = student['PERFIL']

    can.drawString(10, 10, id)
    can.drawString(10, 10, name)
    can.drawString(10, 10, last_name)
    can.drawString(10, 10, doc_number)
    can.drawString(10, 10, doc_type)
    can.drawString(10, 10, rh)
    can.drawString(10, 10, profile)

    can.save()
    packet.seek(0)

    return PdfFileReader(packet)


def get_template(template=TEMPLATE_FILE):
    return PdfFileReader(str(template))


def create_pdf_file(student, canvas_info, template):
    page = template.getPage(0)
    page.mergePage(canvas_info.getPage(0))

    output = PdfFileWriter()
    output.addPage(page)

    page = template.getPage(1)
    output.addPage(page)

    file_name = ID_CARDS_DIR / f"{student['ID']}.pdf"

    with open(file_name, "wb") as file:
        output.write(file)


def create_an_id_card(student):
    # Create a canvas with student info.
    canvas_info = create_info_canvas(student)

    # Get PDF template.
    template = get_template()

    # Merge canvas with template.
    create_pdf_file(student, canvas_info, template)


def create_student_cards():
    # Read data from an Excel file.
    data = get_data()
    print(data)
    # Iterate over each student in the file.
    for _, student in data.head(1).iterrows():
        create_an_id_card(student)
    # Create an id card for each student.


pdfmetrics.registerFont(TTFont("Calibri", "Calibri.ttf"))
