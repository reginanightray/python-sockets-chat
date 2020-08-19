from tkinter import *
import socket

def tick():
    log.see(END)
    s.setblocking(False)
    try:
        message = s.recv(128)
        print(message)
        log.insert(END, message.decode() + '\n')
    except:
        interface.after(1, tick)
        return
    interface.after(1, tick)
    return


def sendmsg(event):
    s.sendto((name.get() + ':' + text.get()).encode(), ('255.255.255.255', 11719))
    text.set('')


interface = Tk()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

text = StringVar()
name = StringVar()
name.set('me')
text.set('')
interface.title('chat client')
interface.geometry('400x300')

log = Text(interface)
nick = Entry(interface, textvariable=name)
msg = Entry(interface, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both', expand='true')

msg.bind('<Return>', sendmsg)

s.sendto(''.encode(), ('255.255.255.255', 11719))
interface.after(1, tick)

interface.mainloop()
