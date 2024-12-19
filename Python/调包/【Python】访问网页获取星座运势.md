```python
#获取星座运势
import requests #引入request库，发起HTTP请求

key="6faa9a8321f88be58d604b8db5df8f46" #你的key值（接口访问编码）
consName=input("请输入星座名称（如：双鱼座）：")
type=input("请输入运势类型（today，tomorrow，week，month，year）：")

param={"key":key，"consName":consName,"type":type}
url=f"http://web.juhe.cn/constellation/getAll"

response=request.get(url,params=param) #请求网址

response=request.get(url,params=param) #发起请求
print(response.json()) #输出得到的数据
```
