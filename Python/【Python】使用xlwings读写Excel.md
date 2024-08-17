```python
import xlwings as xw #引入库

app=xw.App(visible=False,add_book=False) #打开Excel程序，默认为程序可见
wb=app.books.open('data/苏轼的诗词（3460首）.xlsx') #打开已存在的Excel
sheet=wb.sheets[0] #通过序号获取表单对象
data=sheet.range('c2').expand('down').value #一维列表保存全部诗词
print(data)
wb.close() #退出工作簿（可省略）
app.quit() #退出Excel
```
