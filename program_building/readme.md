这是一个项目构建程序
主要用于构建python的项目文件夹结构
只需要输入项目想要存储的路径和项目名称即可

目前项目结构如下
\file tree
- project_name
  - README.md(需写下完整的步骤)
  - .gitignore(由git自动生成)
  - data
    - orginal_data
    - preprocessed_data
    - processed_data
  - src
    - __init__.py （本该有，但是目前项目的复杂程度暂时不太需要）
    - data_preprocessing.py(数据预处理)
	- main.py
	- utils.py
    - display.ipynb
  - model
    - model_named_readme.md
  - log
    - log_readme.md
  - result
    - visualization_resualt(可视化结果，格式需包括jpg/png等压缩图，以及eps/svg等矢量图)
    - calculate_result
  - try(测试文件夹，用于存放尝试的代码)
    - try.ipynb

项目打包命令：
~~~
pyinstaller --onefile --name program_structV2 --icon=icon.ico program_struct.py
~~~