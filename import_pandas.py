import pandas as pd

#   pip install xlrd==1.2.0 needed

cols = [0, 4]

excel_data = pd.read_excel('/home/skwaweru254/Excel/salesContacts.xlsx', usecols=cols)

data = pd.DataFrame(excel_data)

print(data)
