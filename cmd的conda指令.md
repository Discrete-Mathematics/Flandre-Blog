以Python3.9为例：  
1.查看已创建的虚拟环境：  
```
conda-env list
```
2.conda建虚拟环境有两种命令，一种是直接创建，一种是指定路径创建，其中直接创建比较方便。    
①直接创建虚拟环境，默认路径为D:/data111/envs/（虚拟环境的名字）：  
```
conda create -n （虚拟环境的名字） python=3.9
```
②指定路径创建虚拟环境：
```
conda create --p=D:/data111/envs/（虚拟环境的名字） python=3.9
```
③列出conda有哪些虚拟环境：  
```
conda env list
```
④进入虚拟环境：
```
conda activate （虚拟环境的名字）
```
或者
```
conda activate D:/data111/envs/（虚拟环境的名字）
```
⑤退出虚拟环境：  
```
conda deactivate
```
⑥删除虚拟环境：
```
conda remove -n （虚拟环境的名字） -all
```
⑦本地已有一个环境AAA，克隆一个与之相同的BBB：
```
conda create -n BBB --clone AAA
```
3.查看当前激活的虚拟环境所安装的包：
```
conda list
```
