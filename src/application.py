import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class App:
    def __init__(self, name='defaultApp'):
        self.root = tk.Tk()
        self.root.title(name)
        self.root.geometry('400x300+500+500')
        self.root.resizable(False, False)

        self.import_data_path = tk.StringVar()
        self.output_data_path = tk.StringVar()
        self.model_type_enum = ('LearnModel', 'BinarizeBed', 'BinarizeBam')

        self.create_base()
        self.root.mainloop()

    def create_base(self):
        self.import_data_lb = tk.Label(self.root, text='输入文件路径：')
        self.import_data_lb.place(x=20, y=30)

        self.import_data_path_en = tk.Entry(self.root, textvariable=self.import_data_path, width=30)
        self.import_data_path_en.place(x=20,y=50)

        self.import_data_path_bt = tk.Button(self.root, text='浏览', height=1, command=self.cmd_open_source_dir)
        self.import_data_path_bt.place(x=230, y=45)

        self.import_model_type_lb = tk.Label(self.root, text='选择模型：')
        self.import_model_type_lb.place(x=20, y=90)

        self.import_model_type_cb = ttk.Combobox(self.root, values=self.model_type_enum)
        self.import_model_type_cb.current(0)
        self.import_model_type_cb.place(x=20, y=110)

        self.output_data_path_lb = tk.Label(self.root, text='选择输出文件夹：')
        self.output_data_path_lb.place(x=20, y=140)

        self.output_data_path_en = tk.Entry(self.root, textvariable=self.output_data_path,width=30)
        self.output_data_path_en.place(x=20, y=160)

        self.output_data_path_bt = tk.Button(self.root, text='浏览', height=1, command=self.cmd_open_target_dir)
        self.output_data_path_bt.place(x=230, y=155)

        self.start_bt = tk.Button(self.root, text='开始')
        self.start_bt.place(x=200, y=200)


    def cmd_open_source_dir(self):
        self.import_data_path = filedialog.askdirectory(title='选择数据输入文件夹', initialdir='./')
        self.import_data_path_en.delete(0, 'end')
        self.import_data_path_en.insert(0, self.import_data_path)

    def cmd_open_target_dir(self):
        self.output_data_path = filedialog.askdirectory(title='选择结果输出文件夹', initialdir='./')
        self.output_data_path_en.delete(0, 'end')
        self.output_data_path_en.insert(0, self.output_data_path)

