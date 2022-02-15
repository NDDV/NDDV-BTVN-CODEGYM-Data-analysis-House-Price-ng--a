#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('house_price_dống-da.xlsx')
df.info()
#%%
#Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên

df_2 = df[(df['type_of_land'] == 'Bán nhà riêng') & (df['ward_name'].isin(['Phường Trung Liệt','Phường Khâm Thiên']))]
df_2
# %%
#Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên
df_3 = df_2[['address','price','house_direction','balcony_direction','land_certificate','bedroom']]
df_3 = df_3[(df_3['land_certificate'] == 'Sổ đỏ') & (df_3['bedroom']==3)]
df_3
# %%
#Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.
typeofland = df['type_of_land'].unique()
for i in typeofland:
    print(i)
    print('trung bình cộng giá',df[df['type_of_land'] == i]['price'].median())
    print('giá nhỏ nhất',df[df['type_of_land'] == i]['price'].min())
    print('giá lớn nhất',df[df['type_of_land'] == i]['price'].max())
    print('\n')
# %%
wardname = df['ward_name'].unique()
for i in wardname:
    print(i)
    print('Trung bình cộng số phòng ngủ',df[df['ward_name'] == i]['bedroom'].median())
    print('Trung bình cộng số phòng vệ sinh',df[df['ward_name'] == i]['toilet'].median())
    print('Trung bình cộng số tầng',df[df['ward_name'] == i]['floor'].median())
    print('\n')

# %%
