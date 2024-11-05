from tkinter import *

root = Tk()
root.title("Product Determiner Software 420")
root.geometry("500x400")


label = Label(root, text="Let's Multiply 2 Numbers", fg="white", bg="#ff0000", font=("Helvetica", 16, "bold"), height=2, width=300)
label.pack(pady=10)


n1_label = Label(root, text="Enter Number 1", bg="#ffffff")
n1_label.pack()

n1_entry = Entry(root, width=20)
n1_entry.pack(pady=5)


n2_label = Label(root, text="Enter Number 2", bg="#ffffff")
n2_label.pack()

n2_entry = Entry(root, width=20)
n2_entry.pack(pady=5)


def multiply():
    text_box.delete(1.0, END)  
    
    try:
       
        n1 = int(n1_entry.get()) 
        n2 = int(n2_entry.get())
        product = n1 * n2
        
        text_box.insert(END, "Here's the Final Product.....\n")
        text_box.insert(END, f"{n1} x {n2} = {product}\n")
        
    except ValueError:
       text_box.insert(END, "Please Enter Valid Numbers!")

text_box = Text(root, height=4, width=40, wrap=WORD)
text_box.pack(pady=10)

mul_btn = Button(root, text="Calculate", command=multiply, height=1, bg="#0027ff", fg="white")
mul_btn.pack(pady=5)

root.mainloop()



        
        

