from datetime import datetime as Datetime
from io import BytesIO
from zipfile import ZipFile

from odio.v1_2 import create_spreadsheet, create_text, parse_document
from odio.v1_2.elements import (
    A,
    Cell,
    DateStyle,
    ELEMENT_MAP,
    H1,
    Manifest,
    ManifestFileEntry,
    P,
    Row,
    Span,
    Spreadsheet,
    Table,
)


def test_ELEMENT_MAP():
    for element_name, element_properties in ELEMENT_MAP.items():
        cls = element_properties["cls"]
        assert cls.tag_name == element_name


def test_create_text():
    text = create_text()
    doc = text.doc
    document_content = doc.document_content

    body_element = document_content.find_children_by_name("office:body")[0]
    body_element.find_children_by_name("office:text")[0]


def test_A_str():
    a = A("A link", href="https://example.com")

    expected = (
        '<text:a xlink:href="https://example.com" '
        'xlink:type="simple">A link</text:a>\n'
    )
    assert str(a) == expected


def test_DateStyle():
    date_style = DateStyle()
    assert date_style.name == "date"


def test_Row_get_values():
    v1 = 1
    v2 = 2
    v3 = "=A1+A2"
    row = Row(Cell(v1), Cell(v2), Cell(formula=v3))
    assert row.get_values() == [v1, v2, v3]


def test_Row_pack():
    row = Row(Cell(1), Cell(1))
    packed_row = row.pack()

    assert len(packed_row.children) == 1


def test_Cell():
    cell = Cell()
    assert cell.tag_name == "table:table-cell"


def test_Cell_date():
    dt = Datetime(2022, 6, 12)
    cell = Cell(value=dt)

    assert cell.value_type == "date"
    assert cell.attributes["office:date-value"] == "2022-06-12T00:00:00"
    assert cell.get_value() == dt
    assert cell.tag_name == "table:table-cell"


def test_Cell_string():
    value = "atom"
    cell = Cell(value=value)
    assert cell.get_value() == value


def test_Cell_formula():
    formula = "=B1 + C1"
    cell = Cell(formula=formula)
    assert cell.get_value() == formula


def test_H1():
    H1()


def test_ManifestFileEntry():
    full_path = "diary.txt"
    media_type = "text/plain"
    mfe = ManifestFileEntry(full_path=full_path, media_type=media_type)

    assert mfe.attributes["manifest:full-path"] == full_path
    assert mfe.full_path == full_path
    assert mfe.attributes["manifest:media-type"] == media_type
    assert mfe.media_type == media_type


def test_ManifestFileEntry_fill_False():
    ManifestFileEntry(fill=False)


def test_Manifest():
    media_type = "text/plain"
    m = Manifest(media_type=media_type)

    mfe = m.children[0]
    assert mfe.attributes["manifest:full-path"] == "/"
    assert mfe.attributes["manifest:media-type"] == media_type


def test_P():
    P()


def test_Row_append_cell():
    row = Row()
    row.append_cell(1)


def test_Span():
    Span()


def test_create_spreadsheet():
    spreadsheet = create_spreadsheet()
    doc = spreadsheet.doc
    document_content = doc.document_content

    body_element = document_content.find_children_by_name("office:body")[0]
    body_element.find_children_by_name("office:spreadsheet")[0]


def test_Spreadsheet_save():
    spreadsheet = create_spreadsheet()
    with BytesIO() as f:
        spreadsheet.save(f)


def test_Spreadsheet_append_table():
    spreadsheet = Spreadsheet()
    table_name = "a"
    table = spreadsheet.append_table(table_name)
    assert table.attributes["table:name"] == table_name


def test_Table_init():
    table_name = "a"
    table = Table(name=table_name)
    assert table.attributes["table:name"] == table_name
    assert table.name == table_name
    assert table.rows == []


def test_Table_append_row():
    table = Table()
    table.append_row([1])


def test_parse_document():
    sheet = create_spreadsheet()
    with BytesIO() as f:
        sheet.save(f)

        f.seek(0)
        with ZipFile(f) as z:
            parse_document(z)
