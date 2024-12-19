```Python
from pathlib import Path
import xlwings as xw

src_folder=Path('./月销售统计/')
file_list=list(src_folder.glob('*.xlsx))
app=xw.App(visible=False,add_book=False)
sheet_name='产品销售统计'
header=None
all_data=[]
for i in file_list:
  if i.name.startswith('~$'): #跳过临时文件
    continue
  workbook=app.book.open(i)
  for j in workbook.sheets: #获取每个表格
    if j.name==sheet_name:
      if header is None: #如果表头为空
        header=j['A1:I1'].value #将第一行作为表头
      data=j['A2'].expand('table').value #从A2开始的剩余数值赋给data
      all_data=all_data+data #将所有表格合并为1个表格
  workbook.close()
new_workbook=xw.Book()
new_worksheet=new_workbook.sheets.add(sheet_name)
new_worksheet['A1'].value=header
new_worksheet['A2'].value=all_data
new_worksheet.autofit() #根据数据内容自动调整行宽和列高
new_workbook.save(src_folder/'上半年产品销售统计表.xlsx')
new_workbook.close()
app.quit()
```
