from PIL import Image
import os


def refile_name(dir_path):
    """批量修改文件夹的图片名"""
    files = os.listdir(dir_path)
    for idx, file_name in enumerate(files):
        if file_name.lower().endswith(('jpg', 'png', 'jpeg')):
            new_file_name = f"{idx + 1:02d}.jpg"
            os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, new_file_name))


def resize_images(src_dir, dest_dir, size=(400, 200)):
    """调整图片大小并保存到新目录"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for file_name in os.listdir(src_dir):
        if file_name.lower().endswith(('jpg', 'png', 'jpeg')):
            file_path = os.path.join(src_dir, file_name)
            img = Image.open(file_path)
            img.thumbnail(size)
            # new_file_name = file_name[5:]
            img.save(os.path.join(dest_dir, file_name))


# 执行操作
source_dir = "test"
destination_dir = "test_thumb"

refile_name(source_dir)
resize_images(source_dir, destination_dir)
