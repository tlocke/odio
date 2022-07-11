from io import BytesIO

from odio import create_spreadsheet, parse_document


def test_parse_document():
    sheet = create_spreadsheet()
    with BytesIO() as f:
        sheet.save(f)
        f.seek(0)
        parse_document(f)
