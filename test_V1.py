import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.be_quiet = tk.Button(self, fg="red", bg="#8a0303")

        self.be_quiet['text'] = 'SHUT UP!!!'

        self.be_quiet['command'] = lambda: print('SHUTTTTTTT UPPPPPPPPPPPPP!!!!!!!!!\nI HATE YOU!!!!!!')

        self.be_quiet['activebackground'] = '#75fcfc'

        self.be_quiet['activeforeground'] = '#00ffff'
        self.be_quiet.pack(side='bottom')

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
    #def create_widget(self,text,command,buttonname):
     # self.buttonname = tk.Button(self)
      #self.hi_there["text"] = "Hello World\n(click me)"
      #self.hi_there["command"] = self.say_hi
      #self.hi_there.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
