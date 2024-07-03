import tkinter


def led_on():
    global canvs,led
    canvs.itemconfig(led,fill = "red")
    canvs.itemconfig(text = "led is on")        


def led_off():
    global canvs,led
    canvs.itemconfig(led,fill = "white")
    canvs.itemconfig(text = "led is off")        
   
  
    
    
window = tkinter.Tk()
window.title("led control")
window.geometry("500x500+150+200")
window.resizable(False,False)


canvs=tkinter.Canvas(window, height=150, width=150)

coordinate = 60, 50, 150, 150
led=canvs.create_oval(coordinate,fill="white",offset=["center"])




button=tkinter.Button(window,text="led on",command=led_on)
button2=tkinter.Button(window,text="led off",command=led_off)

b=button.place(x=220,y=200)
b2=button2.place(x=220,y=240)
canvs.place(x=150,y=10)


window.mainloop()