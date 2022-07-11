from itertools import chain


class Element:
    def __init__(self, name, *sub_nodes, **attributes):
        self.sub_nodes = sub_nodes
        self.attributes = attributes
        self.name = name

    def __repr__(self):
        arg_str = ", ".join(
            chain(
                (repr(node) for node in self.nodes),
                (f"{k}={repr(v)}" for k, v in self.attributes.items()),
            )
        )
        return f"odio.{self.__class__.__name__}({arg_str})"

    def __eq__(self, other):
        return (
            isinstance(other, Element)
            and self.name == other.name
            and self.nodes == other.nodes
            and self.attrs == other.attrs
        )

    def attach(self, doc, parent_elem):
        node_elem = doc.createElement(self.name)
        parent_elem.appendChild(node_elem)
        for k, v in self.attributes.items():
            try:
                i = k.index("_")
            except ValueError:
                raise OdioException(
                    f"Problem with the attribute '{k}'. Attributes must have a "
                    f"namespace prefix, eg. 'text_'."
                )
            node_elem.setAttribute(k[:i] + ":" + k[i + 1 :], v)
        if isinstance(self, H):
            node_elem.setAttribute("text:outline-level", self.name[-1])
        for node in self.nodes:
            if isinstance(node, str):
                node_elem.appendChild(doc.createTextNode(node))
            else:
                node.attach(doc, node_elem)

    @property
    def text(self):
        return "".join(n for n in self.nodes if isinstance(n, str))


class H(Element):
    def __init__(self, *nodes, **attrs):
        super().__init__("text:h", *nodes, **attrs)


class P(Element):
    def __init__(self, *nodes, **attrs):
        super().__init__("text:p", *nodes, **attrs)


class Span(Element):
    def __init__(self, *nodes, **attrs):
        super().__init__("text:span", *nodes, **attrs)


class A(Element):
    XLINK_HREF = "xlink:href"

    def __init__(self, *nodes, href=None, **attrs):
        super().__init__("text:a", *nodes, **attrs)
        if href is not None:
            if A.XLINK_HREF in self.attrs:
                raise OdioException(
                    f"The keywords 'href' and '{A.XLINK_HREF}' can't both be present "
                    f"as they are synonyms."
                )
            else:
                self.attrs[A.XLINK_HREF] = href

    @property
    def href(self):
        return self.attrs.get(A.XLINK_HREF)
