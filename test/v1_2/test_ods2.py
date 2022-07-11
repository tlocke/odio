import datetime
import os
from zipfile import ZipFile

from odio.v1_2 import Cell, create_spreadsheet, parse_document


def normalized_walk(path):
    return list(
        [os.path.relpath(pth, path), sorted(dirs), sorted(fls)]
        for pth, dirs, fls in sorted(os.walk(path))
    )


def test_create_parse_spreadsheet(tmpdir):
    TABLE_NAME = "Plan"
    py_1 = "veni, vidi, vici"
    py_2 = 0.3
    py_3 = py_4 = 5
    py_5 = "=B1 + C1"
    py_6 = datetime.datetime(2015, 6, 30, 16, 38)
    py_7 = None
    py_8 = "Dombey & Son"
    py_9 = True
    ROW = [
        py_1,
        py_2,
        py_3,
        py_4,
        Cell(formula=py_5),
        py_6,
        py_7,
        py_8,
        py_9,
    ]
    fname = tmpdir.join("actual.ods")
    sheet = create_spreadsheet()
    table = sheet.append_table(TABLE_NAME)
    table.append_row(ROW)

    with open(str(fname), "wb") as f:
        sheet.save(f)
    actual_dir = str(tmpdir.mkdir("actual"))
    with ZipFile(str(fname)) as z:
        z.extractall(actual_dir)

    desired_dir = str(os.path.join(os.path.dirname(__file__), "unpacked"))

    actual_walk = normalized_walk(actual_dir)
    desired_walk = normalized_walk(desired_dir)
    assert actual_walk == desired_walk

    for i, (actual_pth, actual_dirs, actual_fls) in enumerate(actual_walk):
        desired_pth, desired_dirs, desired_fls = desired_walk[i]
        for j, actual_fl in enumerate(actual_fls):
            desired_fl = desired_fls[j]
            with open(
                os.path.join(actual_dir, actual_pth, actual_fl)
            ) as actual_f, open(
                os.path.join(desired_dir, desired_pth, desired_fl)
            ) as desired_f:
                ac = "".join(actual_f)
                de = "".join(desired_f)
                print(ac)
                print(de)
                assert ac == de

    with open(str(fname), "rb") as f:
        with ZipFile(f) as z:
            sheet = parse_document(z)

    table = sheet.tables[0]
    assert table.name == TABLE_NAME
    expected_row = [
        py_1,
        py_2,
        py_3,
        py_4,
        py_5,
        py_6,
        py_7,
        py_8,
        py_9,
    ]
    actual_row = table.rows[0].get_values()
    assert actual_row == expected_row


def test_file_not_closed(tmpdir):
    fname = tmpdir.join("test.ods")
    f = open(str(fname), "wb")
    sheet = create_spreadsheet()
    table = sheet.append_table("Keats")
    table.append_row(("Season", "of", "mists"))
    sheet.save(f)
    f.seek(0)
    f.close()
