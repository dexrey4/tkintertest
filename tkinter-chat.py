import tkinter as tk
import tkinter.scrolledtext
import socket, pickle, threading, time
import tkinter.font as font
from tkinter import messagebox
import sys, time
def error(data):
    messagebox.showinfo('Error', data)
global window
window=tk.Tk()
myFont = font.Font(family='Helvetica')

def clear1(arg):
    entry1.delete(0,tk.END)
def clear2(arg):
    entry2.delete(0,tk.END)
def clear3(arg):
    entry3.delete(0,tk.END)
def button():
    global name
    name = entry1.get()
    global ip1
    global run
    run = True
    ip1 = entry2.get()
    global port1
    port1 = entry3.get()
    window.destroy()
def kill(arg):
    if arg:
        error(arg)
    import sys
    root.destroy()
    #window.destroy()
    sys.exit()

entry1 = tk.Entry(width=50,font=40)
entry1.bind("<FocusIn>",clear1)
entry1['font'] = myFont
entry1.insert(0,"What is your username?")
entry1.place(relx=0.5,y=70,anchor="center")

entry2 = tk.Entry(width=50,font=40)
entry2.bind("<FocusIn>",clear2)
entry2['font'] = myFont
entry2.insert(0,"What is the IP?")
entry2.place(relx=0.5,y=170,anchor="center")

entry3 = tk.Entry(width=50,font=40)
entry3.bind("<FocusIn>",clear3)
entry3['font'] = myFont
entry3.insert(0,"What is the port?")
entry3.place(relx=0.5,y=270,anchor="center")

button1 = tk.Button(text="Connect", font=50, command=button, height=2,width=10)
button1.place(relx=0.46, y=330)




window.title('Tkinter Chat Thing')
window.geometry("900x500")
window.mainloop()
if run:
  nick = name
  ip = ip1
  port = port1

  def receive():
      while True:
          try:
          # Receive Message From Server
          # If 'NICK' Send Nickname
              message = client.recv(1024)
              print(message)
              if message == b'NICK':
                  client.send(nick.encode('ascii'))
                  #print(nick)
              else:
                  add_to_chatbox(message.decode('ascii'))
          except:
              #  Close Connection When Error
              #print(sys.exc_info())
              print("An error occured!")
              client.close()
              exit()
        #break

  def connect():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip,port))
    
    #    kill("Either the IP or Port is incorrect, does not exist, or has refused your connection. Please retry :)")
        

  def write(b):
    message = b
    client.sendall(message.encode('ascii'))

  def startthread():
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()


  HEIGHT = 350
  WIDTH = 500
  global root
  root = tk.Tk()
  root.title("TkinterChatThing")

  canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
  canvas.pack()
  lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
  lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
  text = tk.scrolledtext.ScrolledText(lower_frame)
  text.place(relwidth=1, relheight=1)


  frame = tk.Frame(root, bg='#80c1ff', bd=5)
  frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

  button2 = tk.Button(root, text="Exit", font=30, command=lambda: kill(None))
  button2.place(relx=0.7, relheight=0.10, relwidth=0.25, rely=0.87)

  entry = tk.Entry(frame, font=40)
  entry.place(relwidth=0.65, relheight=1)
  words = []
  def send(arg):
    b = entry.get()
    if not b.strip() == '':
      b = nick + ": " + b
      write(b)
      #print(words)
    entry.delete(0,"end")
    

  def add_to_chatbox(b):
    text.config(state='normal')
    text.insert(tk.END, b + '\n')
    text.config(state='disabled')
    
  button = tk.Button(frame, text="Send", font=30, command=lambda: send("ya pressed a button"))
  button.place(relx=0.7, relheight=1, relwidth=0.3)


  entry.bind("<Return>", send)
  words.clear()
  text.config(state="disabled")
  connect()
  startthread()
  root.mainloop()
