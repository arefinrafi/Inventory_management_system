from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import ttk,messagebox
import os,time

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title(160*blank_space+"Inventory Management System | Developed by Arefin")
        self.root.config(bg="#fff")

        #============Title===============
        self.icon_title=PhotoImage(file="images/logo111.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="#fff",anchor="w",padx="20").place(x=0,y=0,relwidth=1,height=70)
        

        #============Logout Button=======
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #============Clock================
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4D636D",fg="#fff")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #============Left Menu============
        self.Menulogo=Image.open("images/menulogo.png")
        self.Menulogo=self.Menulogo.resize((200,200),Image.ANTIALIAS)
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)

        Leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="#fff")
        Leftmenu.place(x=0,y=102,height=565,width=200)
        
        lbl_menulogo=Label(Leftmenu,image=self.Menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        lbl_menu=Label(Leftmenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        
        self.icon_side=PhotoImage(file="images/arrow1.png")
        btn_employee=Button(Leftmenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#fff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(Leftmenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#fff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(Leftmenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#fff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(Leftmenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#fff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(Leftmenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#fff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(Leftmenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#fff",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #============Content================
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="#fff",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="#fff",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="#fff",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_products=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="#fff",font=("goudy old style",20,"bold"))
        self.lbl_products.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="#fff",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)


        #============Footer================
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By CodFalcon\nFor any technical issue contact: xxxxx-xxxxxx",font=("times new roman",12),bg="#4D636D",fg="#fff").pack(side=BOTTOM,fill=X)

        self.update_content()
#================================================================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_products.config(text=f"Total Products\n[ {str(len(product))} ]")

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n[ {str(len(supplier))} ]")

            cur.execute("select * from maincategory")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(category))} ]")

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")
            Bill=len(os.listdir('Bill'))
            self.lbl_sales.config(text=f'Total Sales [{str(Bill)}]')


            time_=time.strftime("%I:%M:%S") #H Showing 24 hour, I Showing 12hour
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    blank_space =" "
    obj=IMS(root)
    root.mainloop()