from datetime import datetime as Datetime

from odio.v1_2 import DateStyle, create_spreadsheet

s = create_spreadsheet(date_style=DateStyle())
table = s.append_table("hello")
table.append_row([Datetime(2022, 6, 1)])
s.save("try.ods")
