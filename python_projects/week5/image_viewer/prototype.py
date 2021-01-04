import os
from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('Pycture viewer')
root.config(bg='#4e4e4e')
# root.geometry('1x1')



dir = os.walk('./images/')
list = list(dir)
images = []
for i  in list:
    for j in i:
        images.append(j)


images = images[-1]
loaded_images = []
for item in images:
    img = ImageTk.PhotoImage(Image.open(f"images/{item}"))
    loaded_images.append(img)

def next_image(image_number):
    global display
    global next_btn
    global prev_btn

    display.grid_forget()
    display = Label(image=loaded_images[image_number-1],bg='#4e4e4e')
    next_btn = Button(text=">>", relief='groove', width=10, height=1, bg='#151515', fg='skyblue', bd=0,
                      font=('cursive', 15, 'bold'), command=lambda: next_image(image_number+1))
    previous_btn = Button(text="<<", relief='groove', width=10, height=1, bg='#151515', fg='skyblue', bd=0,
                          font=('cursive', 15, 'bold'), command=lambda:previous_image(image_number-1))

    if image_number == len(loaded_images):
        next_btn = Button(root, text=">>",relief='groove',width = 10,height = 1,bg='#151515',fg='skyblue', bd =0,font=('cursive',15,'bold'),state=DISABLED)

    display.grid(row=0, column=0, columnspan=3)
    previous_btn.grid(row=1, column=0, padx=2, pady=3)

    next_btn.grid(row=1, column=2, padx=2, pady=3)


def previous_image(image_number):

    global display
    global next_btn
    global previous_btn

    display.grid_forget()
    display = Label(image=loaded_images[image_number - 1], bg='#4e4e4e')
    next_btn = Button(text=">>", relief='groove', width=10, height=1, bg='#151515', fg='skyblue', bd=0,
                      font=('cursive', 15, 'bold'), command=lambda: next_image(image_number + 1))
    previous_btn = Button(text="<<", relief='groove', width=10, height=1, bg='#151515', fg='skyblue', bd=0,
                          font=('cursive', 15, 'bold'), command=lambda: previous_image(image_number - 1))

    if image_number == 1 :
        previous_btn = Button(text="<<", relief='groove', width=10, height=1, bg='#151515', fg='skyblue', bd=0,
                              font=('cursive', 15, 'bold'), command=previous_image, state=DISABLED)

    display.grid(row=0, column=0, columnspan=3)
    previous_btn.grid(row=1, column=0, padx=2, pady=3)

    next_btn.grid(row=1, column=2, padx=2, pady=3)

display = Label(image=loaded_images[0],bg='#4e4e4e')
display.grid(row=0,column=0,columnspan=3)

previous_btn = Button(text="<<",relief='groove',width = 10,height = 1,bg='#151515',fg='skyblue', bd =0,font=('cursive',15,'bold'),command = previous_image,state=DISABLED)
previous_btn.grid(row=1,column=0,padx=2,pady=3)

exit_btn = Button(text="X",relief='groove',width=6,height = 1,bg='#151515',fg='red',bd = 0,font=('cursive',15,'bold'),command=root.quit)
exit_btn.grid(row=1,column=1,padx=0,pady=3)

next_btn = Button(text=">>",relief='groove',width = 10,height = 1,bg='#151515',fg='skyblue', bd =0,font=('cursive',15,'bold'),command=lambda:next_image(2))
next_btn.grid(row=1,column=2,padx=2,pady=3)

# print(root.winfo_width())
root.mainloop()
