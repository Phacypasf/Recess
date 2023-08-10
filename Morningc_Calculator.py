import tkinter as tk
expression=""
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0,tk.END)

def button_equal():
 expression =entry.get()
result=str(eval(expression))
tk.Entry.delete(0,tk.END)
tk.Entry.insert(tk.END, tk.Result)

window =tk.Tk()
window .tittlt("ACAN BRENDA'S SIMPLE CALCULATOR")
entry =tk.Entry(window, width =20, justify=tk.RIGHT)
entry.grid (row= 0, column =0,columnspan =3)
buttons=["7","8","9",
        "4","5","6",
        "1,","2","3",
        "0"]
row=1
col=0
for button in buttons:
    tk.button( window, text=button,width=5,command=lambda b=button:button_click(b)).grid(row=row,column=col)
    col+=1
    if col>2:
        col=0
        row+=1

operators={"+","-","*","/","."}
row=1
col=3
for operator in operators:
 tk.button( window, text=operator,width=5,command=lambda o=operator:button_click(o)).grid(row=row,column=col)
row+=1

tk.button( window, text="c",width=5,command=button_clear).grid(row=row,column=0)
tk.button( window, text="=",width=5,command=button_equal).grid(row=row,column=1)

window.mainloop()
