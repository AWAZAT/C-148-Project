from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("550x300")

label_list = Label(root)
label_item = Label(root)

list_items = ["Bottle", "Chocolates", "Chips", "Gift Card", "Toy"]
label_list["text"] = "listed Items : " + str(list_items)

def bag_items():
    random_item = random.sample(range(1, 5), 1)
    label_list["text"] = "Put Item No. : " + str(random_item) + "In Bag"

label_list.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    
btn = Button(root, text="What Will This Kid Get? ", command = bag_items, bg = "orange", fg = "white")
btn.place(relx= 0.5, rely = 0.5, anchor = CENTER)

label_item.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()