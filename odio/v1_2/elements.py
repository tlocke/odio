from copy import copy, deepcopy
from datetime import date as Date, datetime as Datetime, timedelta as Timedelta
from decimal import Decimal
from io import TextIOWrapper
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZipFile

from odio.v1_2.mapping import MAP
from odio.v1_2.xml import (
    Element,
    GeneralElement,
    OdioException,
    document_to_str,
    write_document,
)

ELEMENT_MAP = {}


class BaseElement(Element):
    def __init__(self, *children, attributes=None):
        allowed_attributes = ELEMENT_MAP[self.tag_name]["allowed_attributes"]
        allowed_children = ELEMENT_MAP[self.tag_name]["allowed_children"]
        super().__init__(
            *children,
            attributes=attributes,
            allowed_attributes=allowed_attributes,
            allowed_children=allowed_children,
        )


class LineBreak(BaseElement):
    def __init__(self, fill=True):
        super().__init__("text:line-break")


class Meta(BaseElement):
    def __init__(self, *children, attributes=None, fill=True):
        super().__init__("text:meta", *children, attributes=attributes)


class A(BaseElement):
    tag_name = "text:a"

    def __init__(self, *children, href=None, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            if href is not None:
                self.attributes["xlink:href"] = href
                self.attributes["xlink:type"] = "simple"


class H1(BaseElement):
    tag_name = "text:h"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["text:outline-level"] = "1"

    @property
    def level(self):
        return self.attributes.get("text:outline-level")


class H2(BaseElement):
    tag_name = "text:h"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["text:outline-level"] = "2"

    @property
    def level(self):
        return self.attributes.get("text:outline-level")


class H3(BaseElement):
    tag_name = "text:h"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["text:outline-level"] = "3"

    @property
    def level(self):
        return self.attributes.get("text:outline-level")


class H4(BaseElement):
    tag_name = "text:h"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["text:outline-level"] = "4"

    @property
    def level(self):
        return self.attributes.get("text:outline-level")


class H5(BaseElement):
    tag_name = "text:h"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["text:outline-level"] = "5"

    @property
    def level(self):
        return self.attributes.get("text:outline-level")


class H6(BaseElement):
    tag_name = "text:h"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["text:outline-level"] = "6"

    @property
    def level(self):
        return self.attributes.get("text:outline-level")


class H(BaseElement):
    LEVELS = {
        "1": H1,
        "2": H2,
        "3": H3,
        "4": H4,
        "5": H5,
        "6": H6,
    }
    tag_name = "text:h"

    def __init__(self, *children, level=None, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            if level is not None:
                self.attributes["text:outline-level"] = level

    @property
    def level(self):
        return self.attributes.get("text:outline-level")

    def unpack(self):
        level = self.level
        if level is None:
            return self
        else:
            cls = H.LEVELS[level]
            return cls(*self.children, attributes=self.attributes, fill=False)


class P(BaseElement):
    tag_name = "text:p"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)


class Manifest(BaseElement):
    tag_name = "manifest:manifest"

    def __init__(self, *children, media_type=None, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["manifest:version"] = "1.2"
            self.attributes[
                "xmlns:manifest"
            ] = "urn:oasis:names:tc:opendocument:xmlns:manifest:1.0"
            self.append_entry("/", media_type)

    def append_entry(self, full_path, media_type):
        self.children.append(
            ManifestFileEntry(full_path=full_path, media_type=media_type)
        )


class ManifestFileEntry(BaseElement):
    tag_name = "manifest:file-entry"

    def __init__(
        self, *children, attributes=None, full_path=None, media_type=None, fill=True
    ):
        super().__init__(attributes=attributes, *children)
        if fill:
            if full_path is not None:
                self.attributes["manifest:full-path"] = full_path
            if media_type is not None:
                self.attributes["manifest:media-type"] = media_type

    @property
    def full_path(self):
        return self.attributes["manifest:full-path"]

    @property
    def media_type(self):
        return self.attributes["manifest:media-type"]


class Cell(BaseElement):
    tag_name = "table:table-cell"

    def __init__(
        self,
        value=None,
        formula=None,
        currency=None,
        is_percentage=False,
        attributes=None,
        *children,
        fill=True,
    ):
        super().__init__(attributes=attributes, *children)
        if fill:
            if value is not None:
                if isinstance(value, bool):
                    self.attributes["office:value-type"] = "boolean"
                    self.attributes["office:boolean-value"] = (
                        "true" if value else "false"
                    )

                elif isinstance(value, (Decimal, float, int)):
                    if currency is not None:
                        self.attributes["office:currency"] = currency
                        self.attributes["office:value-type"] = "currency"
                    elif is_percentage:
                        self.attributes["office:value-type"] = "percentage"
                    else:
                        self.attributes["office:value-type"] = "float"

                    self.attributes["office:value"] = str(value)

                elif isinstance(value, Datetime):
                    self.attributes["table:style-name"] = "cell_date"
                    self.attributes["office:value-type"] = "date"
                    self.attributes["office:date-value"] = value.strftime(
                        "%Y-%m-%dT%H:%M:%S"
                    )

                elif isinstance(value, Date):
                    self.attributes["table:style-name"] = "cell_date"
                    self.attributes["office:value-type"] = "date"
                    self.attributes["office:date-value"] = value.strftime("%Y-%m-%d")

                elif isinstance(value, Timedelta):
                    self.attributes["table:style-name"] = "cell_date"
                    self.attributes["office:value-type"] = "time"
                    self.attributes["office:time-value"] = value.strftime("%H:%M:%S")

                elif value is None:
                    self.attributes["office:value-type"] = "void"

                elif isinstance(value, str):
                    self.attributes["office:value-type"] = "string"
                    self.attributes["office:string-value"] = value

            if formula is not None:
                if not formula.startswith("="):
                    raise OdioException("A formula must begin with a '='.")
                self.attributes["table:formula"] = f"of:{formula}"

    def get_value(self, decimals=False, ints=False):
        if "office:value-type" in self.attributes:
            if self.value_type == "boolean":
                return self.attributes["office:boolean-value"] == "true"

            elif self.value_type == "currency":
                return Decimal(self.attributes["office:value"])

            elif self.value_type == "date":
                return Datetime.strptime(
                    self.attributes["office:date-value"], "%Y-%m-%dT%H:%M:%S"
                )

            elif self.value_type == "float":
                val = self.attributes["office:value"]
                if ints:
                    try:
                        return int(val)
                    except ValueError:
                        pass

                if decimals:
                    return Decimal(val)

                return float(val)

            elif self.value_type == "percentage":
                val = self.attributes["office:value"]
                if ints:
                    try:
                        return int(val)
                    except ValueError:
                        pass

                if decimals:
                    return Decimal(val)

                return float(val)

            elif self.value_type == "string":
                return (
                    self.attributes["office:string-value"]
                    if "office:string-value" in self.attributes
                    else ""
                ) + self.to_text()

            elif self.value_type == "time":
                return val.strptime(self.attributes["office:time-value"], "%H:%M:%S")

            elif self.value_type == "void":
                return None

            else:
                return None

        elif "table:formula" in self.attributes:
            return self.formula
        else:
            return None

    @property
    def currency(self):
        return self.attributes.get("office:currency")

    @property
    def value_type(self):
        return self.attributes.get("office:value-type")

    @property
    def formula(self):
        try:
            f = self.attributes["table:formula"]
            eq_idx = f.index("=")
            return f[eq_idx:]
        except KeyError:
            return None


NAMESPACES = {
    "urn:oasis:names:tc:opendocument:xmlns:animation:1.0": "anim",
    "urn:oasis:names:tc:opendocument:xmlns:chart:1.0": "chart",
    "urn:oasis:names:tc:opendocument:xmlns:config:1.0": "config",
    "urn:oasis:names:tc:opendocument:xmlns:database:1.0": "db",
    "urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0": "dr3d",
    "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0": "draw",
    "urn:oasis:names:tc:opendocument:xmlns:form:1.0": "form",
    "urn:oasis:names:tc:opendocument:xmlns:manifest:1.0": "manifest",
    "urn:oasis:names:tc:opendocument:xmlns:meta:1.0": "meta",
    "urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0": "number",
    "urn:oasis:names:tc:opendocument:xmlns:office:1.0": "office",
    "urn:oasis:names:tc:opendocument:xmlns:presentation:1.0": "presentation",
    "urn:oasis:names:tc:opendocument:xmlns:script:1.0": "script",
    "urn:oasis:names:tc:opendocument:xmlns:table:1.0": "table",
    "urn:oasis:names:tc:opendocument:xmlns:text:1.0": "text",
    "urn:oasis:names:tc:opendocument:xmlns:style:1.0": "style",
    "http://docs.oasis-open.org/ns/office/1.2/meta/odf#": "odf",
    "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0": "fo",
    "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0": "svg",
    "urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0": "smil",
    "http://purl.org/dc/elements/1.1/": "dc",
    "http://www.w3.org/1998/Math/MathML": "math",
    "http://www.w3.org/2002/xforms": "xforms",
    "http://www.w3.org/1999/xlink": "xlink",
    "http://www.w3.org/1999/xhtml": "xhtml",
    "http://www.w3.org/2003/g/data-view#": "grddl",
    "http://docs.oasis-open.org/ns/office/1.2/meta/pkg#": "pkg",
    "urn:oasis:names:tc:opendocument:xmlns:of:1.2": "of",
}


class DocumentMeta(BaseElement):
    tag_name = "office:document-meta"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["office:version"] = "1.2"
            for k, v in NAMESPACES.items():
                if v in {"office", "xlink", "dc", "meta", "of"}:
                    self.attributes[f"xmlns:{v}"] = k
            self.children.append(
                GeneralElement("office:meta", GeneralElement("meta:generator", "Odio"))
            )


class DocumentSettings(BaseElement):
    tag_name = "office:document-settings"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["office:version"] = "1.2"
            for k, v in NAMESPACES.items():
                if v in {"office", "xlink", "config", "of"}:
                    self.attributes[f"xmlns:{v}"] = k


class DocumentStyles(BaseElement):
    tag_name = "office:document-styles"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["office:version"] = "1.2"
            for k, v in NAMESPACES.items():
                if v in {
                    "anim",
                    "chart",
                    "config",
                    "db",
                    "dr3d",
                    "draw",
                    "form",
                    "meta",
                    "number",
                    "office",
                    "presentation",
                    "script",
                    "table",
                    "text",
                    "style",
                    "odf",
                    "fo",
                    "svg",
                    "smil",
                    "dc",
                    "math",
                    "xforms",
                    "xlink",
                    "xhtml",
                    "grddl",
                    "pkg",
                    "of",
                }:
                    self.attributes[f"xmlns:{v}"] = k


class DocumentContent(BaseElement):
    tag_name = "office:document-content"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["office:version"] = "1.2"
            for k, v in NAMESPACES.items():
                if v in {
                    "anim",
                    "chart",
                    "config",
                    "db",
                    "dr3d",
                    "draw",
                    "form",
                    "meta",
                    "number",
                    "office",
                    "presentation",
                    "script",
                    "table",
                    "text",
                    "style",
                    "fo",
                    "svg",
                    "smil",
                    "dc",
                    "math",
                    "xforms",
                    "xlink",
                    "xhtml",
                    "grddl",
                    "of",
                }:
                    self.attributes[f"xmlns:{v}"] = k

    @property
    def body_root(self):
        office_body = self.find_children_by_name("office:body")[0]
        return office_body.children[0]


class Document:
    MIME_TYPES = {
        "office:text": "application/vnd.oasis.opendocument.text",
        "office:spreadsheet": "application/vnd.oasis.opendocument.spreadsheet",
    }

    def __init__(self, content=None, settings=None, meta=None, styles=None):
        self.document_content = DocumentContent() if content is None else content
        self.document_settings = DocumentSettings() if settings is None else settings
        self.document_meta = DocumentMeta() if meta is None else meta
        self.document_styles = DocumentStyles() if styles is None else styles

    def save(self, f, compressed=True):
        compression = ZIP_DEFLATED if compressed else ZIP_STORED
        body_root = self.document_content.body_root
        with ZipFile(f, "w", compression) as z:
            media_type = Document.MIME_TYPES[body_root.tag_name]
            z.writestr("mimetype", media_type)

            manifest = Manifest(media_type=media_type)

            for path, media_type, element in (
                ("settings.xml", "text/xml", self.document_settings),
                ("content.xml", "text/xml", self.document_content),
                ("meta.xml", "text/xml", self.document_meta),
                ("styles.xml", "text/xml", self.document_styles),
            ):
                manifest.append_entry(path, media_type)
                with z.open(path, "w") as f:
                    write_document(
                        TextIOWrapper(f, encoding="utf8", newline=""), element
                    )

            z.writestr("META-INF/manifest.xml", document_to_str(manifest))


class Span(BaseElement):
    tag_name = "text:span"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)


class Spreadsheet(BaseElement):
    tag_name = "office:spreadsheet"

    def __init__(self, *children, doc=None, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.doc = doc

    def append_table(self, name):
        table = Table(name=name)
        self.children.append(table)
        return table

    def save(self, f, compressed=True):
        return self.doc.save(f, compressed=compressed)

    @property
    def tables(self):
        return self.find_children_by_name("table:table")


class Text(BaseElement):
    tag_name = "office:text"

    def __init__(self, *children, doc=None, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.doc = doc

    def append_table(self, name):
        table = Table(name=name)
        self.children.append(table)
        return table

    def save(self, f, compressed=True):
        return self.doc.save(f, compressed=compressed)

    @property
    def tables(self):
        return self.find_children_by_name("table:table")


class Row(BaseElement):
    tag_name = "table:table-row"

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)

    def append_cell(self, value=None, formula=None, currency=None, is_percentage=False):

        if isinstance(value, Cell):
            cell = value

        else:
            cell = Cell(
                value=value,
                formula=formula,
                currency=currency,
                is_percentage=is_percentage,
            )

        self.children.append(cell)

    def get_values(self, decimals=False, ints=False):
        cells = self.find_children_by_name("table:table-cell")
        return [c.get_value(decimals=decimals, ints=ints) for c in cells]

    def pack(self):
        new_row = Row(attributes=self.attributes)
        cells = new_row.children

        prev_c = None
        for c in self.children:
            if c == prev_c:
                try:
                    repeats = int(cells[-1].attributes["table:number-columns-repeated"])
                except KeyError:
                    repeats = 1

                cells[-1].attributes["table:number-columns-repeated"] = str(repeats + 1)

            else:
                cells.append(c)

            prev_c = c

        return new_row

    def unpack(self):
        new_row = Row(attributes=self.attributes)
        cells = new_row.children

        for c in self.children:
            try:
                repeats = int(c.attributes["table:number-columns-repeated"])
            except KeyError:
                repeats = 1

            for _ in range(repeats):
                cells.append(copy(c))

        return new_row


class Table(BaseElement):
    tag_name = "table:table"

    def __init__(self, *children, name=None, attributes=None, fill=True):
        super().__init__(attributes=attributes, *children)
        if fill:
            if name is not None:
                self.attributes["table:name"] = name

            self.children.append(GeneralElement("table:table-column"))

    def append_row(self, row):
        row_element = Row()
        self.children.append(row_element)

        for val in row:
            row_element.append_cell(val)

    @property
    def rows(self):
        return self.find_descendants_by_name("table:table-row")

    @property
    def name(self):
        return self.attributes["table:name"]


class NumberText(BaseElement):
    tag_name = "number:text"
    allowed_types = (str,)

    def __init__(self, *children, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)


class NumberYear(BaseElement):
    tag_name = "number:year"

    def __init__(self, *children, is_long=True, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["number:style"] = "long" if is_long else "short"


class NumberMonth(BaseElement):
    tag_name = "number:month"

    def __init__(self, *children, is_long=True, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["number:style"] = "long" if is_long else "short"


class NumberDay(BaseElement):
    tag_name = "number:day"

    def __init__(self, *children, is_long=True, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["number:style"] = "long" if is_long else "short"


class NumberHours(BaseElement):
    tag_name = "number:hours"

    def __init__(self, *children, is_long=True, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["number:style"] = "long" if is_long else "short"


class NumberMinutes(BaseElement):
    tag_name = "number:minutes"

    def __init__(self, *children, is_long=True, attributes=None, fill=True):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["number:style"] = "long" if is_long else "short"


class DateStyle(BaseElement):
    tag_name = "number:date-style"

    def __init__(
        self,
        *children,
        name="date",
        year_long=True,
        year_month_sep="-",
        month_long=True,
        month_day_sep="-",
        day_long=True,
        day_hour_sep=" ",
        hour_long=True,
        hour_minute_sep=":",
        minute_long=True,
        attributes=None,
        fill=True,
    ):
        super().__init__(*children, attributes=attributes)
        if fill:
            self.attributes["style:name"] = name
            self.children.append(NumberYear(is_long=year_long))
            self.children.append(NumberText(year_month_sep))
            self.children.append(NumberMonth(is_long=month_long))
            self.children.append(NumberText(month_day_sep))
            self.children.append(NumberDay(is_long=day_long))
            self.children.append(NumberText(day_hour_sep))
            self.children.append(NumberHours(is_long=hour_long))
            self.children.append(NumberText(hour_minute_sep))
            self.children.append(NumberMinutes(is_long=minute_long))

    @property
    def name(self):
        return self.attributes["style:name"]


element_classes = {
    v.tag_name: v for k, v in globals().items() if hasattr(v, "tag_name")
}

for k, v in MAP.items():
    props = deepcopy(v)
    props["cls"] = element_classes.get(k)
    ELEMENT_MAP[k] = props
