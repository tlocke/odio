====
Odio
====

A pure-Python library for the import / export of
`ODF <http://en.wikipedia.org/wiki/OpenDocument>`_ (``.ods`` and ``.odt``) documents.
Licensed under the `MIT Licence <http://opensource.org/licenses/MIT>`_. Odio runs on
Python 3.7+ and supports ODF 1.1 and 1.2.

.. image:: https://github.com/tlocke/odio/workflows/odio/badge.svg
   :alt: Build Status

.. contents:: Table of Contents
   :depth: 1
   :local:


Installation
------------

It's a good idea to set up a virtualenv::

  python3 -m venv venv
  source venv/bin/activate

then install Odio with pip::

  pip install odio


Examples
--------

Create And Save A Spreadsheet
`````````````````````````````

>>> from odio.v1_2 import create_spreadsheet, Cell
>>> import datetime
>>> 
>>>
>>> # Create the spreadsheet.
>>> sheet = create_spreadsheet()
>>>	
>>> # Add a table (tab) to the spreadsheet
>>> table = sheet.append_table('Plan')
>>> table.append_row(
...     [
...         "veni, vidi, vici", 0.3, 5, Cell(formula='=B1 + C1'),
...         datetime.datetime(2015, 6, 30, 16, 38),
...     ]
... )
>>>
>>> with open('test.ods', 'wb') as f:
...     sheet.save(f)


Parse a spreadsheet
```````````````````

>>> from odio import parse_document
>>>
>>>
>>> # Parse the document we just created.
>>> with open('test.ods', 'rb') as f:
...     sheet = parse_document(f)
>>>
>>> table = sheet.tables[0]
>>> print(table.name)
Plan
>>> for row in table.rows:
...     print(row.get_values())
['veni, vidi, vici', 0.3, 5.0, '=B1 + C1', datetime.datetime(2015, 6, 30, 16, 38)]


Create And Save A Text Document
```````````````````````````````

>>> from odio.v1_2 import create_text, P, H1, H2, Span
>>> 
>>>
>>> txt = create_text()
>>>	
>>> txt.children.append(H1("The Meditations"))
>>> txt.children.append(H2("Book One"))
>>> txt.children.append(
...     P(
...         "From my grandfather Verus: the lessons of noble character ",
...         "and even temper."
...     )
... )
>>> txt.children.append(
...     P(
...         "From my father's reputation and my memory of "
...         "him: modesty and manliness."
...     )
... )
>>>
>>> with open('test.odt', 'wb') as f:
...     txt.save(f)


Parse a text document
`````````````````````

>>> from odio import parse_document
>>>
>>>
>>> # Parse the text document we just created.
>>> txt = parse_document(open('test.odt', "rb"))
>>> 
>>> # Find a child
>>> child = txt.children[2] 
>>> print(child.tag_name)
text:p
>>>
>>> print(child)
<text:p>
  From my grandfather Verus I learned good morals and the government of my temper. ')


Hyperlinks
``````````

In a text document:

>>> from odio import A, P, create_text
>>>
>>> txt = create_text()
>>> txt.append(
...     P("The 12 books of "),
...     A("The Meditations", href="https://en.wikipedia.org/wiki/Meditations"),
...     P(" is written in Greek")
... )
>>>
>>> print(txt.nodes[1].href)
https://en.wikipedia.org/wiki/Meditations

and within a cell of a spreadsheet:

>>> sheet = create_spreadsheet()
>>> row = [
...     Cell(
...         P("The 12 books of "),
...         A("The Meditations", href="https://en.wikipedia.org/wiki/Meditations"),
...         P(" is written in Greek")
...     ),
... ]
>>>
>>> table = sheet.append_table('Book IX', [row])
>>>
>>> cell = table.rows[0][0]
>>> print(cell)
>>> print(cell.nodes[1].href)


Style
`````

>>> from odio.v1_2 import create_text, P, H, Span
>>> 
>>>
>>> txt = create_text()
>>>	
>>> txt.children.append(
...     H1("The Meditations", text_style_name='Title'),
...     H("Book One", text_style_name='Heading 1'),
...     P(
...         "From my grandfather ",
...         Span("Verus", text_style_name='Strong Emphasis'),
...         " I learned good morals and the government of my temper."
...     ),
...     P(
...         "From the reputation and remembrance of my father, "
...         "modesty and a ", Span("manly", text_style_name='Emphasis'),
...         " character."
...     )
... )
>>>
>>> with open('test.odt', 'wb') as f:
>>>     txt.save(f)
References
----------

- `ODF 1.1
  <http://docs.oasis-open.org/office/v1.1/OS/OpenDocument-v1.1-html/OpenDocument-v1.1.html>`_

