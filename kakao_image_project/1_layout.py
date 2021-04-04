import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Kakao image project")

# image load frame
load_frame = Frame(root)
load_frame.pack(fill="x", padx=5, pady=5)

btn_add_image = Button(load_frame, padx=5, pady= 5, width=12, text="이미지 가져오기")
btn_add_image.pack(side="left")

# image name frame
name_frame = LabelFrame(root, text="현재 이미지")
name_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_name = Entry(name_frame)
txt_name.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

# image view

# save path frame
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

# option frame
option_frame = Frame(root)
option_frame.pack(fill="x", padx=5, pady=5)

btn_previous = Button(option_frame, padx=5, pady= 5, width=12, text="<")
btn_previous.pack(side="left")

btn_delete = Button(option_frame, padx=5, pady= 5, width=12, text="삭제")
btn_delete.pack(side="left")

btn_filter = Button(option_frame, padx=5, pady= 5, width=12, text="필터")
btn_filter.pack(side="left")

btn_next = Button(option_frame, padx=5, pady= 5, width=12, text=">")
btn_next.pack(side="left")

root.resizable(False, False)
root.mainloop()