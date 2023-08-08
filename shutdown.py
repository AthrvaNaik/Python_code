import os
from tkinter import *

def Restart():
    os.system("shutdown/r /t 1")
def Restart_time():
    os.system("shutdown /r /t 20")
def Logout():
    os.system("shutdown -1")  
def Shtdown():
    os.system("shutdown /s /t 1")  
sd=Tk()
sd.title("ShutDown")
sd.geometry("500x500")
sd.config(bg="cyan")

R_button=Button(sd,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=Restart)
R_button.place(x=150,y=60,height=40,width=200)
Rt_button=Button(sd,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=Restart_time)
Rt_button.place(x=150,y=170,height=40,width=200)
lg_button=Button(sd,text="Log Out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=Logout)
lg_button.place(x=150,y=270,height=40,width=200)
sd_button=Button(sd,text="Shut Down",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=Shtdown)
sd_button.place(x=150,y=370,height=40,width=200)
sd.mainloop()
