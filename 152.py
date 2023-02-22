from tkinter import *
root=Tk()
root.title("Multidimensional Arrays")

root.geometry("500x500")

label= Label(root)

array_2d = [["Dilean","A"], ["Joshua", "B"],["Vaniah","C"]]
print(array_2d[0][1])

array_3d = [[["Dilean","A+","Excelllent"],["Joshua","A","Very Good"],["Vaniah","B", "Good"]]]
print(array_3d[0][0][2])

def report():
    label["text] = array_3d[0][1][0] + " got grade " + array_3d[0][1][1] +"and he is doing " + array_3d[0][1][2]

btn = Button(root, text= "show report", command = report)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)
  
label.place(relx = 0.5, rely =0.6, anchor = CENTER)
        
root.mainloop()
