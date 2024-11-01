# UsefulTool Develop
 这是一个自己开发的暂时有一些用的小工具的仓库，由于作者不太会编写图形化界面，所以程序比较丑陋

## 目录

1. [Translation文件夹](./Translation)存放Translate Helper GUI开发代码
2. [file_tree文件夹](./file_tree)存放文件树生成程序（非GUI）的开发代码
3. [program_building文件夹](./program_building) 存放用于自动生成python的项目架构的开发代码

## 2024.11.1 更新

- 更新了program_building项目，将原先的项目结构进行调整，通过实践发现同时维护data的readme和src的readme以及总的readme是不现实且繁琐的，所以将data的readme和src的readme部分集成到了总的src的部分
- 原先项目的文件路径都放在import的下方、if **name**='**main**'外，这会导致运行时的bug，所以现在将data路径以及output路径等内容都放在了if **name**='**main**'内部
- **发布program_building_v3.0**

## 2024.8.15 更新

- 添加完善了program_building项目创建工具，使得其中的readme索引使用typora可以正确跳转

- ps.利用program_building项目创建工具，只需要输入项目名称和项目在本地的绝对路径，就可以创建包含data，try，src，results等文件夹的结构的项目，同时已经写好了基本的main.py文件格式以及readme的基本内容
