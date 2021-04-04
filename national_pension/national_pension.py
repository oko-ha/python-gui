import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("국민 연금 계산기")

def calc(a, b, c, d, j):
    e = c * d * 12
    f = 11 * e / 1656
    g = b + f
    h = e / f / 12
    i = a + c + h
    k = g * j * 0.072
    l = g + k
    m = (g * 12 * 5)/(k * 12)
    n = 68 + m

    txt_e.configure(state='normal')
    txt_f.configure(state='normal')
    txt_g.configure(state='normal')
    txt_h.configure(state='normal')
    txt_i.configure(state='normal')
    txt_k.configure(state='normal')
    txt_l.configure(state='normal')
    txt_m.configure(state='normal')
    txt_n.configure(state='normal')
    txt_e.delete(0,"end")
    txt_f.delete(0,"end")
    txt_g.delete(0,"end")
    txt_h.delete(0,"end")
    txt_i.delete(0,"end")
    txt_k.delete(0,"end")
    txt_l.delete(0,"end")
    txt_m.delete(0,"end")
    txt_n.delete(0,"end")
    txt_e.insert(0, str(round(e)))
    txt_f.insert(0, str(round(f)))
    txt_g.insert(0, str(round(g)))
    txt_h.insert(0, str(round(h)))
    txt_i.insert(0, str(round(i)))
    txt_k.insert(0, str(round(k)))
    txt_l.insert(0, str(round(l)))
    txt_m.insert(0, str(round(m)))
    txt_n.insert(0, str(round(n)))
    txt_e.configure(state='readonly')
    txt_f.configure(state='readonly')
    txt_g.configure(state='readonly')
    txt_h.configure(state='readonly')
    txt_i.configure(state='readonly')
    txt_k.configure(state='readonly')
    txt_l.configure(state='readonly')
    txt_m.configure(state='readonly')
    txt_n.configure(state='readonly')

def start():
    try:
        a = int(txt_a.get())
        b = int(txt_b.get())
        c = int(txt_c.get())
        d = int(txt_d.get())
        j = int(txt_j.get())
        if a < 60 or a > 63:
            msgbox.showerror("Error", "60~63세 사이 나이를 입력하세요")
        elif c > 4 or c < 0:
            msgbox.showerror("Error", "추가 납입 기간을 다시 입력하세요")
        elif d > 46 or d < 0:
            msgbox.showerror("Error", "추가 납부 금액을 다시 입력하세요.")
        elif j > 5 or j < 0:
            msgbox.showerror("Error", "수령 연기 기간을 다시 입력하세요.")
        else:
            calc(a, b, c, d, j) 
    except:
        msgbox.showerror("Error", "숫자를 입력하세요.")

    
    

# 추가납부 프레임
frame_add = LabelFrame(root, text="국민연금 추가납부 경우")
frame_add.pack(side="left", padx=5, pady=5, ipady=5)

frame_a = LabelFrame(frame_add)
frame_a.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_a_1 = Label(frame_a, text="나의 나이 입력")
lbl_a_1.pack(side="left", padx=5, pady=5)

lbl_a_2 = Label(frame_a, text="   세")
lbl_a_2.pack(side="right", padx=5, pady=5)

txt_a = Entry(frame_a, bg = 'light blue', width=10)
txt_a.pack(side="right", padx=5, ipady=4)

frame_b = LabelFrame(frame_add)
frame_b.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_b_1 = Label(frame_b, text="나의 수령 연금액 입력 (a)")
lbl_b_1.pack(side="left", padx=5, pady=5)

lbl_b_2 = Label(frame_b, text="만원")
lbl_b_2.pack(side="right", padx=5, pady=5)

txt_b = Entry(frame_b, bg = 'light blue', width=10)
txt_b.pack(side="right", padx=5, ipady=4)

frame_c = LabelFrame(frame_add)
frame_c.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_c_1 = Label(frame_c, text="추가 납입기간을 입력")
lbl_c_1.pack(side="left", padx=5, pady=5)

lbl_c_2 = Label(frame_c, text="   년")
lbl_c_2.pack(side="right", padx=5, pady=5)

txt_c = Entry(frame_c, bg = 'light blue', width=10)
txt_c.pack(side="right", padx=5, ipady=4)

frame_d = LabelFrame(frame_add)
frame_d.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_d_1 = Label(frame_d, text="매월 추가납부 금액 입력")
lbl_d_1.pack(side="left", padx=5, pady=5)

lbl_d_2 = Label(frame_d, text="만원")
lbl_d_2.pack(side="right", padx=5, pady=5)

txt_d = Entry(frame_d, bg = 'light blue', width=10)
txt_d.pack(side="right", padx=5, ipady=4)

frame_e = LabelFrame(frame_add)
frame_e.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_e_1 = Label(frame_e, text="추가 납부 금액")
lbl_e_1.pack(side="left", padx=5, pady=5)

