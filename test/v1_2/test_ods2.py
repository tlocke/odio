import datetime
import os
import zipfile
from xml.dom.minidom import parseString

import odio


def normalized_walk(path):
    return list(
        [os.path.relpath(pth, path), sorted(dirs), sorted(fls)]
        for pth, dirs, fls in sorted(os.walk(path)))


def test_create_parse_spreadsheet(tmpdir):
    TABLE_NAME = 'Plan'
    ROW = [
        "veni, vidi, vici", 0.3, 5, 5, odio.Formula('=B1 + C1'),
        datetime.datetime(2015, 6, 30, 16, 38), None, "Dombey & Son", True]
    fname = tmpdir.join('actual.ods')
    with open(str(fname), 'wb') as f, \
            odio.create_spreadsheet(f, '1.2') as sheet:
        sheet.append_table(TABLE_NAME, [ROW])
    actual_dir = str(tmpdir.mkdir('actual'))
    with zipfile.ZipFile(str(fname)) as z:
        z.extractall(actual_dir)

    desired_dir = str(os.path.join(os.path.dirname(__file__), 'unpacked'))

    actual_walk = normalized_walk(actual_dir)
    desired_walk = normalized_walk(desired_dir)
    assert actual_walk == desired_walk

    for i, (actual_pth, actual_dirs, actual_fls) in enumerate(actual_walk):
        desired_pth, desired_dirs, desired_fls = desired_walk[i]
        for j, actual_fl in enumerate(actual_fls):
            desired_fl = desired_fls[j]
            actual_f = open(os.path.join(actual_dir, actual_pth, actual_fl))
            desired_f = open(
                os.path.join(desired_dir, desired_pth, desired_fl))
            ac = ''.join(actual_f)
            de = ''.join(desired_f)
            print(de)
            print(ac)
            assert ac == de

    sheet = odio.parse_spreadsheet(open(str(fname), 'rb'))
    table = sheet.tables[0]
    assert table.name == TABLE_NAME
    assert table.rows[0] == ROW


def test_parse_spreadsheet_cell_p():
    xml_str = """<?xml version="1.0" encoding="UTF-8"?>
<table:table
    xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"
    xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
    xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
    table:name="table1">
  <table:table-row>
    <table:table-cell office:value-type="string">
      <text:p>electron</text:p>
    </table:table-cell>
  </table:table-row>
</table:table>"""
    dom = parseString(xml_str)
    result = odio.v1_2.TableReader(dom.documentElement)
    assert result.rows[0][0] == 'electron'


def test_file_not_closed(tmpdir):
    fname = tmpdir.join('test.ods')
    f = open(str(fname), 'wb')
    with odio.create_spreadsheet(f, '1.2') as sheet:
        sheet.append_table('Keats', ('Season', 'of', 'mists'))
    f.seek(0)
    f.close()


def test_get_text():
    xml_str = """<?xml version="1.0" encoding="UTF-8"?>
<cell></cell>"""
    dom = parseString(xml_str)

    val = odio.v1_2._get_text(dom)
    assert val == ''
