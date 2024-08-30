from PIL import Image
import os
from tqdm import tqdm


def is_numbered(file_name):
    """检查文件是否已经编号"""
    if file_name.lower().endswith('.jpg'):
        return file_name[:-4].isdigit()
    elif file_name.lower().endswith('.jpeg'):
        return file_name[:-5].isdigit()
    elif file_name.lower().endswith('.png'):
        return file_name[:-4].isdigit()
    return False


def refile_name(dir_path):
    """批量修改文件夹的图片名"""
    files = os.listdir(dir_path)
    existing_numbers = set()

    # 找到现有编号
    for file_name in files:
        if is_numbered(file_name):
            existing_numbers.add(int(file_name[:-4]))

    # 为未编号的文件重新命名
    for idx, file_name in tqdm(enumerate(files), desc="Renaming Files", total=len(files)):
        if file_name.lower().endswith(('jpg', 'png', 'jpeg')) and not is_numbered(file_name):
            # 找到下一个可用的编号
            new_number = max(existing_numbers, default=0) + 1
            new_file_name = f"{new_number:02d}.jpg"
            existing_numbers.add(new_number)
            os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, new_file_name))


def resize_images(src_dir, dest_dir, size=(634, 1268)):
    """调整图片大小并保存到新目录"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    src_files = os.listdir(src_dir)
    dest_files = set(os.listdir(dest_dir))

    for file_name in tqdm(src_files, desc="Resizing Images"):
        if file_name.lower().endswith(('jpg', 'png', 'jpeg')) and file_name not in dest_files:
            file_path = os.path.join(src_dir, file_name)
            img = Image.open(file_path)
            img.thumbnail(size)
            img.save(os.path.join(dest_dir, file_name))
            make_markdown(file_name)


def make_markdown(img_name):
    """创建md文件"""
    content = """
    ---
    title: 
    caption: 
    ---
    """
    file_num = '00'
    if img_name.lower().endswith('.jpg'):
        file_num = img_name[:-4]
    elif img_name.lower().endswith('.jpeg'):
        file_num = img_name[:-5]
    elif img_name.lower().endswith('.png'):
        file_num = img_name[:-4]

    file_dir = '../../../_images/' + file_num + '.md'

    with open(file_dir, 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    current_dir = os.getcwd()  # 获取当前工作目录
    print("开始重命名文件...")
    refile_name(current_dir)
    print("文件重命名完成。")

    print("开始调整图片大小...")
    resize_images(current_dir, '../thumbs')
    print("图片调整完成。")
    input("按任意键退出...")  # 等待用户输入


if __name__ == "__main__":
    main()
