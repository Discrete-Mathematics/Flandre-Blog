```python
import requests #引入request库

imgSrc="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" #目标网址（资源）
objPath="海报.jpg" #保存到硬盘上的文件名（包含后缀）

img=requests.get(imgSrc) #发出请求
with open(objPath,'ab') as f:
    f.write(img.content)
```
