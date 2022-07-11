from odio.v1_2.elements import (
    Cell,
    Document,
    ELEMENT_MAP,
    H,
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    P,
    Span,
    Spreadsheet,
    Text,
)
from odio.v1_2.xml import (
    GeneralElement,
    parse_xml_str,
)


def create_spreadsheet(date_style=None):
    doc = Document()
    spreadsheet = Spreadsheet(doc=doc)
    document_content = doc.document_content
    document_content.children.append(GeneralElement("office:scripts"))
    document_content.children.append(GeneralElement("office:automatic-styles"))
    document_styles = doc.document_styles
    styles = GeneralElement("office:styles")
    document_styles.children.append(styles)
    if date_style is not None:
        styles.children.append(date_style)
        styles.children.append(
            GeneralElement(
                "style:style",
                attributes={
                    "style:name": "cell_date",
                    "style:family": "table-cell",
                    "style:data-style-name": date_style.name,
                },
            ),
        )
    document_content.children.append(GeneralElement("office:body", spreadsheet))
    return spreadsheet


def create_text(date_style=None):
    doc = Document()
    text = Text(doc=doc)
    document_content = doc.document_content
    document_content.children.append(GeneralElement("office:scripts"))
    document_content.children.append(GeneralElement("office:automatic-styles"))
    document_styles = doc.document_styles
    styles = GeneralElement("office:styles")
    document_styles.children.append(styles)
    if date_style is not None:
        styles.children.append(date_style)
        styles.children.append(
            GeneralElement(
                "style:style",
                attributes={
                    "style:name": "cell_date",
                    "style:family": "table-cell",
                    "style:data-style-name": date_style.name,
                },
            ),
        )
    document_content.children.append(GeneralElement("office:body", text))
    return text


def parse_document(z):
    manifest = parse_xml_str(ELEMENT_MAP, z.read("META-INF/manifest.xml"))
    kwargs = {}
    for entry in manifest.children:
        if entry.full_path == "/":
            continue
        element = parse_xml_str(ELEMENT_MAP, z.read(entry.full_path))
        kwarg = element.tag_name.split("-")[-1]
        kwargs[kwarg] = element
    doc = Document(**kwargs)
    return doc.document_content.body_root


__all__ = [
    "Cell",
    "DateStyle",
    "H",
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "P",
    "Span",
    "Table",
    "create_spreadsheet",
    "parse_spreadsheet",
]
