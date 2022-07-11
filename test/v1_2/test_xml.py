from io import StringIO
from xml.dom.minidom import parseString

import pytest

from odio.v1_2.xml import (
    Attributes,
    Children,
    Element,
    GeneralElement,
    OdioException,
    document_to_str,
    element_to_str,
    parse_element,
    parse_xml_str,
    write_element,
    write_line,
)


def test_Attributes_init():
    Attributes({})


def test_Attributes_init_v_none():
    with pytest.raises(
        OdioException,
        match="The type of an attribute value must be str. Found <class 'NoneType'>",
    ):
        Attributes({"version": None})


def test_Attributes_setitem_v_none():
    attrs = Attributes()
    with pytest.raises(
        OdioException,
        match="The type of an attribute value must be str. Found <class 'NoneType'>",
    ):
        attrs["version"] = None


def test_Attributes_repr():
    repr(Attributes({"version": "1.2"}, allowed={"version"}))


def test_Children_check_type():
    with pytest.raises(
        OdioException,
        match="A child must be a str or a subclass of Element, but found a "
        "<class 'dict'>",
    ):
        Children([{}], allowed=(str,))


def test_Children_iadd():
    with pytest.raises(
        OdioException,
        match="A child must be a str or a subclass of Element, but found a "
        "<class 'int'>",
    ):
        children = Children([], allowed=(str,))
        children += [1]


def test_Children_append_mixed():
    children = Children([], allowed=("*",))
    children.append(" modesty and a ")
    children.append(" manly character ")
    assert children == ["modesty and a manly character"]


def test_Children_append_cdata():
    pass


def test_Children_append_elements():
    pass


def test_GeneralElement_find_descendants_by_name():
    element = GeneralElement("table")
    assert element.find_descendants_by_name("row") == []


def test_write_line():
    with StringIO() as f:
        write_line(f, "", "<spreadsheet>")


def test_write_element_simple():
    element = GeneralElement("spreadsheet")
    with StringIO() as f:
        write_element(f, "", element)
        assert f.getvalue() == "<spreadsheet/>\n"


def test_write_element_attributes():
    element = GeneralElement("spreadsheet", attributes={"version": "1.2"})
    with StringIO() as f:
        write_element(f, "", element)
        assert f.getvalue() == '<spreadsheet version="1.2"/>\n'


def test_write_element():
    element = GeneralElement("spreadsheet", GeneralElement("table"))
    with StringIO() as f:
        write_element(f, "", element)
        expected = """<spreadsheet>
  <table/>
</spreadsheet>
"""
        assert f.getvalue() == expected


def test_write_element_single_str_child():
    element = GeneralElement("spreadsheet", "*")
    with StringIO() as f:
        write_element(f, "", element)
        expected = "<spreadsheet>*</spreadsheet>\n"
        assert f.getvalue() == expected


def test_GeneralElement_eq():
    a = GeneralElement("a")
    b = GeneralElement("a")
    assert a == b


def test_GeneralElement_find_children_by_name():
    spreadsheet = GeneralElement("spreadsheet")
    element = GeneralElement("document", spreadsheet, GeneralElement("text"))

    children = element.find_children_by_name("spreadsheet")

    assert children == [spreadsheet]


def test_GeneralElement_to_text():
    element = GeneralElement("cell", "")
    assert element.to_text() == ""


def test_GeneralElement_child_type():
    with pytest.raises(
        OdioException,
        match="A child must be a str or a subclass of Element, but found a "
        "<class 'dict'>",
    ):
        GeneralElement("table", {"name": "Alf"})


def test_document_to_str():
    element = GeneralElement("spreadsheet")
    document_to_str(element)


def test_element_to_str():
    element = GeneralElement("spreadsheet")
    element_to_str(element)


def test_element_to_str_text():
    element = GeneralElement(
        "p",
        "From my grandfather Verus: the lessons of noble character ",
        "and even temper.",
    )
    actual = element_to_str(element)
    assert (
        actual
        == """<p>
  From my grandfather Verus: the lessons of noble character
  and even temper.
</p>
"""
    )


def test_parse_element_one_str_child():
    xml_str = """<?xml version="1.0" encoding="UTF-8"?>
<cell> </cell>"""
    dom = parseString(xml_str)

    class Cell(Element):
        tag_name = "cell"

        def __init__(self, *children, attributes=None, fill=True):
            super().__init__(
                *children,
                attributes=attributes,
                allowed_attributes={},
                allowed_children={str}
            )

    element_map = {
        "cell": {
            "allowed_children": {str},
            "allowed_attributes": {},
            "cls": Cell,
        }
    }
    element = parse_element(element_map, dom.documentElement)
    assert element.children[0] == " "


def test_parse_xml_str(mocker):
    element_map = {}
    xml_str = """<?xml version="1.0" encoding="UTF-8"?>
  <p>electron</p>"""
    p = parse_xml_str(element_map, xml_str)
    assert p.children[0] == "electron"


def test_parse_xml_str_unpack(mocker):
    class Ul(Element):
        tag_name = "ul"

        def __init__(self, *children, attributes=None, fill=True):
            super().__init__(
                *children,
                attributes=attributes,
                allowed_attributes={},
                allowed_children={"li"}
            )

        def unpack(self):
            self.children.append(GeneralElement("li"))
            return self

    element_map = {"ul": {"cls": Ul}}
    xml_str = """<?xml version="1.0" encoding="UTF-8"?>
  <ul>
    <li>electron</li>
  </ul>"""
    ul = parse_xml_str(element_map, xml_str)
    assert len(ul.children) == 2
