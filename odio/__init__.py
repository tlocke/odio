import odio.v1_1
import odio.v1_2
import zipfile
import xml.dom.minidom

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def create_spreadsheet(f, version='1.2'):
    if version == '1.1':
        return odio.v1_1.SpreadsheetWriter(f)
    elif version == '1.2':
        return odio.v1_2.SpreadsheetWriter(f)
    else:
        raise Exception(
            "The version '" + str(version) +
            "' isn't recognized. The valid version strings are '1.1' "
            "and '1.2'.")


def read_spreadsheet(f):
    with zipfile.ZipFile(f, 'r') as z:
        content = z.read('content.xml')
    f.close()
    dom = xml.dom.minidom.parseString(content)
    version = dom.documentElement.getAttribute('office:version')
    spreadsheet_elem = dom.getElementsByTagName('office:spreadsheet')[0]

    if version == '1.1':
        return odio.v1_1.SpreadsheetReader(spreadsheet_elem)
    elif version == '1.2':
        return odio.v1_2.SpreadsheetReader(spreadsheet_elem)
    else:
        raise Exception(
            "The version '" + str(version) +
            "' isn't recognized. The valid version strings are '1.1' "
            "and '1.2'.")
