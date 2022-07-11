import xml.dom.minidom
import zipfile

import odio.v1_1
import odio.v1_2
from odio.common import H, P, Span


def create_spreadsheet(version="1.2"):
    if version == "1.1":
        return odio.v1_1.create_spreadsheet()
    elif version == "1.2":
        return odio.v1_2.create_spreadsheet()
    else:
        raise Exception(
            f"The version '{version}' isn't recognized. The valid version strings "
            f"are '1.1' and '1.2'."
        )


def parse_document(f):
    with zipfile.ZipFile(f, "r") as z:
        dom = xml.dom.minidom.parseString(z.read("META-INF/manifest.xml"))
        version = dom.documentElement.getAttribute("manifest:version")

        if version == "1.1":
            return odio.v1_1.parser.parse_node(dom)
        elif version == "1.2":
            return odio.v1_2.parse_document(z)
        else:
            raise Exception(
                "The version '{version}' isn't recognized. The valid version strings "
                "are '1.1' and '1.2'."
            )


class Formula:
    def __init__(self, formula):
        self.formula = formula

    def __repr__(self):
        return f"odio.Formula('{self.formula}')"

    def __str__(self):
        return self.formula

    def __eq__(self, other):
        return isinstance(other, Formula) and self.formula == other.formula


def create_text(f, version="1.2"):
    if version == "1.1":
        return odio.v1_1.TextWriter(f)
    elif version == "1.2":
        return odio.v1_2.TextWriter(f)
    else:
        raise Exception(
            f"The version '{version}' isn't recognized. The valid version strings "
            f"are '1.1' and '1.2'."
        )


def parse_text(f):
    with zipfile.ZipFile(f, "r") as z:
        content = z.read("content.xml")
    f.close()
    dom = xml.dom.minidom.parseString(content)
    version = dom.documentElement.getAttribute("office:version")
    text_elem = dom.getElementsByTagName("office:text")[0]

    if version == "1.1":
        return odio.v1_1.TextReader(text_elem)
    elif version == "1.2":
        return odio.v1_2.TextReader(text_elem)
    else:
        raise Exception(
            f"The version '{version}' isn't recognized. The valid version strings "
            f"are '1.1' and '1.2'."
        )


__all__ = ["H", "P", "Span"]
