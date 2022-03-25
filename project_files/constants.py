"""
There are no constants in Python, but of course, it cannot stop us
to use some of the value as constant.
This file will store some values, which will never change during the runtime
"""

from pathlib import Path
from reportlab.lib.units import mm


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
TEMPLATES_DIR = BASE_DIR / "templates"
IMAGES_DIR = BASE_DIR / "images"
ID_CARDS_DIR = BASE_DIR / "id_cards"

DATA_FILE = DATA_DIR / "student_data.xlsx"
TEMPLATE_FILE = TEMPLATES_DIR / "student_card_front.pdf"
TEMPLATE_FILE = TEMPLATES_DIR / "student_card_back.pdf"

PAGE_WIDTH = 54 * mm
PAGE_HEIGHT = 85 * mm
PAGE_SIZE = PAGE_WIDTH, PAGE_HEIGHT

FONT = "Calibri"
FONT_SIZE = 6
FONT_COLOR = (0, 0, 0)
#print(TEMPLATES_DIR)