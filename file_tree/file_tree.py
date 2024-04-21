import os
import contextlib
import sys
def generate_file_tree(directory, prefix='', level=0):
    """Generate a textual representation of the file tree rooted at `directory`."""
    entries = os.listdir(directory)


    for entry in entries:
        full_path = os.path.join(directory, entry)
        relative_path = prefix + '/' + entry if prefix else entry


        if os.path.isdir(full_path):
            if level==0:
                print(f"{'└'}{'    ' * level}── {entry}")
            else:
                print(f"{' '}{'    ' * level}└──{entry}")
            generate_file_tree(full_path, prefix=relative_path, level=level + 1)
        else:

            # print(f"{prefix}{'    ' * level}└── {entry}")
            if level==0:
                print(f"{'└'}{'    ' * level}── {entry}")
            else:
                print(f"{' '}{'    ' * level}└── {entry}")

def main():
    print("该程序用于生成文件树")
    directory = input("请输入文件夹路径：")
    if '"' in directory:
        directory=directory.replace('"','')
    elif "'" in directory:
        directory=directory.replace("'","")
    else:
        pass
    txt_file_path = os.path.join(directory, 'file_tree.txt')
    with open(txt_file_path, 'w',encoding='utf-8') as output_file:
        with contextlib.redirect_stdout(output_file):
            generate_file_tree(directory=directory)
    print(f"文件树已生成并保存到 {txt_file_path}")
    # generate_file_tree(directory=directory)
if __name__ == '__main__':
    main()
    print("按任意键退出")
    sys.stdin.read(1)
