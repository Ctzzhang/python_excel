# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
excel_file_path = 'test.xlsx'
df = pd.read_excel(excel_file_path)

print(df.columns)

# 读取第一列数据
first_column_data = df.iloc[:, 0]
a = df[1212]
print(first_column_data)

print(a)





# 对第一列数据进行处理（这里以示例为准，你需要根据实际需求进行处理）
processed_data = first_column_data.apply(lambda x: x * 2)  # 示例：将每个值乘以2

# 将处理后的数据写入第二列
df['NewColumnName'] = processed_data


# 打印修改后的数据框
print(df)

# 将修改后的数据框写入新的Excel文件
df.to_excel(excel_file_path, index=False)