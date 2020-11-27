from pyexcel_ods import get_data
import pyexcel as pe
import json

data = get_data("Global.ods")
sheets = pe.get_book(file_name="Global.ods")
print(json.dumps(data))
print(sheets)
