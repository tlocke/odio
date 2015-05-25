from odfio.v1_1 import OdsOut

def test_writerow():
    out = OdsOut(open("test.ods", "wb"))
    out.writerow("hello", 1, datetime.datetime(2015, 5, 22))
    out.close()
