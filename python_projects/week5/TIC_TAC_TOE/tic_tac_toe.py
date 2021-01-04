from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('Tic-Tac-Toe')
root.geometry('500x600')
root.resizable(0,0)

PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

button = StringVar()
triggered = True

def trigger(button):
    global triggered
    if button['text'] == '' and triggered == True:
        button['text'] ='X'
        triggered = False
        checker()
    elif button['text'] == '' and triggered == False:
        button['text'] ='O'
        triggered = True
        checker()

def checker():
    if (btn1['text']=='X'and btn2['text']=='X' and btn3['text']=='X'):
        btn1.config(bg='red',fg='yellow')
        btn2.config(bg='red',fg='yellow')
        btn3.config(bg='red',fg='yellow')
        n=int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo('HURRAY','PlayerX wins!')
        Reset()
    elif (btn4['text']=='X'and btn5['text']=='X' and btn6['text']=='X'):
        btn4.config(bg='red',fg='yellow')
        btn5.config(bg='red',fg='yellow')
        btn6.config(bg='red',fg='yellow')
        n=int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerX wins!')
        Reset()
    elif (btn7['text']=='X'and btn8['text']=='X' and btn9['text']=='X'):
        btn7.config(bg='red',fg='yellow')
        btn8.config(bg='red',fg='yellow')
        btn9.config(bg='red',fg='yellow')
        n=int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerX wins!')
        Reset()
    elif (btn1['text']=='X'and btn4['text']=='X' and btn7['text']=='X'):
        btn1.config(bg='red',fg='yellow')
        btn4.config(bg='red',fg='yellow')
        btn7.config(bg='red',fg='yellow')
        n=int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerX wins!')
        Reset()
    elif (btn2['text']=='X'and btn5['text']=='X' and btn8['text']=='X'):
        btn2.config(bg='red',fg='yellow')
        btn5.config(bg='red',fg='yellow')
        btn8.config(bg='red',fg='yellow')
        n=int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerX wins!')
        Reset()
    elif (btn3['text']=='X'and btn6['text']=='X' and btn9['text']=='X'):
        btn3.config(bg='red',fg='yellow')
        btn6.config(bg='red',fg='yellow')
        btn9.config(bg='red',fg='yellow')
        n=int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerX wins!')
        Reset()
    elif (btn1['text']=='X'and btn5['text']=='X' and btn9['text']=='X'):
        btn1.config(bg='red',fg='yellow')
        btn5.config(bg='red',fg='yellow')
        btn9.config(bg='red',fg='yellow')
        n=int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerX wins!')
        Reset()
    elif (btn3['text']=='X'and btn5['text']=='X' and btn7['text']=='X'):
        btn3.config(bg='red',fg='yellow')
        btn5.config(bg='red',fg='yellow')
        btn7.config(bg='red',fg='yellow')
        n=int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerX wins!')
        Reset()


    if (btn1['text']=='O'and btn2['text']=='O' and btn3['text']=='O'):
        btn1.config(bg='red',fg='yellow')
        btn2.config(bg='red',fg='yellow')
        btn3.config(bg='red',fg='yellow')
        n=int(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerO wins!')
        Reset()
    elif (btn4['text']=='O'and btn5['text']=='O' and btn6['text']=='O'):
        btn4.config(bg='red',fg='yellow')
        btn5.config(bg='red',fg='yellow')
        btn6.config(bg='red',fg='yellow')
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerO wins!')
        Reset()
    elif (btn7['text']=='O'and btn8['text']=='O' and btn9['text']=='O'):
        btn7.config(bg='red',fg='yellow')
        btn8.config(bg='red',fg='yellow')
        btn9.config(bg='red',fg='yellow')
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerO wins!')
        Reset()
    elif (btn1['text']=='O'and btn4['text']=='O' and btn7['text']=='O'):
        btn1.config(bg='red',fg='yellow')
        btn4.config(bg='red',fg='yellow')
        btn7.config(bg='red',fg='yellow')
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerO wins!')
        Reset()
    elif (btn2['text']=='O'and btn5['text']=='O' and btn8['text']=='O'):
        btn2.config(bg='red',fg='yellow')
        btn5.config(bg='red',fg='yellow')
        btn8.config(bg='red',fg='yellow')
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerO wins!')
        Reset()
    elif (btn3['text']=='O'and btn6['text']=='O' and btn9['text']=='O'):
        btn3.config(bg='red',fg='yellow')
        btn6.config(bg='red',fg='yellow')
        btn9.config(bg='red',fg='yellow')
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerO wins!')
        Reset()
    elif (btn1['text']=='O'and btn5['text']=='O' and btn9['text']=='O'):
        btn1.config(bg='red',fg='yellow')
        btn5.config(bg='red',fg='yellow')
        btn9.config(bg='red',fg='yellow')
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerO wins!')
        Reset()
    elif (btn3['text']=='O'and btn5['text']=='O' and btn7['text']=='O'):
        btn3.config(bg='red',fg='yellow')
        btn5.config(bg='red',fg='yellow')
        btn7.config(bg='red',fg='yellow')
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        tkinter.messagebox.showinfo('HURRAY', 'PlayerO wins!')
        Reset()

def Reset():
    global triggered

    btn1['text'] = ''
    btn2['text'] = ''
    btn3['text'] = ''
    btn4['text'] = ''
    btn5['text'] = ''
    btn6['text'] = ''
    btn7['text'] = ''
    btn8['text'] = ''
    btn9['text'] = ''

    btn1.config(bg='#486982',fg = 'white')
    btn2.config(bg='#486982',fg = 'white')
    btn3.config(bg='#486982',fg = 'white')
    btn4.config(bg='#486982',fg = 'white')
    btn5.config(bg='#486982',fg = 'white')
    btn6.config(bg='#486982',fg = 'white')
    btn7.config(bg='#486982',fg = 'white')
    btn8.config(bg='#486982',fg = 'white')
    btn9.config(bg='#486982',fg = 'white')

    triggered = True

def New_game():
    Reset()
    PlayerX.set(0)
    PlayerO.set(0)

title_frame = Frame(root,width=500,height=100,)
title_frame.pack()

title_label = Label(title_frame,text='Tic-Tac-Toe',font=('cursive',30,'bold'))
title_label.pack(side='top',pady = 10)



playing_area = Frame(root,width=480,height=450,bg='blue')
playing_area.pack()

btn1 = Button(playing_area,text='',width=20,height=8,relief='groove',bg = '#486982',fg = 'white',command=lambda : trigger(btn1))
btn1.grid(row=0,column=0)

btn2 = Button(playing_area,text='',width=20,height=8,relief='groove',bg = '#486982',fg = 'white',command=lambda : trigger(btn2))
btn2.grid(row=0,column=1)

btn3 = Button(playing_area,text='',width=20,height=8,relief='groove',bg = '#486982',fg = 'white',command=lambda : trigger(btn3))
btn3.grid(row=0,column=2)

btn4 = Button(playing_area,text='',width=20,height=8,relief='groove',bg = '#486982',fg = 'white',command=lambda : trigger(btn4))
btn4.grid(row=1,column=0)

btn5 = Button(playing_area,text='',width=20,height=8,relief='groove',bg = '#486982',fg = 'white',command=lambda : trigger(btn5))
btn5.grid(row=1,column=1)

btn6 = Button(playing_area,text='',width=20,height=8,relief='groove',bg = '#486982',fg = 'white',command=lambda : trigger(btn6))
btn6.grid(row=1,column=2)

btn7 = Button(playing_area,text='',width=20,height=8,relief='groove',bg = '#486982',fg = 'white',command=lambda : trigger(btn7))
btn7.grid(row=2,column=0)

btn8 = Button(playing_area,text='',width=20,height=8,relief='groove',bg = '#486982',fg = 'white',command=lambda : trigger(btn8))
btn8.grid(row=2,column=1)

btn9 = Button(playing_area,text='',width=20,height=8,relief='groove',bg = '#486982',fg = 'white',command=lambda : trigger(btn9))
btn9.grid(row=2,column=2)




score_area = Frame(root,width=240,height=100)
score_area.pack(side=LEFT)

playerX = Label(score_area,text="PlayerX:",font=('cursive',15,'bold'),relief='groove',bd = 0)
playerX.grid(row=0,column=0,padx=10)

score_x = Entry(score_area,font=('cursive',10,'bold'),textvariable = PlayerX)
score_x.grid(row=0,column=1,padx=0)

playerO = Label(score_area,text="PlayerO:",font=('cursive',15,'bold'),relief='groove',bd=0)
playerO.grid(row=1,column=0,padx=10)

score_o = Entry(score_area,font=('cursive',10,'bold'),textvariable=PlayerO)
score_o.grid(row=1,column=1,padx=0)





control_area = Frame(root,width=240,height=100)
control_area.pack(side=RIGHT)

new_game = Button(control_area,text="New Game",width=20, font= ('cursive',12,'bold'),relief='groove',command=New_game)
new_game.grid(row=0,column=0,padx=20,pady=5)

reset = Button(control_area,text="Reset",width=20, font = ('cursive',12,'bold'),relief='groove',command=Reset)
reset.grid(row=1,column=0,padx=20,pady=5)



root.mainloop()
