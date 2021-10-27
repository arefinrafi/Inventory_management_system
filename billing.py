from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import time

class BillingClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title(160*blank_space+"Inventory Management System | Developed by Arefin")
        self.root.config(bg="#fff")

        self.cart_list=[]

        #============Title===============
        self.icon_title=PhotoImage(file="images/logo111.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="#fff",anchor="w",padx="20").place(x=0,y=0,relwidth=1,height=70)
        

        #============Logout Button=======
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #============Clock================
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4D636D",fg="#fff")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #=============Product Frame============
        self.var_search=StringVar()

        MainProductFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        MainProductFrame.place(x=6,y=110,width=410,height=550)

        pTitle=Label(MainProductFrame,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        ProductFrame1=Frame(MainProductFrame,bd=2,relief=RIDGE,bg="white")
        ProductFrame1.place(x=2,y=42,width=398,height=90)

        lbl_name=Label(ProductFrame1,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        btn_showall=Button(ProductFrame1,text="Show All",command=self.show,font=("goudy old style",15),bg="#083539",fg="white",cursor="hand2").place(x=290,y=10,width=100,height=25)
        lbl_search=Label(ProductFrame1,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        ent_search=Entry(ProductFrame1,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=130,y=47,width=150,height=22)
        btn_search=Button(ProductFrame1,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=290,y=47,width=100,height=25)

        ProductFrame2=Frame(MainProductFrame,bd=3,relief=RIDGE)
        ProductFrame2.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame2,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame2,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame2,columns=("pid","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        
        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("quantity",text="Quantity")
        self.product_Table.heading("status",text="Status")

        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=60)
        self.product_Table.column("name",width=80)
        self.product_Table.column("price",width=80)
        self.product_Table.column("quantity",width=80)
        self.product_Table.column("status",width=80)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(MainProductFrame,text="Note: 'Enter 0 Quantity to remove product from the cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
        
        #======================Customer Frame============================
        self.var_cname=StringVar()
        self.var_contact=StringVar()

        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)

        #================Calculator And Cart Frame============================
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
        #================Calculator Frame============================
        self.var_cal_input=StringVar()

        CalculatorFrame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        CalculatorFrame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(CalculatorFrame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(CalculatorFrame,text='7',font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(CalculatorFrame,text='8',font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(CalculatorFrame,text='9',font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(CalculatorFrame,text='+',font=("arial",15,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(CalculatorFrame,text='4',font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(CalculatorFrame,text='5',font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(CalculatorFrame,text='6',font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(CalculatorFrame,text='-',font=("arial",15,"bold"),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)


        btn_1=Button(CalculatorFrame,text='1',font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(CalculatorFrame,text='2',font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(CalculatorFrame,text='3',font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(CalculatorFrame,text='*',font=("arial",15,"bold"),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(CalculatorFrame,text='0',font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(CalculatorFrame,text='C',font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_equal=Button(CalculatorFrame,text='=',font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(CalculatorFrame,text='/',font=("arial",15,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)


        #================Cart Frame============================
        CartFrame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        CartFrame.place(x=280,y=8,width=245,height=342)

        self.cartTitle=Label(CartFrame,text="Cart\t Total Product: [0]",font=("goudy old style",15),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)
        

        scrolly=Scrollbar(CartFrame,orient=VERTICAL)
        scrollx=Scrollbar(CartFrame,orient=HORIZONTAL)

        self.cart_Table=ttk.Treeview(CartFrame,columns=("pid","name","price","quantity"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.cart_Table.xview)
        scrolly.config(command=self.cart_Table.yview)
        
        self.cart_Table.heading("pid",text="PID")
        self.cart_Table.heading("name",text="Name")
        self.cart_Table.heading("price",text="Price")
        self.cart_Table.heading("quantity",text="Quantity")

        self.cart_Table["show"]="headings"

        self.cart_Table.column("pid",width=40)
        self.cart_Table.column("name",width=90)
        self.cart_Table.column("price",width=90)
        self.cart_Table.column("quantity",width=40)
        self.cart_Table.pack(fill=BOTH,expand=1)
        self.cart_Table.bind("<ButtonRelease-1>",self.get_data_cart)

        #================ADD Cart Widgets Frame============================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_stock=StringVar()

        CartButtonsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        CartButtonsFrame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(CartButtonsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(CartButtonsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(CartButtonsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(CartButtonsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(CartButtonsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(CartButtonsFrame,textvariable=self.var_quantity,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_inStock=Label(CartButtonsFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(CartButtonsFrame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(CartButtonsFrame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
        #===================Billing Area====================
        BillFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        BillFrame.place(x=953,y=110,width=410,height=410)

        bTitle=Label(BillFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#f44336",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(BillFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.text_bill_area=Text(BillFrame,yscrollcommand=scrolly.set)
        self.text_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.text_bill_area.yview)

        #===================Billing Buttons====================
        BillMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        BillMenuFrame.place(x=953,y=520,width=410,height=140)

        self.lbl_amount=Label(BillMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amount.place(x=2,y=5,width=150,height=70)

        self.lbl_discount=Label(BillMenuFrame,text="Discount\n[5%]",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=154,y=5,width=120,height=70)

        self.lbl_net_pay=Label(BillMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=276,y=5,width=130,height=70)

        btn_print=Button(BillMenuFrame,text="Print",font=("goudy old style",15,"bold"),cursor="hand2",bg="green",fg="white")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(BillMenuFrame,text="Clear All",font=("goudy old style",15,"bold"),cursor="hand2",bg="gray",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(BillMenuFrame,text="Generate/Save Bill",command=self.generate_bill,font=("goudy old style",15,"bold"),cursor="hand2",bg="#009688",fg="white")
        btn_generate.place(x=246,y=80,width=160,height=50)

        #==============Footer====================
        footer=Label(self.root,text="IMS-Inventory Management System | Developed By Arefin\nFor Any Technical Issue Contact: xxxxxxxxxxx",font=("times new roman",12,"bold"),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

        self.show()
        # self.bill_top()
    #====================All Functions=========================
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            # self.product_Table=ttk.Treeview(ProductFrame2,columns=("pid","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            cur.execute("select pid,name,price,quantity,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select pid,name,price,quantity,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record Found!!!",parent=self.root)


        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_quantity.set('1')

    def get_data_cart(self,ev):
        f=self.cart_Table.focus()
        content=(self.cart_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_quantity.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        

    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error','Please select product from the list',parent=self.root)
        elif self.var_quantity.get()=='':
            messagebox.showerror('Error','Quantity is Required',parent=self.root)
        elif int(self.var_quantity.get())>int(self.var_stock.get()):
            messagebox.showerror('Error','Invalid Quantity',parent=self.root)
        else:
            # price_cal=float(int(self.var_quantity.get())*float(self.var_price.get()))
            # print(price_cal)
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_quantity.get(),self.var_stock.get()]
            
            # print(self.cart_list)
            #===========Update Cart==============
            present='no'
            index_=-1
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product already present\nDo you want to Update|Remove from the Cart List",parent=self.root)
                if op==True:
                    if self.var_quantity.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_quantity.get() #Quantity
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amount=0
        self.net_pay=0
        self.discount=0

        for row in self.cart_list:
            self.bill_amount=self.bill_amount+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amount*5)/100
        self.net_pay=self.bill_amount-self.discount

        self.lbl_amount.config(text=f'Bill Amount(Tk.)\n{str(self.bill_amount)}')
        self.lbl_net_pay.config(text=f'Net Pay(Tk.)\n{str(self.net_pay)}')
        self.cartTitle.config(text=f"Cart\t Total Product: [{str(len(self.cart_list))}]")


    def show_cart(self):
        try:
            self.cart_Table.delete(*self.cart_Table.get_children())
            for row in self.cart_list:
                self.cart_Table.insert('',END,values=row)

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)

    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are Required.",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add Product to the Cart!!!",parent=self.root)
        else:
            #=========Bill Top=========
            self.bill_top()
            #=========Bill Middle=========
            self.bill_middle()
            #=========Bill Bottom=========
            self.bill_bottom()
            # pass

    def bill_top(self):
        invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        # print(invoice)
        bill_top_temp=f'''
\t\tFrootel-Inventory
\tPhone No. 01986700800, Chittagong-4223
{str("="*47)}
Customer Name: {self.var_cname.get()}
Phone No.: {self.var_contact.get()}
Bill No.: {str(invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQty\tPrice
{str("="*47)}
        '''

        self.text_bill_area.delete('1.0',END)
        self.text_bill_area.insert('1.0',bill_top_temp)


    def bill_middle(self):
        for row in self.cart_list:
            name=row[1]
            qty=row[3]
            price=str(float(row[2])*int(row[3]))
            self.text_bill_area.insert(END,"\n "+name+"\t\t\t"+qty+"\tRs."+price)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str('='*47)}
 Bill Amount\t\t\t\tTk.{self.bill_amount}
 Discount\t\t\t\tTk.{self.discount}
 Net Pay\t\t\t\tTk.{self.net_pay}
{str('='*47)}\n
        '''

        self.text_bill_area.insert(END,bill_bottom_temp)

if __name__=="__main__":
    root=Tk()
    blank_space =" "
    obj=BillingClass(root)
    root.mainloop()