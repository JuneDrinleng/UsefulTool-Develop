import os

# 获取当前脚本所在文件的绝对路径
current_script_path = os.path.abspath(__file__)

# 提取脚本所在文件夹路径
script_dir_path = os.path.dirname(current_script_path)
res=os.path.join(script_dir_path, 'ressource')
print(res)