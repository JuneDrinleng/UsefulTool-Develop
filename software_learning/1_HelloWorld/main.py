from model import *

def main_gui():
    input_text = None  # 在全局作用域或类作用域定义变量
    root = tk.Tk() #创建主窗口对象root
    style = Style(theme='superhero')  # 设置主题为 'superhero'
    root.title('Translate Helper') #给主窗口添加标题

    #定义label的内容和字体
    text='请输入您需要翻译的内容：'
    front_style=(get_kai_font_name(), 10) #直接设置可能面临分辨率模糊的问题
    hello_label=tk.Label(root, text=text, font=front_style)
    # hello_label.pack() #将label添加到主窗口 
    #修改label布局：
    hello_label.place(x=20, y=20,anchor='nw')

    #输入框部分：
    input_box=InputBox(root)
    input_text=input_box.bind_enter()

    #定义输出框提示字体和内容
    text2='翻译结果：'
    front_style=(get_kai_font_name(), 10) #直接设置可能面临分辨率模糊的问题
    label2=Label(root, text=text2, font=front_style)
    label2.place(x=20, y=70,anchor='nw')    #修改布局

    # # 添加“始终置顶”按钮
    # always_on_top_button = tk.Button(root, text="始终置顶", command=lambda: toggle_always_on_top(root))
    # always_on_top_button.place(x=90, y=120, anchor='nw', width=120, height=30)
    always_on_top_var = tk.BooleanVar(value=False)
    always_on_top_checkbox =Checkbutton(
        root,
        text="始终置顶",
        variable=always_on_top_var,
        command=lambda: toggle_always_on_top(root, always_on_top_checkbox)
        # font=front_style
    )
    always_on_top_checkbox.place(x=90, y=120, anchor='nw', width=120, height=30)

    root.geometry('250x200') #设置窗口大小
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center') #居中显示
    root.mainloop()#主窗口循环展示



if __name__ == '__main__':
    main_gui()