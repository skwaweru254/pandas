import pandas as pd

#   pip install xlrd==1.2.0 needed

excel_data = pd.read_excel('/home/skwaweru254/Excel/salesContacts.xlsx')

data = pd.DataFrame(excel_data, columns=[])

print(excel_data)

