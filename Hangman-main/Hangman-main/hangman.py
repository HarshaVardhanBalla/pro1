# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:04:24 2023

@author: harsh
"""

from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


window = Tk()
window.title('HANG-MAN')
Fruits_list= ['APPLE','MANGO','CITRUS']
            
Images = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

def newGame():
    root.destroy()
    global fill_up_word
    global GuessesCount
    GuessesCount =0
    
    the_word=random.choice(Fruits_list)
    fill_up_word = " ".join(the_word)
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
	global GuessesCount
	if GuessesCount<11:	
		txt = list(fill_up_word)
		guessed = list(lblWord.get())
		if fill_up_word.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblWord.set("".join(guessed))
				if lblWord.get()==fill_up_word:
					messagebox.showinfo("Hangman","YOU WON!")
		else:
			GuessesCount += 1
			Image_Label.config(image=Images[GuessesCount])
			if GuessesCount==11:
					messagebox.showwarning("SORRY Hangman","YOU LOST")


Image_Label=Label(window)
Image_Label.grid(row=0, column=0, columnspan=3, padx=10, pady=40)


  
lblWord = StringVar()
Label(window, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4,fg='white', bg='black').grid(row=1+n//9,column=n%9)
    n+=1

def first_page():
    global root
    root = Tk()
    root.title("Welcome Page Interface")
    root.minsize(width = 400, height = 400)
    root.maxsize(width = 400, height = 400)

    button2 = Label(root, text = "HANGMAN GAME", width = 150, bg="cyan",font=14,height = 10, relief=RAISED)
    button2.pack(padx = 1, pady = 50 )


    button5 = Button(root, text = "PRESS TO START",command=newGame,bg="orange",font=12, width = 30, height = 1)
    button5.pack(padx = 10, pady= 20 )

    root.mainloop()
first_page()

