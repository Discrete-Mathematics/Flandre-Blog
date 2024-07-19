```python
import requests

url='https://www.baidu.com'

headers={"User-Agent":"Mozilla/5.0(windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML,Line Gecko)"
                      "Chrome/54.0.2840.99 Safari/537.36"}

response=requests.get(url,headers=headers)
print(response.txt)
```
