import os
from urllib.parse import quote

# 指定要遍历的目录
directory_to_search = "./docs"


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


# 获取所有 .md 文件的相对路径
md_files = get_md_file_paths(directory_to_search)

lines = ["* [首页](/)\n"]
# 打印结果
for md_file in md_files:
    line = f"* [{md_file[1]}]({quote(md_file[0])})"
    lines.append(line+"\n")
open("_sidebar.md","w").writelines(lines)
