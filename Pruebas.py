import tkinter as tk
def funcion1():
    print("Se realizó la suma satisfactoriamente :D")
def multiplicar():
    x=int(campo1.get())
    y=int(campo2.get())
    n=int(campo3.get())
    m=int(campo4.get())
    result1.set(x*n)
    result2.set(x*m)
    result3.set(y*n)
    result4.set(y*m)
def sumar():
    p=int(result1.get())
    q=int(result2.get())
    r=int(result3.get())
    s=int(result4.get())
    result5.set(p-s)
    result6.set(q+r)
    v=str(result5.get())
    i=str(result6.get())
    result7.set(v+' + '+i+'i')
marco = tk.Tk()
marco.title("Programa números complejos")
marco.geometry('500x500')
marco.configure (background = '#fafad2')

result1=tk.StringVar()
result2=tk.StringVar()
result3=tk.StringVar()
result4=tk.StringVar()
result5=tk.StringVar()
result6=tk.StringVar()
result7=tk.StringVar()
l1=tk.Label(marco, text="a = ").grid(row=0)
l2=tk.Label(marco, text="b = ").grid(row=1)
l3=tk.Label(marco, text="c = ").grid(row=2)
l4=tk.Label(marco, text="d = ").grid(row=3)
l5=tk.Label(marco, textvariable=result1).grid(row=4,column=0)
l6=tk.Label(marco, textvariable=result2).grid(row=5,column=0)
l7=tk.Label(marco, textvariable=result3).grid(row=6,column=0)
l8=tk.Label(marco, textvariable=result4).grid(row=7,column=0)
l9=tk.Label(marco, textvariable=result7).grid(row=8,column=0)

campo1=tk.Entry(marco)
campo2=tk.Entry(marco)
campo3=tk.Entry(marco)
campo4=tk.Entry(marco)

campo1.grid(row=0,column=1)
campo2.grid(row=1,column=1)
campo3.grid(row=2,column=1)
campo4.grid(row=3,column=1)

tk.Button(marco, text="Multiplicar",command=multiplicar).grid(row=9, column=0,sticky=tk.W,pady=4)
tk.Button(marco, text="Sumar",command=sumar).grid(row=10, column=0,sticky=tk.W,pady=4)

marco.mainloop()