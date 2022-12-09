import pandas as pd

#   pip install xlrd==1.2.0 needed

cols = [0, 4]

excel_data = pd.read_excel('/home/skwaweru254/Excel/salesContacts.xlsx', usecols=cols)

data = pd.DataFrame(excel_data)

print(data)


#   Convert csv to excel using few lines
cols1 = [1, 2]

csv_data = pd.read_csv('/home/skwaweru254/passwords.csv', usecols=cols1)

df = pd.DataFrame(csv_data)

convert_excel = csv_data.to_excel('/home/skwaweru254/passwords.xlsx')

print(df)

print(convert_excel)
