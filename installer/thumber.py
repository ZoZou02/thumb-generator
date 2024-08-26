from PIL import Image
import os

def refile_name(dir_path):
    """批量修改文件夹中的图片文件名"""
    files = [f for f in os.listdir(dir_path) if f.lower().endswith(('jpg', 'png', 'jpeg'))]
    files.sort()  # 对图片文件进行排序
    for idx, file_name in enumerate(files):
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
            new_file_name = file_name
            img.save(os.path.join(dest_dir, new_file_name))


def main():
    current_dir = os.getcwd()  # 获取当前工作目录
    refile_name(current_dir)
    resize_images(current_dir, 'thumb')


if __name__ == "__main__":
    main()
