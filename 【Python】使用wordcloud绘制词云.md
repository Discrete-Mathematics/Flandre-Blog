```python
from wordcloud import WordCloud,STOPWORDS
from PIL import Image
import numpy as np

#准备遮罩图片（蒙版图像、词云形状）
img=Image.open("images/苏轼.png")
img_array=np.array(img)

#设置字体
#font=r'C:\Windows\Fonts\simkai.ttf' #需要在你电脑上确认字体文件的存在
font=r'./fonts/AlibabaPuHuiTi-2-65-Medium.ttf'
#使用阿里巴巴普惠字体2.0，下载地址为https://www.alibabafonts.com/#/font

#准备停用词
stopwords=set(STOPWORDS)
stopwords.add("惟有")

wc=WordCloud(width=600,                #图片宽度（单位：像素）
             height=600,               #图片高度（单位：像素）
             background_color='white', #背景颜色
             max_font_size=80,         #词云最大字号
             min_font_size=16,         #词云最小字号
             font_path=font,           #中文分词必须有中文字体设置
             min_word_length=2,        #最小单词长度
             mask=img_array,           #设置遮罩图片；若没有该项则为默认设置
             stopwords=stopwords       #设置停用词
)

word_list=' '.join(res)
wc.generate_from_text(word_list) #绘制词云

#设置保存的png文件名
wc.to_file("output/wordcloud词云.png")
```
