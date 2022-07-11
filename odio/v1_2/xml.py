from abc import ABC
from collections import UserDict, UserList
from io import StringIO
from xml.dom import Node
from xml.dom.minidom import parseString


class OdioException(Exception):
    pass


class Children(UserList):
    def __init__(self, iterable=None, *, allowed=()):
        self.allowed = allowed
        super().__init__()
        if iterable is not None:
            for v in iterable:
                self.append(v)

    """
    "__iadd__", "__imul__", "__init__", "__init_subclass__", "__iter__", "__le__",
    "__len__", "__lt__", "__mul__", "__ne__", "__new__", "__reduce__", "__reduce_ex__",
    "__repr__", "__reversed__", "__rmul__", "__setattr__", "__setitem__", "__sizeof__",
    "__str__", "__subclasshook__", "append", "clear", "copy", "count", "extend",
    "index", "insert", "pop", "remove", "reverse", "sort"
    """

    def __iadd__(self, other):
        for v in other:
            self.append(v)

    def __delitem__(self):
        raise OdioException("Children are append-only in Odio.")

    def __setitem__(self, val):
        raise OdioException("Children are append-only in Odio.")

    def append(self, value):
        if len(self.allowed) == 0:
            raise OdioException("No children are allowed for this element.")

        if isinstance(value, str):
            if str not in self.allowed and "*" not in self.allowed:
                raise OdioException(
                    f"Children of type str aren't allowed for this element. The "
                    f"allowed children are {self.allowed}."
                )
            else:
                if len(self.data) > 0 and isinstance(self.data[-1], str):
                    val = self.data[-1] + value
                else:
                    val = value

        elif isinstance(value, Element):
            if value.tag_name not in self.allowed and "*" not in self.allowed:
                raise OdioException(
                    f"Children with tag name {value.tag_name} aren't allowed for this "
                    f"element. The allowed types of children are {self.allowed}."
                )
            else:
                super().append(value)
        else:
            raise OdioException(
                f"A child must be a str or a subclass of Element, but found a "
                f"{type(value)}"
            )


class Attributes(UserDict):
    def __init__(self, dictionary=None, allowed=None):
        self._allowed = {} if allowed is None else allowed
        super().__init__()
        if dictionary is not None:
            for k, v in dictionary.items():
                self[k] = v

    def __setitem__(self, k, v):
        self._check_pair(k, v)
        super().__setitem__(k, v)

    def _check_pair(self, k, v):
        if not isinstance(k, str):
            raise OdioException(
                f"The type of an attribute name must be str. Found {type(k)}"
            )
        if not isinstance(v, str):
            raise OdioException(
                f"The type of an attribute value must be str. Found {type(v)}"
            )

        if k not in self._allowed and "*" not in self._allowed:
            raise OdioException(
                f"The name of the attribute was {k} but it must be one of "
                f"{self._allowed}"
            )


class Element(ABC):
    def __init__(
        self, *children, attributes=None, allowed_attributes=None, allowed_children=None
    ):
        self.attributes = Attributes(attributes, allowed=allowed_attributes)
        self.children = Children(children, allowed=allowed_children)

    def __repr__(self):
        return f"odio.Element({self.tag_name})"

    def __eq__(self, other):
        return (
            isinstance(other, Element)
            and self.tag_name == other.tag_name
            and self.children == other.children
            and self.attributes == other.attributes
        )

    def to_text(self):
        return "".join(n for n in self.children if isinstance(n, str))

    def find_children_by_name(self, tag_name):
        return [c for c in self.children if c.tag_name == tag_name]

    def pack(self):
        return self

    def unpack(self):
        return self

    def find_descendants_by_name(self, tag_name):
        descendants = []
        for child in self.children:
            if isinstance(child, str):
                continue
            else:
                if child.tag_name == tag_name:
                    descendants.append(child)
                descendants.extend(child.find_descendants_by_name(tag_name))

        return descendants

    def __str__(self):
        return element_to_str(self)


