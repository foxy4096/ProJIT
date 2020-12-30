from tkinter import*
root=Tk()
l_1=Label(root,text="Admission Form",font="bold 20").grid(row=0,column=2)

pa=Label(root,text="Password",font="bold 10")

pb=Label(root,text="Username",font="bold 10")

na=Label(root,text="Name",font="bold 10")

age=Label(root,text="Age",font="bold 10")

pa.grid(row=1,)
pb.grid(row=2,column=0)
na.grid(row=3,column=0)
age.grid(row=4)


pa=StringVar()
pb=StringVar()
na=StringVar()
age=StringVar()
foll=IntVar()



a=Entry(root,textvariable=pa)
b=Entry(root,textvariable=pb)
c=Entry(root,textvariable=na)
d=Entry(root,textvariable=age)
a.grid(row=1,column=2)
b.grid(row=2,column=2)
c.grid(row=3,column=2)
d.grid(row=4,column=2)



b_1=Button(root,text="submit").grid(row=6,column=2)

fs=Checkbutton(root,text="Accept",font="bold 10",variable=foll).grid(row=5,column=2)
root.mainloop()