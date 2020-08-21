from tkinter import *
import socket


def main_window(event):
    def sendmsg(event):
        s.sendto((name.get() + ':' + msg_widget.get()).encode(), ('255.255.255.255', 11719))
        msg_widget.delete(0, END)
        msg_widget.insert(0, "")

    def tick():
        chatlog_widget.see(END)
        s.setblocking(False)
        try:

            message = s.recv(128)
            print(message)
            chatlog_widget.insert(END, message.decode() + '\n')
        except:
            interface.after(1, tick)
            return
        interface.after(1, tick)

    nick: str = name.get()
    tk.destroy()
    interface = Tk()
    nick_displayed_widget = Label(interface, text=nick)
    interface.title('chat client')
    interface.geometry('400x300')
    chatlog_widget = Text(interface)
    msg_widget = Entry(interface, textvariable=text)
    msg_widget.pack(side='bottom', fill='x', expand='true')
    nick_displayed_widget.pack(side='bottom', fill='x', expand='true')
    chatlog_widget.pack(side='top', fill='both', expand='true')
    msg_widget.bind('<Return>', sendmsg)
    interface.after(1, tick)
    interface.mainloop()




s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

tk = Tk()

text = StringVar()
name = StringVar()
tk.geometry('400x300')
tk.title('Chat client')

greeting_widget = Label(tk, text='Enter your name')
nick_entry_window_widget = Entry(tk, textvariable=name)
greeting_widget.pack(fill='x', expand='True')
nick_entry_window_widget.pack(fill='x', expand='True')
nick_entry_window_widget.bind('<Return>', main_window)

tk.mainloop()
