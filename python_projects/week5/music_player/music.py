from tkinter import *
import pygame
from tkinter import filedialog
import os

pygame.mixer.init()
current_dir = os.getcwd().replace('\\','/')
root1= Tk()
root1.title('instructions for using this program')
root1.geometry('700x450')
root1.resizable(0,0)


paused = False
def quit_instructions():

    root1.quit()
    root = Tk()
    root.title('MusiPy')
    root.config(bg='#323232', relief='groove', bd=0)
    root.geometry('700x300')
    root.resizable(0, 0)

    def add_songs():
        songs = filedialog.askopenfilenames(initialdir=current_dir, title='choose songs\\songs',
                                            filetypes=(('mp3 file', '*.mp3'),))
        for song in songs:
            song = song.replace(f'{current_dir}/audio/', '')
            song = song.replace('.mp3', '')
            songs_list_display.insert(END, song)

    def play():
        song = songs_list_display.get(ACTIVE)
        song = f'{current_dir}/audio/{song}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)



    def pause(is_paused):
        global paused
        paused = is_paused
        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True

    def next():
        new_song = songs_list_display.curselection()
        new_song = new_song[0] + 1
        song = songs_list_display.get(new_song)
        song = f'{current_dir}/audio/{song}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        songs_list_display.selection_clear(0, END)
        songs_list_display.activate(new_song)
        songs_list_display.selection_set(new_song, last=None)

    def previous():
        previous_song = songs_list_display.curselection()
        previous_song = previous_song[0] - 1
        song = songs_list_display.get(previous_song)
        song = f'{current_dir}/audio/{song}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        songs_list_display.selection_clear(0, END)
        songs_list_display.activate(previous_song)
        songs_list_display.selection_set(previous_song, last=None)

    songs_list_display = Listbox(root, bg='#191919', fg='white', font=('cursive', 10, 'bold'), width=68, height=80,
                                 relief='groove', bd=0, selectbackground='skyblue', selectforeground='black')
    songs_list_display.pack(side=LEFT, padx=5, pady=5, ipady=5, ipadx=5)

    button_display = Frame(root, width=190, height=288, relief='groove', bg='#323232')
    button_display.place(x=500, y=6)

    play_button = Button(button_display, text="|>", font=('cursive', 16, 'bold'), width=13, height=1, relief='groove',
                         bd=0, bg='#191919', fg='skyblue', command=play)
    play_button.grid(row=0, column=0, padx=5, pady=5)

    pause_button = Button(button_display, text="||", font=('cursive', 16, 'bold'), width=13, height=1, relief='groove',
                          bd=0, bg='#191919', fg='skyblue', command=lambda: pause(paused))
    pause_button.grid(row=1, column=0, padx=5, pady=5)

    next_button = Button(button_display, text=">>", font=('cursive', 16, 'bold'), width=13, height=1, relief='groove',
                         bd=0, bg='#191919', fg='skyblue', command=next)
    next_button.grid(row=2, column=0, padx=5, pady=5)

    previous_button = Button(button_display, text="<<", font=('cursive', 16, 'bold'), width=13, height=1,
                             relief='groove', bd=0, bg='#191919', fg='skyblue', command=previous)
    previous_button.grid(row=3, column=0, padx=5, pady=5)

    add_button = Button(button_display, text="+", font=('cursive', 16, 'bold'), width=13, height=1, relief='groove',
                        bd=0, bg='#191919', fg='skyblue', command=add_songs)
    add_button.grid(row=4, column=0, padx=5, pady=5)

    exit_button = Button(button_display, text="x", font=('cursive', 16, 'bold'), width=13, height=1, relief='groove',
                         bd=0, bg='#191919', fg='red', command=root.quit)
    exit_button.grid(row=5, column=0, padx=5, pady=5)

    root1.destroy()
    root.mainloop()

instructions = Label(root1, text='''0. MusiPy, a very basic music player windows os, read the instructions below.....

1. please create a folder named "audio" in the same directory as this .py file contain.
   Then copy all .mp3 files in this folder.

2. after performing the first step, run the program and then click on '+' button which will
   open a window to select songs in audio folder that is created before.

3. select the song/songs to be viewed on the app display.

4. click on the song which you want to play and then click the "|>" 
    to play the track as there is auto play option available.

5. click on "||" to pause the track.

6. click on ">>" to play the next track.

7. click on "<<" to play the previous track to the current one.

8. click on the "X" button to exit from the music player

9. after reading the above, click on the "OK" button to launch the music player
''',font=('cursive',10,'bold'),padx=5, pady=8)
instructions.pack()


exit = Button(root1,text="OK",command=quit_instructions,width=15,height=2,relief='groove')
exit.pack()

mainloop()