class GeneralElement(Element):
    def __init__(self, tag_name, *children, attributes=None, fill=True):
        self.tag_name = tag_name
        allowed_attributes = {"*"}
        allowed_children = {"*"}
        super().__init__(
            *children,
            attributes=attributes,
            allowed_attributes=allowed_attributes,
            allowed_children=allowed_children,
        )


def escape(data):
    return data.replace("&", "&amp;").replace(">", "&gt;").replace("<", "&lt;")


def quoteattr(data):
    d = escape(data)

    if '"' in d:
        if "'" in d:
            return f'''"{d.replace('"', '&quot;')}"'''
        else:
            return f"'{d}'"
    else:
        return f'"{d}"'


def atts_to_str(attrs):
    if len(attrs) == 0:
        return ""
    else:
        return " " + " ".join(f"{k}={quoteattr(v)}" for k, v in sorted(attrs.items()))


def write_line(f, indent, line):
    f.write(f"{indent}{line}\n")


def write_element(f, indent, element):
    element = element.pack()
    tag_name = element.tag_name
    att_str = atts_to_str(element.attributes)
    children = element.children

    if len(children) == 0:
        write_line(f, indent, f"<{tag_name}{att_str}/>")
    elif len(children) == 1 and isinstance(children[0], str):
        write_line(f, indent, f"<{tag_name}{att_str}>{children[0]}</{tag_name}>")
    else:
        write_line(f, indent, f"<{tag_name}{att_str}>")
        new_indent = f"{indent}  "
        for child in children:
            if isinstance(child, str):
                write_line(f, new_indent, escape(child))
            else:
                write_element(f, new_indent, child)

        write_line(f, indent, f"</{tag_name}>")


def document_to_str(document):
    with StringIO() as f:
        write_document(f, document)
        return f.getvalue()


def element_to_str(element):
    with StringIO() as f:
        write_element(f, "", element)
        return f.getvalue()


def write_document(f, element):
    write_line(f, "", '<?xml version="1.0" encoding="utf-8"?>')
    write_element(f, "", element)


def parse_xml_str(element_map, xml_str):
    dom = parseString(xml_str)
    return parse_element(element_map, dom.documentElement)


def parse_element(element_map, node):

    tag = node.tagName

    try:
        cls = element_map[tag]["cls"]
        try:
            element = cls(fill=False)
        except TypeError as e:
            raise OdioException(f"Problem with {cls}: {e}")
    except KeyError:
        try:
            element = GeneralElement(tag, fill=False)
        except TypeError as e:
            raise OdioException(f"Problem with {cls}: {e}")

    for i in range(node.attributes.length):
        attr = node.attributes.item(i)
        element.attributes[attr.name] = attr.value

    child_nodes = node.childNodes

    if str in element.children.allowed and len(element.children.allowed) == 1:
        element.children.append(child_nodes.item(0).nodeValue)
    else:
        for i in range(child_nodes.length):
            child_node = child_nodes.item(i)
            node_type = child_node.nodeType
            if node_type == Node.TEXT_NODE:
                fnode = child_node.nodeValue
                snode = fnode.strip()

                if len(snode) == 0:
                    continue

                if i > 0 and len(fnode.lstrip()) < len(fnode):
                    child = f" {snode}"

                elif i < (child_nodes.length - 1) and len(fnode.rstrip()) < len(fnode):
                    child = f"{snode} "

                else:
                    child = snode

                element.children.append(child)

            elif node_type == Node.ELEMENT_NODE:

                if (
                    child_node.tagName == "table:table-cell"
                    and "table:number-columns-repeated" in element.attributes
                ):
                    repeats = int(element.attributes["table:number-columns-repeated"])
                else:
                    repeats = 1

                for i in range(repeats):
                    element.children.append(parse_element(element_map, child_node))

            else:
                raise OdioException(f"Node type {node_type} not recognised.")

    return element.unpack()
