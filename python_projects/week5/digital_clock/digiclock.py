from tkinter import *
import time

def clock():
    hour = str(time.strftime('%H'))
    minute = str(time.strftime('%M'))
    seconds = str(time.strftime('%S'))
    if int(hour) > 12 and int(minute) > 0:
        label_ampm.config(text='PM')
    if int(hour) > 12 :
        hour = str((int(hour)-12))

    label_hour1.config(text=hour)
    label_minute1.config(text=minute)
    label_seconds1.config(text=seconds)

    label_hour1.after(1000,clock)

root = Tk()
root.title('DigiTime')
root.geometry('630x260')
root.config(bg = '#0d1418')
root.maxsize(630,260)
root.minsize(630,260)

label_hour1 = Label(root,text = '12',font = ('sans serif',52,'bold'),bg = '#33312E',fg = '#ccc6b8')
label_hour1.place(x = '30',y = '30',width = '120',height = '150')

label_hour2 = Label(root,text= 'HOURS',font= ('sans serif',13,'bold'),bg = '#33312E',fg = '#ccc6b8')
label_hour2.place(x = '30',y = '200',width = '120',height = '30')

label_minute1 = Label(root,text = '59',font = ('sans serif',52,'bold'),bg = '#33312E',fg = '#ccc6b8')
label_minute1.place(x = '180',y = '30',width = '120',height = '150')

label_minute2 = Label(root,text= 'MINUTES',font= ('sans serif',13,'bold'),bg = '#33312E',fg = '#ccc6b8')
label_minute2.place(x = '180',y = '200',width = '120',height = '30')

label_seconds1 = Label(root,text = '59',font = ('sans serif',52,'bold'),bg = '#33312E',fg = '#ccc6b8')
label_seconds1.place(x = '330',y = '30',width = '120',height = '150')

label_seconds2 = Label(root,text= 'SECONDS',font= ('sans serif',13,'bold'),bg = '#33312E',fg = '#ccc6b8')
label_seconds2.place(x = '330',y = '200',width = '120',height = '30')

label_ampm = Label(root,text = 'AM',font = ('sans serif',45,'bold'),bg = '#33312E',fg = '#ccc6b8')
label_ampm.place(x = '480',y = '30',width = '120',height = '150')

label_ampm2 = Label(root,text= 'AM/PM',font= ('sans serif',13,'bold'),bg = '#33312E',fg = '#ccc6b8')
label_ampm2.place(x = '480',y = '200',width = '120',height = '30')

clock()

root.mainloop()