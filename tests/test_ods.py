from odio.v1_1 import OdsOut
import datetime

def test_writerow():
    out = OdsOut(open("test.ods", "wb"))
    out.writerow("veni, vidi, vici", 1, 0.7, datetime.datetime(2015, 5, 22))
    out.close()

test_writerow()
