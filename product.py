from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by Arefin")
        self.root.config(bg="#fff") #33bbf9
        self.root.focus_force()
        #=======================================

        #=============All Variables=============
        self.var_pid=StringVar()
        self.var_category=StringVar()
        self.var_supplier=StringVar()
        self.category_list=[]
        self.supplier_list=[]
        self.fetch_category_supplier()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()

        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()
        
        #=============Left Frame=============

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)

        #===========Title========================
        title=Label(product_Frame,text="Manage Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="#fff").pack(side=TOP,fill=X)

        #===========Label========================
        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_product_name=Label(product_Frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_quantity=Label(product_Frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)

        #===========Entry Box========================
        cmb_category=ttk.Combobox(product_Frame,textvariable=self.var_category,values=self.category_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_category.place(x=150,y=60,width=200)
        cmb_category.current(0)

        cmb_supplier=ttk.Combobox(product_Frame,textvariable=self.var_supplier,values=self.supplier_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_supplier.place(x=150,y=110,width=200)
        cmb_supplier.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_quantity=Entry(product_Frame,textvariable=self.var_quantity,font=("goudy old style",15),bg='lightyellow').place(x=150,y=260,width=200)

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

        #===============Button==================
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="#fff",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="#fff",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="#fff",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607b8d",fg="#fff",cursor="hand2").place(x=340,y=400,width=100,height=40)

        #=============Right Frame=============
        #=========Search Frame==================
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="#fff")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #=========Options=======================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10,width=210,height=28)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="#fff",cursor="hand2").place(x=420,y=10,width=150,height=28)


        #============Employee Details==============
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(p_frame,columns=("pid","Category","Supplier","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        
        self.ProductTable.heading("pid",text="Pro ID")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("quantity",text="Quantity")
        self.ProductTable.heading("status",text="Status")

        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("quantity",width=100)
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        
    #=========================================================

    def fetch_category_supplier(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            cur.execute("Select name from maincategory")
            cat=cur.fetchall()
            self.category_list.append("Empty")
            if len(cat)>0:
                del self.category_list[:]
                self.category_list.append("Select")
                for i in cat:
                    self.category_list.append(i[0])

            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            self.supplier_list.append("Empty")
            if len(sup)>0:
                del self.supplier_list[:]
                self.supplier_list.append("Select")
                for i in sup:
                    self.supplier_list.append(i[0])

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_category.get()=="Select" or self.var_category.get()=="Empty" or self.var_supplier.get()=="Select" or self.var_supplier.get()=="Empty" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,quantity,status) values(?,?,?,?,?,?)",(
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added Successfully",parent=self.root)
                    self.show()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)


    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pid.set(row[0]),
        self.var_category.set(row[1]),
        self.var_supplier.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_quantity.set(row[5]),
        self.var_status.set(row[6]),

    #=========================================================
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select product from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,quantity=?,status=? where pid=?",(
                        
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),

                        self.var_pid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Successfully",parent=self.root)
                    self.show()

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()

        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select product from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()


        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)


    def clear(self):
        self.var_pid.set("")
        self.var_category.set("Select")
        self.var_supplier.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_status.set("Active")

        self.var_searchtext.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtext.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record Found!!!",parent=self.root)


        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()