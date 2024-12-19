根据官方的[README.md](https://github.com/labelmeai/labelme)文件，用anaconda打开cmd指令框后依次执行以下指令：
```
conda create --name=labelme python=3
source activate labelme
pip install labelme
```
在执行第二条指令时可能会出现：
```
'source' 不是内部或外部命令，也不是可运行的程序
或批处理文件。
```
此时可改为执行
```
activate labelme
```
或
```
conda activate labelme
```
静待labelme安装完成后即可输入
```
labelme
```
来运行labelme了  

P.S.笔者在输入指令时跳过了第二条指令但仍然成功安装了
