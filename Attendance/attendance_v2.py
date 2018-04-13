import tkinter
from tkinter import ttk
from PIL import ImageTk, Image, ImageFilter
from tkinter import messagebox
from tkinter import tix
import random
import threading
import time
from Data import teachers


class Login:
    def __init__(self):
        path = 'Source/unnamed.jpg'
        image_old = Image.open(path)
        #image_old = image_old.filter(ImageFilter.BLUR)
        image = image_old.resize((app.winfo_screenwidth(), app.winfo_screenheight()), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self.t = ttk.Label(app, image=image).grid(rowspan=10, columnspan=10)
        self.image = image

    def rem(self, e, widget):
        widget.delete(0, tkinter.END)

    def f_pas(self, e):
        text = self.pas['text']
        if text == 'Show':
            self.e_pass.configure(show='')
            self.pas.configure(text='Hide')
        else:
            self.e_pass.configure(show='\u2022')
            self.pas.configure(text='Show')

    def enter_con(self, e, widget):
        widget.configure(foreground='red')
        if widget['text'] == 'Forgot Password':
            widget.configure(font=('', 9, 'normal', 'roman', 'underline'))

    def leave_con(self, e, widget):
        widget.configure(foreground='black')
        if widget['text'] == 'Forgot Password':
            widget.configure(font=('', 9, 'normal', 'roman'))

    def log_check(self, f1):
        data = teachers.log()
        hod = 0

        if not data == []:
            for _ in data:
                if self.e_user.get() == _[0]:
                    hod = _[0]
                    if self.e_pass.get() == _[1]:
                        flag_log = 2
                        break
                    else:
                        flag_log = 1
                        break
                else:
                    flag_log = 0

            if flag_log is 2:
                f1.destroy()
                m = messagebox.showinfo('Success', 'Logged in successfully !!!')
                if m:
                    self.a = Attend(hod)

            elif flag_log is 1:
                    messagebox.showwarning('Warning', 'Incorrect Password !!!')
            else:
                messagebox.showwarning('Warning', 'Incorrect User Name !!!')
        else:
            if self.e_user.get() == 'Shubham':
                if self.e_pass.get() == 'Error':
                    pass
                else:
                    messagebox.showerror('Error', 'Wrong Administrator Password !!!')
            else:
                messagebox.showerror('Error', 'Wrong Administrator Name !!!')

    def log(self, n1=None):
        try:
            self.a.n1.destroy()
        except:
            pass

        f1 = ttk.Labelframe(app, text='Login', style='TLabelframe')
        f1.grid(row=2, column=3, ipadx=50, rowspan=5, columnspan=4)

        ttk.Label(f1, text='User Name', font=('times', 20)).pack(pady=10)
        self.e_user = ttk.Entry(f1, width=25, font=('times', 20))
        self.e_user.pack(pady=10)
        self.e_user.bind('<Button-1>', lambda e, widget=self.e_user: self.rem(e, widget))

        ttk.Label(f1, text='Password', font=('times', 20)).pack(pady=10)
        self.e_pass = ttk.Entry(f1, width=25, font=('times', 20), show='\u2022')
        self.e_pass.pack(pady=10)
        self.e_pass.bind('<Button-1>', lambda e, widget=self.e_pass: self.rem(e, widget))

        self.pas = ttk.Label(f1, cursor='hand2')
        self.pas.configure(text='Show')
        self.pas.bind('<Button-1>', self.f_pas)
        self.pas.bind('<Enter>', lambda e, widget=self.pas: self.enter_con(e, widget))
        self.pas.bind('<Leave>', lambda e, widget=self.pas: self.leave_con(e, widget))
        self.pas.pack(anchor='e', padx=50)

        forgot = tkinter.Label(f1, text='Forgot Password', font=('', 9, 'normal', 'roman'), cursor='hand2')
        forgot.bind('<Enter>', lambda e, widget=forgot: self.enter_con(e, widget))
        forgot.bind('<Leave>', lambda e, widget=forgot: self.leave_con(e, widget))
        forgot.pack()

        ttk.Button(f1, text='Submit', cursor='hand2', command=lambda: self.log_check(f1)).pack(pady=10)


class Attend:
    def __init__(self, user):
        self.user = user
        self.n1 = ttk.Notebook(app, width=1200, height=600)
        self.f1 = ttk.Frame(self.n1)
        self.n1.add(self.f1, text='          Daily Record          ')
        self.f2 = ttk.Frame(self.n1)
        self.n1.add(self.f2, text='          Monthly Record          ')
        self.f3 = ttk.Frame(self.n1)
        self.n1.add(self.f3, text='          Settings          ')
        self.n1.grid(row=2, column=3)

        threading.Thread(target=self.daily_rec).start()
        threading.Thread(target=self.mon_rec).start()
        threading.Thread(target=self.settings).start()

        #state_1.Attend2(self.f1)

    def daily_rec(self):

        def cal(c):

            import sys
            import calendar

            root = tkinter.Toplevel()
            root.title('Ttk Calendar')
            root.grab_set()
            w = c.winfo_reqheight()
            h = c.winfo_reqheight()
            print(w, h)
            root.geometry('+%d+%d' % (w, h))

            tkinter.Label(root, text='NEW').pack()

            root.mainloop()

        def check():
            for e, i in enumerate(v1):
                if i.get() == 1:
                    for j in v2[e]:
                        j.set(1)
                else:
                    for j in v2[e]:
                        j.set(0)

        def cur_enter(ev, t1, t2, t3, t4):
            t1.config(fg='red')
            t2.config(fg='red')
            t4.config(fg='red')
            t3.config(foreground='red')

        def cur_leave(ev, t1, t2, t3, t4):
            t1.config(fg='black')
            t2.config(fg='black')
            t4.config(fg='black')
            t3.config(foreground='black')

        def log_out():
            m = messagebox.askyesno('Alert', 'Do you want to Log Out ?')
            if m:
                l.log(self.n1)

        frame = tkinter.Frame(self.f1)
        frame.pack(pady=20, fill='x', expand=True)

        back = ttk.Button(frame, text='<- Log Out', command=log_out)
        back.grid(padx=20)
        f = ttk.Frame(frame)
        f.grid(row=0, column=1, padx=400)
        ttk.Label(f, text='Date : ', font=(14)).grid(row=0, column=0)
        e = ttk.Entry(f, font=(14), width=9)
        e.grid(row=0, column=1)
        e.insert(0, time.strftime('%d/%m/%Y'))
        #e.config(state='disable')
        '''c = ttk.Button(f, text='Calender')
        c.config(command=lambda c=c: cal(c))
        c.grid(row=0, column=2, padx=5)'''
        submit = ttk.Button(f, text="Submit ->")
        submit.grid(row=0, column=3, padx=435)

        data = teachers.lec()
        if data is []:
            for _ in data:
                if _[0] == self.user:
                    c = _[1].split(',')
                    c.sort()
                    break
                else:
                    pass
        else:
            c = ["CSE", "ECE", "ELECTRICAL", "CIVIL", "MECHANICAL"]
            c.sort()

        n2 = ttk.Notebook(self.f1, width=1200, height=600)
        n2.pack(fill='both', expand=True)
        v1 = []
        v2 = []

        for i in range(0, len(c)):
            f = ttk.Frame(n2)
            n2.add(f, text='   '+c[i]+'   ')

            canvas1 = tkinter.Canvas(f)
            scrolly = tix.Scrollbar(f, command=canvas1.yview, orient='vertical')

            canvas1.pack(side='left', fill='both', expand=True)
            scrolly.pack(side='right', fill='y')

            f2 = tkinter.Frame(canvas1, width=1100, height=550)

            ttk.Label(f2, text='S.No.', font=('times', 14)).grid(row=0, column=0, padx=80, pady=20)
            ttk.Label(f2, text='Roll No.', font=('times', 14)).grid(row=0, column=1, padx=80, pady=20)
            ttk.Label(f2, text='Name', font=('times', 14)).grid(row=0, column=2, padx=80, pady=20)
            ttk.Label(f2, text='Total Attended', font=('times', 14)).grid(row=0, column=4, padx=80, pady=20)

            '''e = tix.Entry(f2)
            e.insert(0, '01/01/2018')
            e.grid(row=0, column=3, padx=80, pady=20)'''

            v11 = tkinter.Variable()
            v11.set(0)
            v1.append(v11)
            v21 = []
            v2.append(v21)

            for j in range(0, 50):
                v21.append(tkinter.Variable())
                v21[j].set(0)
                t1 = tkinter.Label(f2, text=j+1, font=('helvatica', 12))
                t1.grid(row=j+3, column=0, padx=20)
                t2 = tkinter.Label(f2, text='181'+str(j), font=('helvatica', 12))
                t2.grid(row=j+3, column=1, padx=70)
                t3 = ttk.Label(f2, text='Student-'+str(j+1), font=('helvatica', 12), wraplength=100)
                t3.grid(row=j+3, column=2, columnspan=2, padx=70)
                t4 = tkinter.Label(f2, text=str(random.randrange(10))+'/10', font=('helvatica', 12))
                t4.grid(row=j+3, column=4)
                t5 = tix.Checkbutton(f2, onvalue=1, offvalue=0, variable=v21[j], font=('helvatica', 20))
                t5.grid(row=j+3, column=5, padx=70)
                t1.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_enter(ev, t1, t2, t3, t4))
                t2.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_enter(ev, t1, t2, t3, t4))
                t3.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_enter(ev, t1, t2, t3, t4))
                t4.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_enter(ev, t1, t2, t3, t4))
                t5.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_enter(ev, t1, t2, t3, t4))
                t1.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_leave(ev, t1, t2, t3, t4))
                t2.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_leave(ev, t1, t2, t3, t4))
                t3.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_leave(ev, t1, t2, t3, t4))
                t4.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_leave(ev, t1, t2, t3, t4))
                t5.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4: cur_leave(ev, t1, t2, t3, t4))

            '''for k in range(3, 200):
                tix.Label(f2, text=k).grid(row=1, column=k)'''

            tix.Checkbutton(f2, text='All', onvalue=1, offvalue=0, variable=v11, command=check).grid(row=0, column=5)
            canvas1.create_window(0, 0, window=f2)

            f2.update_idletasks()
            canvas1.itemconfigure("frame")

            canvas1.config(scrollregion=canvas1.bbox("all"))
            canvas1.config(yscrollcommand=scrolly.set)

    def mon_rec(self):
        def bind_x(*args):
            f.update_idletasks()
            canvas1.xview(*args)
            canvas2.xview(*args)

        def OnMouseWheel(event):
            canvas2.yview_scroll(int(-1*(event.delta/120)), "units")
            return "break"

        def cur_enter(ev, t1, t2, t3, t4, t5):
            t1.config(fg='red')
            t2.config(fg='red')
            t3.config(foreground='red')
            t4.config(fg='red')
            for i in range(len(t5)):
                t5[i].config(fg='red')

        def cur_leave(ev, t1, t2, t3, t4, t5):
            t1.config(fg='black')
            t2.config(fg='black')
            t3.config(foreground='black')
            t4.config(fg='black')
            for i in range(len(t5)):
                t5[i].config(fg='black')

        data = teachers.lec()
        if data is []:
            for _ in data:
                if _[0] == self.user:
                    c = _[1].split(',')
                    c.sort()
                    break
                else:
                    pass
        else:
            c = ["CSE", "ECE", "ELECTRICAL", "CIVIL", "MECHANICAL"]
            c.sort()

        n2 = ttk.Notebook(self.f2)
        n2.pack(fill='both', expand=True)

        for i in range(0, len(c)):
            f = ttk.Frame(n2, width=1150, height=10)
            n2.add(f, text='   '+c[i]+'   ')

            frame1 = ttk.Frame(f)
            frame1.pack(side='top', fill='x')

            frame2 = ttk.Frame(f)
            frame2.pack(fill='both', expand=True)

            canvas1 = tkinter.Canvas(frame1, height=40)
            canvas2 = tkinter.Canvas(frame2)
            scrolly = tix.Scrollbar(frame2, command=canvas2.yview, orient='vertical')
            scrollx = tix.Scrollbar(f, command=bind_x, orient='horizontal')

            scrolly.pack(side='right', fill='y')
            scrollx.pack(side='bottom', fill='x')
            canvas1.pack(side='top', fill='x', expand=True)
            canvas2.pack(side='left', fill='both', expand=True)
            f.bind_all("<MouseWheel>", OnMouseWheel)

            f1 = tkinter.Frame(canvas1)
            f2 = tkinter.Frame(canvas2)

            ttk.Label(f1, text='S.No.', font=('times', 14)).grid(row=0, column=0, padx=30)
            ttk.Label(f1, text='Roll No.', font=('times', 14)).grid(row=0, column=1, padx=33)
            ttk.Label(f1, text='Name', font=('times', 14)).grid(row=0, column=2, padx=54)

            for j in range(0, 10):
                ttk.Label(f1, text=j+1, font=('times', 14)).grid(row=0, column=4+j, padx=4)

            for j in range(10, 30):
                ttk.Label(f1, text=j+1, font=('times', 14)).grid(row=0, column=4+j, padx=1)

            ttk.Label(f1, text='Total', font=('times', 14)).grid(row=0, column=j+5, padx=10)

            '''e = tix.Entry(f2)
            e.insert(0, '01/01/2018')
            e.grid(row=0, column=3, padx=80, pady=20)'''

            for j in range(0, 50):
                t1 = tkinter.Label(f2, text=j+1, font=('helvatica', 12))
                t1.grid(row=j+3, column=0, padx=40)
                t2 = tkinter.Label(f2, text='181'+str(j), font=('helvatica', 12))
                t2.grid(row=j+3, column=1, padx=40)
                t3 = ttk.Label(f2, text='Student-'+str(j+1), font=('helvatica', 12), wraplength=100)
                t3.grid(row=j+3, column=2, columnspan=2, padx=40)
                t4 = tkinter.Label(f2, text='    '+str(random.randrange(10))+'/10    ', font=('helvatica', 12))
                t4.grid(row=j+3, column=35)

                t5 = []

                for k in range(0, 10):
                    t = tkinter.Label(f2, text=str(random.choice(['A', 'P'])), font=('helvatica', 12))
                    t.grid(row=j+3, column=k+4, padx=2, sticky='W')
                    t5.append(t)
                    t.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_enter(ev, t1, t2, t3, t4, t5))
                    t.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_leave(ev, t1, t2, t3, t4, t5))
                    tkinter.Label(f2).grid(row=j+3, column=k+5)

                for k in range(11, 21):
                    t = tkinter.Label(f2, text=str(random.choice(['A', 'P'])), font=('helvatica', 12))
                    t.grid(row=j+3, column=k+4, padx=4, sticky='W')
                    t5.append(t)
                    t.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_enter(ev, t1, t2, t3, t4, t5))
                    t.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_leave(ev, t1, t2, t3, t4, t5))

                for k in range(21, 31):
                    t = tkinter.Label(f2, text=str(random.choice(['A', 'P'])), font=('helvatica', 12))
                    t.grid(row=j+3, column=k+4, padx=3, sticky='W')
                    t5.append(t)
                    t.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_enter(ev, t1, t2, t3, t4, t5))
                    t.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_leave(ev, t1, t2, t3, t4, t5))

                t1.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_enter(ev, t1, t2, t3, t4, t5))
                t2.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_enter(ev, t1, t2, t3, t4, t5))
                t3.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_enter(ev, t1, t2, t3, t4, t5))
                t4.bind('<Enter>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_enter(ev, t1, t2, t3, t4, t5))
                t1.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_leave(ev, t1, t2, t3, t4, t5))
                t2.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_leave(ev, t1, t2, t3, t4, t5))
                t3.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_leave(ev, t1, t2, t3, t4, t5))
                t4.bind('<Leave>', lambda ev, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5: cur_leave(ev, t1, t2, t3, t4, t5))

            '''for k in range(3, 200):
                tix.Label(f2, text=k).grid(row=1, column=k)'''

            canvas1.create_window(0, 0, window=f1)
            canvas2.create_window(0, 0, window=f2)

            f1.update_idletasks()
            canvas1.itemconfigure("frame")

            f2.update_idletasks()
            canvas2.itemconfigure("frame")

            canvas1.config(scrollregion=canvas1.bbox("all"))
            canvas1.config(xscrollcommand=scrollx.set)

            canvas2.config(scrollregion=canvas2.bbox("all"))
            canvas2.config(yscrollcommand=scrolly.set)
            canvas2.config(xscrollcommand=scrollx.set)

    def settings(self):
        def color1():
            c1.config(fg='blue')
            c1.after(500, color2)

        def color2():
            c1.config(fg='red')
            c1.after(500, color3)

        def color3():
            c1.config(fg='green')
            c1.after(500, color1)

        n2 = ttk.Notebook(self.f3)
        '''f1 = ttk.Frame(n2)
        n2.add(f1, text='  Add a Student  ')
        f2 = ttk.Frame(n2)
        n2.add(f2, text='  Remove a Student  ')'''
        n2.pack()
        c1 = tkinter.Label(n2, text='Code Is In Construction !!!', font=('', 40))
        c1.config(fg='red')
        c1.pack()
        c1.after(1000, color1)

if __name__ == '__main__':
    app = tkinter.Tk()
    app.title('Attendance System')
    #app.geometry('1280x800')
    app.wm_state('zoomed')
    #app.configure(background='#008B8B')

    s = ttk.Style()
    s.configure('TLabelframe.Label', font=('times', 20))
    s.configure('TNotebook', tabposition='n')
    s.configure('TNotebook.Tab', font=('times', 16), padding=(10, 10, 10, 10))
    #s.configure('TLabelframe', background='#008B8B')

    l = Login()
    l.log()

    app.mainloop()