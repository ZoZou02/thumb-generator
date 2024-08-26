from PIL import Image
import os
import argparse

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
            new_file_name = file_name
            img.save(os.path.join(dest_dir, new_file_name))


def main():
    # parser = argparse.ArgumentParser(description="批量重命名和调整图片大小")
    # parser.add_argument("source_dir", help="源图片文件夹路径")
    # parser.add_argument("destination_dir", help="调整大小后的图片保存文件夹路径")

    # args = parser.parse_args()

    # refile_name(args.source_dir)
    current_dir = os.getcwd()  # 获取当前工作目录
    refile_name(current_dir)

    # resize_images(args.source_dir, args.destination_dir)
    resize_images(current_dir, 'thumb')


if __name__ == "__main__":
    main()
