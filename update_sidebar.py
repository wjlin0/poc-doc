import os
from urllib.parse import quote

# 指定要遍历的目录
directory_to_search = "./docs/"


def get_md_file_paths(directory):
    md_file_paths = []
    # 遍历指定目录及其子目录中的文件和文件夹
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件是否以 .md 结尾
            if file.endswith(".md"):
                # 构建文件的相对路径并添加到列表中
                md_file_paths.append([os.path.join(root, file).lstrip("./"), str(file).replace(".md", "")])
    return md_file_paths


def set_chi_sidebar(dir):
    md_files = get_md_file_paths(dir)
    shang = os.path.normpath(os.path.join(dir, '../'))
    if shang == 'docs':
        shang = '/'
        lines = [f"* [上一级]({shang})\n"]
    else:
        lines = [f"* [上一级]({shang}/)\n"]

    for md_file in md_files:
        if '_sidebar.md' in md_file[0]:
            continue
        if 'README.md' in md_file[0]:
            continue
        line = f"* [{md_file[1]}]({quote(md_file[0])})"
        lines.append(line + "\n")

    open(os.path.join(dir, "_sidebar.md"), "w").writelines(lines)


import os


def build_directory_structure(directory):
    structure = {}

    def add_md_files(current_dir, current_dict):
        has_md = False
        for root, dirs, files in os.walk(current_dir):
            # 检查当前目录及其子目录中是否存在 .md 文件
            if any(file.endswith('.md') for file in files):
                has_md = True
                break

        if has_md:
            for dir_name in os.listdir(current_dir):
                dir_path = os.path.join(current_dir, dir_name)
                if os.path.isdir(dir_path):
                    sub_dict = {}
                    if add_md_files(dir_path, sub_dict):
                        current_dict[dir_path] = sub_dict
            return True
        return False

    add_md_files(directory, structure)
    if directory not in structure:
        structure[directory] = {}

    return structure


# 使用示例


def for_key(fatherKey, structure):
    if structure == {}:
        set_chi_sidebar(fatherKey)
        return
    # 判断这个目录下有无 README.md 或者 存在README.md 但是文件内容为空
    if not os.path.exists(os.path.join(fatherKey, "README.md")):
        md_files = get_md_file_paths(fatherKey)
        shang = os.path.normpath(os.path.join(fatherKey, '../'))
        if shang == 'docs':
            shang = '/'
            lines = [f"* [上一级]({shang})\n"]
        else:
            lines = [f"* [上一级]({shang}/)\n"]
        lines.append(f"* [说明]({fatherKey})\n")
        for md_file in md_files:
            if '_sidebar' in md_file[0]:
                continue
            if 'README.md' in md_file[0]:
                continue
            line = f"* [{md_file[1]}]({quote(md_file[0])})"
            lines.append(line + "\n")

        open(os.path.join(fatherKey, "README.md"), "w").writelines(lines)
    elif os.path.getsize(os.path.join(fatherKey, "README.md")) == 0:
        md_files = get_md_file_paths(fatherKey)

        shang = os.path.normpath(os.path.join(fatherKey, '../'))
        if shang == 'docs':
            shang = '/'

        lines = [f"* [上一级]({shang})\n"]
        lines.append(f"* [说明]({fatherKey})\n")
        for md_file in md_files:
            if '_sidebar' in md_file[0]:
                continue
            line = f"* [{md_file[1]}]({quote(md_file[0])})"
            lines.append(line + "\n")

        open(os.path.join(fatherKey, "README.md"), "w").writelines(lines)

    shang = os.path.normpath(os.path.join(fatherKey, '../'))
    if shang == "docs":
        lines = "* [上一级](/)\n"
    else:
        lines = f"* [上一级]({shang}/)\n"
    lines += f"* [说明]({fatherKey})\n"
    for key in structure.keys():
        name = str(key).split("/")[-1]

        lines += f"* [{name}](/{os.path.normpath(key)}/)\n"

    with open(os.path.join(fatherKey, "_sidebar.md"), "w") as f:
        f.write(lines)

    for key in structure.keys():
        for_key(key, structure[key])


directory = './docs/wy876_poc'
structure = build_directory_structure(directory)

for key in structure.keys():
    for_key(key, structure[key])
