import os  
import shutil  

# 定义源文件夹和目标文件夹路径，替换为自己的路径  
source_dir ="D:\\防疲劳\\SLPT-master-main\\output114514"
target_dir = "D:\\防疲劳\\SLPT-master-main\\output114514\\labels"

def move_jpg_files():  
    # 检查源文件夹是否存在  
    if not os.path.exists(source_dir):  
        print(f"源文件夹 {source_dir} 不存在。")  
        return  

    # 检查目标文件夹是否存在，如果不存在则创建  
    if not os.path.exists(target_dir):  
        os.makedirs(target_dir)  
        print(f"创建目标文件夹 {target_dir}.")  

    # 统计移动的文件数量  
    moved_count = 0  

    # 遍历源文件夹中的所有文件  
    for filename in os.listdir(source_dir):  
        # 提取文件扩展名并转换为小写  
        if os.path.isfile(os.path.join(source_dir, filename)):  
            file_ext = os.path.splitext(filename)[1].lower()  
            if file_ext == '.jpg':#设置要移动的文件的后缀
                # 检查目标文件夹中是否已存在同名文件  
                target_file = os.path.join(target_dir, filename)  
                if os.path.exists(target_file):  
                    print(f"文件 {filename} 已经存在于目标文件夹，跳过。")  
                    continue  

                try:  
                    # 移动文件  
                    shutil.move(os.path.join(source_dir, filename), target_dir)  
                    moved_count += 1  
                    print(f"成功移动 {filename} 到 {target_dir}")  
                except Exception as e:  
                    print(f"移动 {filename} 时发生错误：{str(e)}")  

    print(f"已移动 {moved_count} 个 JPG 文件。")  

if __name__ == "__main__":  
    move_jpg_files()
