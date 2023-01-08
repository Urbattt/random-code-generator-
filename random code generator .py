from tkinter import*
import random
root=Tk()
root.geometry("500x500")
root.title("code generator")

display=Label(root)

def randomizer():
    alpha_list=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    random_no1=random.randint(0,25)
    random_no2=random.randint(0,25)
    random_no3=random.randint(0,25)
    random_no4=random.randint(0,25)
    random_no5=random.randint(0,25)
    
    random_alpha1=alpha_list[random_no1]
    random_alpha2=alpha_list[random_no2]
    random_alpha3=alpha_list[random_no3]
    random_alpha4=alpha_list[random_no4]
    random_alpha5=alpha_list[random_no5]
    display["text"]= str(random_alpha1)+str(random_alpha2)+str(random_alpha3)+str(random_alpha4)+str(random_alpha5)

btn1 = Button(root, text="random code", command=randomizer)
btn1.place(relx=0.5, rely =0.5, anchor=CENTER)
display.place(relx=0.5,rely=0.6, anchor=CENTER)
    
    
root.mainloop()