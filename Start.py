try:
    import tkinter as tk
    from tkinter import messagebox
    from Filing import file
    from gamee import Run
    from PIL import ImageTk
except ImportError:
    import tkinter as tk
    from tkinter import messagebox
    from Filing import file
    from gamee import Run
    from PIL import ImageTk
    print(ImportError)


class begin(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.f = tk.Frame(self, bg="black", height=200, width=200)
        self.f.place(relwidth=1, relheight=1)
        self.but_image = ImageTk.PhotoImage(file="images/spaceship.png")
        self.but_image1 = ImageTk.PhotoImage(file="images/spaceship1.png")
        self.but_image2 = ImageTk.PhotoImage(file="images/spaceship2.png")
        self.imag = ImageTk.PhotoImage(file="images/space_planets_takeoff_explosion_96455_1280x800.jpg")
        self.l1 = tk.Label(self.f, image=self.imag)
        self.l1.place(relheight=1, relwidth=1)
        self.b1 = tk.Button(self.f, text="Start Game", height=3, width=25, bg="blue", fg="white",
                            activebackground="Pink",
                            activeforeground="purple", highlightcolor="red", command=self.go)
        self.b1.place(rely=0.4, relheight=0.09, relwidth=0.12)
        self.b2 = tk.Button(self.f, text="Score", height=3, width=25, bg="blue", fg="white",
                            activebackground="Pink",
                            activeforeground="purple", highlightcolor="red", command=self.high_score)
        self.b2.place(rely=0.5, relheight=0.09, relwidth=0.12)
        self.b3 = tk.Button(self.f, text="Help", height=3, width=25, bg="blue", fg="white", activebackground="Pink",
                            activeforeground="purple", highlightcolor="red", command=self.help)
        self.b3.place(rely=0.6, relheight=0.09, relwidth=0.12)
        self.b5 = tk.Button(self.f, text="About", height=3, width=25, bg="blue", fg="white", activebackground="Pink",
                            activeforeground="purple", highlightcolor="red", command=self.about)
        self.b5.place(rely=0.7, relheight=0.09, relwidth=0.12)
        self.b6 = tk.Button(self.f, text="Exit", height=3, width=25, bg="blue", fg="white", activebackground="Pink",
                            activeforeground="purple", highlightcolor="red", command=self.exi)
        self.b6.place(rely=0.8, relheight=0.09, relwidth=0.12)
        self.b7 = tk.Button(self.f, text="Delete Records", height=2, width=15, bg="blue", fg="white",
                            activebackground="Pink",
                            activeforeground="purple", highlightcolor="red", command=self.clear)
        self.b7.place(rely=0.9, relx=0.85, relheight=0.09, relwidth=0.12)

    @staticmethod
    def exi():
        if messagebox.askyesno("Exit", "Do you really want to Exit?") == 1:
            exit()

    def about(self):
        self.aboutlev = tk.Toplevel(self)
        self.aboutlev.resizable(0, 0)
        self.aboutlev.grab_set()
        self.aboutlev.title("About")
        self.aboutlev.iconbitmap('images/aboutlevelicon.ico')
        self.aboutframe = tk.Frame(self.aboutlev, bg="Black")
        self.aboutframe.pack()
        self.aboutt = tk.Label(self.aboutframe, text="Object Oriented Project"
                                                     "\nMade by M.Mussab Zafar (18K-0302)",
                               fg="white", bg='black')
        self.aboutt.pack()
        self.aboutbutton = tk.Button(self.aboutframe, text="Back", command=self.aboutlev.destroy)
        self.aboutbutton.pack()

    def high_score(self):
        f = file()
        self.highlev = tk.Toplevel(self)
        self.highlev.grab_set()
        self.highlev.geometry("200x300")
        self.highlev.resizable(0, 0)
        self.highlev.iconbitmap('images/main.ico')
        self.highlev.title("Score")
        score = f.reader()
        self.highlist = tk.Listbox(self.highlev, bg="Black", fg='White')
        self.highlist.place(relwidth=1, relheight=1)
        try:
            for line in score:
                self.highlist.insert(tk.END, line)
        except ValueError:
            print("Nothing Found in Score")
        except:
            pass

    def help(self):
        self.helplev = tk.Toplevel(self)
        self.helplev.resizable(0, 0)
        self.helplev.grab_set()
        self.helplev.iconbitmap('images/helplevelicon.ico')
        self.helplev.title("Help")
        self.helpframe = tk.Frame(self.helplev, bg="Black")
        self.helpframe.pack()
        self.instruct = tk.Label(self.helpframe, text="This is a simple 2d Space shooter :)"
                                                      "\nEach Player is given 3 chances"
                                                      "\nThe enemy ships have 3 different waves"
                                                      "\nPlayer ship moves with left and right keys and fires with "
                                                      "Space Bar "
                                                      "\nAt the End of the game: Name, score and health remaining is "
                                                      "displayed"
                                                      "\nThe Save File is deleted automatically after 10 saves",
                                 bg="Black", fg="White")
        self.instruct.pack()
        self.instructbutton = tk.Button(self.helpframe, text="Back", command=self.helplev.destroy)
        self.instructbutton.pack()

    def clear(self):
        file.del_file()

    def go(self):
        self.toplev = tk.Toplevel(self)
        self.toplev.grab_set()
        self.toplev.resizable(0, 0)
        self.entry_var = tk.StringVar()
        self.entry_widget = tk.Entry(self.toplev, textvariable=self.entry_var)
        self.entry_widget.pack()
        self.entry_widget.focus()
        self.button1 = tk.Button(self.toplev, state="disabled", text='Submit', command=self.send_over)
        self.button1.pack()
        self.entry_var.trace("w", self.check)

    def check(self, *args):
        if self.entry_var.get() != '' and self.entry_var.get().isspace() == False:
            self.button1.config(state="normal")
        else:
            self.button1.config(state="disabled")

    def send_over(self):
        try:
            if self.entry_var.get().isalpha():
                self.var = self.entry_var.get()
            else:
                raise Exception
        except Exception:
            tk.messagebox.showerror("Error", "Username cannot consist of Numbers and Special Characters")
            self.send_over
        else:
            self.toplev.destroy()
            self.choicelev = tk.Toplevel(self)
            self.choicelev.grab_set()
            self.choicelev.resizable(0, 0)
            self.chbutton1 = tk.Button(self.choicelev, image=self.but_image,
                                       command=lambda: self.choice(0))
            self.chbutton1.pack()
            self.chbutton2 = tk.Button(self.choicelev, image=self.but_image1,
                                       command=lambda: self.choice(1))
            self.chbutton2.pack()
            self.chbutton3 = tk.Button(self.choicelev, image=self.but_image2,
                                       command=lambda: self.choice(2))
            self.chbutton3.pack()

    def choice(self, choice):
        self.choicelev.destroy()
        self.withdraw()
        Go = Run(choice)
        score = Go.run_game()
        self.deiconify()
        f = file()
        f.collect(self.var, score)
        f.filer()


if __name__ == '__main__':
    master = begin()
    master.geometry("1200x700+0+0")
    master.title("Alien Invasion")
    master.iconbitmap('images/main.ico')
    master.resizable(0, 0)
    master.mainloop()