- `ODF 1.2 <https://docs.oasis-open.org/office/v1.2/OpenDocument-v1.2.html>`_


Regression Tests
----------------

To run the regression tests, install `tox <http://testrun.org/tox/latest/>`_::

  pip install tox

then run ``tox`` from the ``odio`` directory::

  tox


Doing A Release Of Odio
-----------------------

Run ``tox`` make sure all tests pass, then update the release notes and then do::

  git tag -a x.y.z -m "version x.y.z"
  rm -r build; rm -r dist
  python -m build
  twine upload --sign dist/*


Release Notes
-------------

Version 0.0.22, 2021-02-08
``````````````````````````

- Substitute ``<text:line-break/>`` for line breaks.


Version 0.0.21, 2021-02-05
``````````````````````````

- Finding text should never result in a ``None``.


Version 0.0.20, 2021-02-04
``````````````````````````

- Text should appear in the content of a ``<text:p>`` element within a cell.


Version 0.0.19, 2021-02-04
``````````````````````````

- Where line breaks appear in a text element's content, they are now replaced by a
  ``<text:line-break/>`` element. This means that line breaks appear in the
  spreadsheet, whereas before they didn't.


Version 0.0.18, 2019-11-29
``````````````````````````

- Performance improvement: rather than use the ``xml.sax.saxutils`` versions of
  ``escape`` and ``quoteattr`` I've copied them into the source of Odio, but removing
  the code for entities that aren't needed.


Version 0.0.17, 2018-08-19
``````````````````````````

- When parsing a spreadsheet cell of text type, if the value isn't contained in the
  attribute, recursively use the next nodes in the element contents.


Version 0.0.16, 2018-06-01
``````````````````````````

- Support the boolean type.


Version 0.0.15, 2017-03-29
``````````````````````````

- Fix bug where XML attribute values aren't escaped.


Version 0.0.14, 2017-03-28
``````````````````````````

- Use a streaming approach to file processing rather than an in-memory
  approach. This uses much less memory.


Version 0.0.13, 2017-03-09
``````````````````````````

- Bug where a file was closed when it was passed into a create_spreadsheet for
  ODF version 1.2.


Version 0.0.12, 2017-03-09
``````````````````````````

- The file-like object passed into the parse_* and create_* functions are no
  longer closed when the returned object is closed.


Version 0.0.11, 2017-03-07
``````````````````````````

- Support the ``table:number-columns-repeated`` attribute.


Version 0.0.10, 2017-03-07
``````````````````````````

- Spreadsheet: Python ``None`` corresponds to a ``table-cell`` with no attributes.

- Automate continuous integration with TravisCI.


Version 0.0.9, 2017-03-03
`````````````````````````

- Passes tests with Python 3.5.
- Can now export uncompressed spreadsheets.


Version 0.0.8, 2015-08-02
`````````````````````````

- Change ``read_spreadsheet`` to ``parse_spreadsheet``.
- Add support for formulas.


Version 0.0.7, 2015-07-17
`````````````````````````

- Can now read ODS spreadsheets. See Quickstart section for details.

- The ``append_row()`` method now accepts a single sequence type, rather than an
  arbitrary number of positional parameters.

- API changed so that only the top level ``odio`` package needs to be imported. The
  ``create_spreadsheet()`` function is new, and accepts an ODF version string
  ('1.1', '1.2').


Version 0.0.5, 2015-06-13
`````````````````````````

- Fixed links on readme file.


Version 0.0.4, 2015-06-13
`````````````````````````

- Renamed OdsOut to Spreadsheet to make things more intuitive.


Version 0.0.3, 2015-06-13
`````````````````````````

- Added support for ODF 1.2.


Version 0.0.1, 2015-05-25
`````````````````````````

- Make wheel setting 'universal'.


Version 0.0.0, 2015-05-25
`````````````````````````

- Initial release, nothing to see yet.
