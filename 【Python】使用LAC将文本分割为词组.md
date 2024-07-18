```python
from LAC import LAC
data="我爱北京天安门"
lac=LAC(mode='seg')
res=lac.run("".join(data))
cut_content=' '.join(res)
print(cut_content)
```
