from odio.v1_1 import OdsOut
import datetime
import zipfile
import os


def test_writerow(tmpdir):
    fname = tmpdir.join('actual.ods')
    with OdsOut(open(str(fname), "wb")) as out:
        table = out.append_table('Plan')
        table.append_row(
            (
                "veni, vidi, vici", 0.3, 5,
                datetime.datetime(2015, 6, 30, 16, 38)))
    actual_dir = tmpdir.mkdir('actual')
    with zipfile.ZipFile(str(fname)) as z:
        z.extractall(str(actual_dir))

    '''
    desired_dir = tmpdir.mkdir('desired')
    desired_name = os.path.join(os.path.dirname(__file__), 'test.ods')
    with zipfile.ZipFile(desired_name) as z:
        z.extractall(str(desired_dir))
    '''
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
            assert ''.join(actual_f) == ''.join(desired_f)
