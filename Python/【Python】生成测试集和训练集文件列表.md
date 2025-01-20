```python
import os
import random
 
# 设置要扫描的目录
directory = 'your_path'  # 请替换为你的目录路径
 
# 获取文件列表
image_files = [f
               for f in os.listdir(directory)
               if f.endswith(('.jpg', '.jpeg', '.png'))]  # 根据实际需要更改文件类型
 
# 随机打乱文件列表
random.shuffle(image_files)
 
# 划分比例
train_size = int(0.7 * len(image_files))
train_files = image_files[:train_size]
test_files = image_files[train_size:]
 
# 写入 train_list.txt
with open('train_list1.txt', 'w') as train_file:
    for item in train_files:
        train_file.write(f"{item}\n")
 
# 写入 test_list.txt
with open('test_list1.txt', 'w') as test_file:
    for item in test_files:
        test_file.write(f"{item}\n")
 
print("train_list.txt 和 test_list.txt 已生成。")
```
