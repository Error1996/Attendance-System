import Calender
import tkinter
import calendar

tk = tkinter.Tk()
can = tkinter.Canvas(tk)
can.pack()
cal = calendar.calendar(firstweekday=calendar.SATURDAY)
can.create_window(100, 100, window=cal)
can.update_idletasks()
can.itemconfigure('frame')
tk.mainloop()