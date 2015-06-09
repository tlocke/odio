import zipfile
import os.path

with zipfile.ZipFile('test.ods', 'w') as z:
    z.writestr('mimetype', 'application/vnd.oasis.opendocument.spreadsheet')
    os.chdir('unpacked')
    for pth, dirs, fls in os.walk('.'):
        for fname in fls:
            z.write(os.path.join(pth, fname))
