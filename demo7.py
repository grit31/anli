from PIL import Image
import os

# 定义源文件夹和目标文件夹
source_dir = r'D:\anli\厨房真实\厨房真实'  # 源文件夹的路径
target_dir = r'D:\anli\厨房真实512'  # 目标文件夹的路径

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 遍历源文件夹
for file_name in os.listdir(source_dir):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        # 读取图片
        file_path = os.path.join(source_dir, file_name)
        image = Image.open(file_path)
        if image.mode != 'RGB':
            continue  # 只处理彩色图片

        # 调整图片大小
        image = image.resize((512, 512), Image.ANTIALIAS)

        # 保存到目标文件夹
        target_path = os.path.join(target_dir, file_name)
        image.save(target_path)

print("所有图片处理完毕，并保存到了新的文件夹。")
