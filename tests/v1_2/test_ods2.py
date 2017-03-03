import odio
import datetime
import zipfile
import os


def test_create_parse_spreadsheet(tmpdir):
    TABLE_NAME = 'Plan'
    ROW = [
        "veni, vidi, vici", 0.3, 5, odio.Formula('=B1 + C1'),
        datetime.datetime(2015, 6, 30, 16, 38), None]
    fname = tmpdir.join('actual.ods')
    with odio.create_spreadsheet(open(str(fname), "wb"), '1.2') as sheet:
        table = sheet.append_table(TABLE_NAME)
        table.append_row(ROW)
    actual_dir = tmpdir.mkdir('actual')
    with zipfile.ZipFile(str(fname)) as z:
        z.extractall(str(actual_dir))

    desired_dir = os.path.join(os.path.dirname(__file__), 'unpacked')

    actual_walk = list(os.walk(str(actual_dir)))
    t_actual_walk = list(
        (os.path.relpath(pth, str(actual_dir)), dirs, fls)
        for pth, dirs, fls in actual_walk)
    desired_walk = list(os.walk(str(desired_dir)))
    t_desired_walk = list(
        (os.path.relpath(pth, str(desired_dir)), dirs, fls)
        for pth, dirs, fls in desired_walk)
    assert t_actual_walk == t_desired_walk

    for i, (actual_pth, actual_dirs, actual_fls) in enumerate(actual_walk):
        desired_pth, desired_dirs, desired_fls = desired_walk[i]
        for j, actual_fl in enumerate(actual_fls):
            desired_fl = desired_fls[j]
            actual_f = open(os.path.join(actual_pth, actual_fl))
            desired_f = open(os.path.join(desired_pth, desired_fl))
            ac = ''.join(actual_f)
            de = ''.join(desired_f)
            print(ac, de)
            assert ac == de

    sheet = odio.parse_spreadsheet(open(str(fname), 'rb'))
    table = sheet.tables[0]
    assert table.name == TABLE_NAME
    print(type(table.rows[0][3].formula), type(ROW[3].formula))
    print(table.rows[0], ROW)
    assert table.rows[0] == ROW
