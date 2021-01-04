from tkinter import *

data = ''
operator = ''
I = 0
# ================================number clicking functions================================
def one_triggered():
    global data
    data += '1'
    screen_text.set(data)

def two_triggered():
    global data
    data += '2'
    screen_text.set(data)

def three_triggered():
    global data
    data += '3'
    screen_text.set(data)

def four_triggered():
    global data
    data += '4'
    screen_text.set(data)

def five_triggered():
    global data
    data += '5'
    screen_text.set(data)

def six_triggered():
    global data
    data += '6'
    screen_text.set(data)

def seven_triggered():
    global data
    data += '7'
    screen_text.set(data)

def eight_triggered():
    global data
    data += '8'
    screen_text.set(data)

def nine_triggered():
    global data
    data += '9'
    screen_text.set(data)

def zero_triggered():
    global data
    data += '0'
    screen_text.set(data)


# =====================================operational functions==================================
def plus_triggered():
    global data
    global operator
    global I
    I = int(data)
    operator = '+'
    data+='+'
    screen_text.set(data)

def minus_triggered():
    global data
    global operator
    global I
    I = int(data)
    operator = '-'
    data+='-'
    screen_text.set(data)

def multiply_triggered():
    global data
    global operator
    global I
    I = int(data)
    operator = 'x'
    data+='x'
    screen_text.set(data)

def divide_triggered():
    global data
    global operator
    global I
    I = int(data)
    operator = '/'
    data+='/'
    screen_text.set(data)

# =======================================result giving functions================================
def result():
    global data
    global operator
    global I
    if '+' in data:
        A = int(data.split('+')[1])
        result = I+A
        data = str(result)
        screen_text.set(data)
    elif '-' in data:
        A = int(data.split('-')[1])
        result = I - A
        data = str(result)
        screen_text.set(data)
    elif 'x' in data:
        A = int(data.split('x')[1])
        result = I * A
        data = str(result)
        screen_text.set(data)
    elif '/' in data:
        A = int(data.split('/')[1])
        result = I / A
        data = str(round(result,4))
        screen_text.set(data)

# ====================================clearing the screen functions================================
def clear():
    global data
    global operator
    global I

    data = ''
    screen_text.set(data)

# ==================================main window secion================================
root = Tk()
root.geometry('300x400')
root.title('Calculator')
# root.wm_iconbitmap('calculator.png')
root.resizable(0,0)
root.config()


# ===================================display =================================
screen_text = StringVar()
screen = Label(root, text='',anchor='c',textvariable= screen_text)
screen.config(bg='#E0F3F0',font=('cursive',25,'bold'))
screen.pack(expand=True, fill='both')


# ====================================button_row1================================
button_row1 = Frame(root)
button_row1.config()
button_row1.pack(expand=True, fill='both')

one = Button(button_row1,text="1",command=one_triggered)
one.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
one.pack(expand=True, fill='both', side='left')

two = Button(button_row1,text="2",command=two_triggered)
two.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
two.pack(expand=True, fill='both', side='left')

three = Button(button_row1,text="3",command=three_triggered)
three.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
three.pack(expand=True, fill='both', side='left')

plus = Button(button_row1,text="+",command=plus_triggered)
plus.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
plus.pack(expand=True, fill='both', side='left')


# ====================================button_row2================================
button_row2 = Frame(root)
button_row2.config()
button_row2.pack(expand=True, fill='both')

four = Button(button_row2,text="4",command=four_triggered)
four.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
four.pack(expand=True, fill='both', side='left')

five = Button(button_row2,text="5",command=five_triggered)
five.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
five.pack(expand=True, fill='both', side='left')

six = Button(button_row2,text="6",command=six_triggered)
six.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
six.pack(expand=True, fill='both', side='left')

minus = Button(button_row2,text="-",command=minus_triggered)
minus.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
minus.pack(expand=True, fill='both', side='left')



# ====================================button_row3================================
button_row3 = Frame(root)
button_row3.config()
button_row3.pack(expand=True, fill='both')

seven = Button(button_row3,text="7",command=seven_triggered)
seven.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
seven.pack(expand=True, fill='both', side='left')

eight = Button(button_row3,text="8",command=eight_triggered)
eight.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
eight.pack(expand=True, fill='both', side='left')

nine = Button(button_row3,text="9",command=nine_triggered)
nine.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
nine.pack(expand=True, fill='both', side='left')

multiply = Button(button_row3,text="x",command=multiply_triggered)
multiply.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
multiply.pack(expand=True, fill='both', side='left')



# ====================================button_row4================================
button_row4 = Frame(root)
button_row4.config()
button_row4.pack(expand=True, fill='both')

clear = Button(button_row4,text="C",command=clear)
clear.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
clear.pack(expand=True, fill='both', side='left')

zero = Button(button_row4,text="0",command=zero_triggered)
zero.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
zero.pack(expand=True, fill='both', side='left')

result = Button(button_row4,text="=",command=result)
result.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
result.pack(expand=True, fill='both', side='left')

divide = Button(button_row4,text="/",command=divide_triggered)
divide.config(relief='groove',border=0,font=('cursive',20,'bold'),bg = '#0B1229',fg ='skyblue')
divide.pack(expand=True, fill='both', side='left')


root.mainloop()