lbl_e_2 = Label(frame_e, text="만원")
lbl_e_2.pack(side="right", padx=5, pady=5)

txt_e = Entry(frame_e, width=10)
txt_e.configure(state='disabled')
txt_e.pack(side="right", padx=5, ipady=4)

frame_f = LabelFrame(frame_add)
frame_f.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_f_1 = Label(frame_f, text="추가 연금 수령액 (b)")
lbl_f_1.pack(side="left", padx=5, pady=5)

lbl_f_2 = Label(frame_f, text="만원")
lbl_f_2.pack(side="right", padx=5, pady=5)

txt_f = Entry(frame_f, width=10)
txt_f.configure(state='disabled')
txt_f.pack(side="right", padx=5, ipady=4)

frame_g = LabelFrame(frame_add)
frame_g.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_g_1 = Label(frame_g, text="나의 연금액 (a + b)")
lbl_g_1.pack(side="left", padx=5, pady=5)

lbl_g_2 = Label(frame_g, text="만원")
lbl_g_2.pack(side="right", padx=5, pady=5)

txt_g = Entry(frame_g, width=10)
txt_g.configure(state='disabled')
txt_g.pack(side="right", padx=5, ipady=4)

frame_h = LabelFrame(frame_add)
frame_h.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_h_1 = Label(frame_h, text="추가 납부의 손익 분기점")
lbl_h_1.pack(side="left", padx=5, pady=5)

lbl_h_2 = Label(frame_h, text="   년")
lbl_h_2.pack(side="right", padx=5, pady=5)

txt_h = Entry(frame_h, width=10)
txt_h.configure(state='disabled')
txt_h.pack(side="right", padx=5, ipady=4)

frame_i = LabelFrame(frame_add)
frame_i.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_i_1 = Label(frame_i, text="추가 납부의 손익 분기점")
lbl_i_1.pack(side="left", padx=5, pady=5)

lbl_i_2 = Label(frame_i, text="   세")
lbl_i_2.pack(side="right", padx=5, pady=5)

txt_i = Entry(frame_i, width=10)
txt_i.configure(state='disabled')
txt_i.pack(side="right", padx=5, ipady=4)


# 수령연기 프레임
frame_delay = LabelFrame(root, text="국민연금 수령연기 경우")
frame_delay.pack(padx=5, pady=5, ipady=5)

frame_j = LabelFrame(frame_delay)
frame_j.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_j_1 = Label(frame_j, text="수령 연기 기간 입력")
lbl_j_1.pack(side="left", padx=5, pady=5)

lbl_j_2 = Label(frame_j, text="   년")
lbl_j_2.pack(side="right", padx=5, pady=5)

txt_j = Entry(frame_j, bg = 'light blue', width=10)
txt_j.pack(side="right", padx=5, ipady=4)

frame_k = LabelFrame(frame_delay)
frame_k.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_k_1 = Label(frame_k, text="추가 연금 수령액")
lbl_k_1.pack(side="left", padx=5, pady=5)

lbl_k_2 = Label(frame_k, text="만원")
lbl_k_2.pack(side="right", padx=5, pady=5)

txt_k = Entry(frame_k, width=10)
txt_k.configure(state='disabled')
txt_k.pack(side="right", padx=5, ipady=4)

frame_l = LabelFrame(frame_delay)
frame_l.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_l_1 = Label(frame_l, text="나의 연금액")
lbl_l_1.pack(side="left", padx=5, pady=5)

lbl_l_2 = Label(frame_l, text="만원")
lbl_l_2.pack(side="right", padx=5, pady=5)

txt_l = Entry(frame_l, width=10)
txt_l.configure(state='disabled')
txt_l.pack(side="right", padx=5, ipady=4)

frame_m = LabelFrame(frame_delay)
frame_m.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_m_1 = Label(frame_m, text="수령 연금의 손익분기점")
lbl_m_1.pack(side="left", padx=5, pady=5)

lbl_m_2 = Label(frame_m, text="   년")
lbl_m_2.pack(side="right", padx=5, pady=5)

txt_m = Entry(frame_m, width=10)
txt_m.configure(state='disabled')
txt_m.pack(side="right", padx=5, ipady=4)

frame_n = LabelFrame(frame_delay)
frame_n.pack(padx=5, pady=5, ipady=5, fill="both")

lbl_n_1 = Label(frame_n, text="수령 연금의 손익 분기점")
lbl_n_1.pack(side="left", padx=5, pady=5)

lbl_n_2 = Label(frame_n, text="   세")
lbl_n_2.pack(side="right", padx=5, pady=5)

txt_n = Entry(frame_n, width=10)
txt_n.configure(state='disabled')
txt_n.pack(side="right", padx=5, ipady=4)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(side="bottom", fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="년금 계산", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()