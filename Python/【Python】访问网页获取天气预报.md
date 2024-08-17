```python
import requests #引入request库，发起HTTP请求
key="4080fdf35495a31a75cab22449d0b5ac" #你的key值（接口访问编码）
city=input("请输入你要查询的城市：")

param={"city":city,"key":key}
url=f"http://apis.juhe.cn/simpleWeather/query"

response=request.get(url,params=para)
print(response.json())
```
