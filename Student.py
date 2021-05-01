from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        
        title = Label(self.root,text="STUDENT MANAGEMENT SYSTEM",bd=10, relief=RAISED,font=("times new roman",20,"bold"),bg="yellow",fg="green")
        title.pack(side=TOP,fill=X)

#--------all variables-----------
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

#   -------Manage Frame----------
        Manage_Frame = Frame(self.root,border=5,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=80,width=490,height=600)


        m_title=Label(Manage_Frame,text="manage students",bg='crimson',fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_roll=Label(Manage_Frame,text="Roll no:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')

        txt_Roll=Entry(Manage_Frame,bg='white',textvariable=self.Roll_No_var,font=("times new roman",20,"bold"),border=5,relief=RIDGE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        lbl_name=Label(Manage_Frame,text="Name:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')

        txt_name=Entry(Manage_Frame,bg='white',textvariable=self.name_var,font=("times new roman",20,"bold"),border=5,relief=RIDGE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

        lbl_Email=Label(Manage_Frame,text="Email:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky='w')

        txt_Email=Entry(Manage_Frame,bg='white',textvariable=self.email_var,font=("times new roman",20,"bold"),border=5,relief=RIDGE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky='w')

        lbl_Gender=Label(Manage_Frame,text="Gender:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')
 
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",15,"bold"),state="readonly",width=27)
        combo_gender['values']=('male','female','other')
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky='w')

        lbl_contact=Label(Manage_Frame,text="Contact:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky='w')

        txt_contact=Entry(Manage_Frame,bg='white',textvariable=self.contact_var,font=("times new roman",20,"bold"),border=5,relief=RIDGE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')

        lbl_dob=Label(Manage_Frame,text="D.O.B:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky='w')

        txt_dob=Entry(Manage_Frame,bg='white',textvariable=self.dob_var,font=("times new roman",20,"bold"),border=5,relief=RIDGE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky='w')
        
        lbl_address=Label(Manage_Frame,text="Address:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky='w')

        self.txt_address=Text(Manage_Frame,width=48,relief=RIDGE,height=3,font=("times new roman",10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky='w')

#---------Button Frame-----------
        btn_Frame=Frame(Manage_Frame,relief=RIDGE,bd=4,bg='crimson')
        btn_Frame.place(x=10,y=500,width=450)

        Addbtn=Button(btn_Frame,text='ADD',command=self.add_students,width=10).grid(row=0,column=0,padx=20,pady=20)
        updatebtn=Button(btn_Frame,text='UPDATE',command=self.update_data,width=10).grid(row=0,column=1,padx=20,pady=20)
        deletebtn=Button(btn_Frame,text='DELETE',command=self.delete_data,width=10).grid(row=0,column=2,padx=10,pady=20)
        clearbtn=Button(btn_Frame,text='CLEAR',command=self.clear,width=10).grid(row=0,column=3,padx=10,pady=20)



#   -------Detail Frame----------
        Detail_Frame = Frame(self.root,border=5,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=550,y=80,width=750,height=600)
        
        lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky='w')

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("times new roman",15,"bold"),state="readonly",width=10)
        combo_search['values']=('Roll_no','Name','Contact')
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky='w')

        txt_search=Entry(Detail_Frame,bg='white',textvariable=self.search_txt,font=("times new roman",20,"bold"),border=5,relief=RIDGE,width=10)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')

        searchbtn=Button(Detail_Frame,text='Search',command=self.search_data,width=10).grid(row=0,column=3,padx=10,pady=20)
        showallbtn=Button(Detail_Frame,text='showall',command=self.fetch_data,width=10).grid(row=0,column=4,padx=10,pady=20)




#------------Table Frame-------------------
        
        Table_Frame = Frame(Detail_Frame ,border=5,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=20,y=80,width=700,height=480)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=('roll','name','email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading('roll', text="Roll No" )
        self.Student_table.heading('name', text="Name" )
        self.Student_table.heading('email', text="Email" )
        self.Student_table.heading('gender', text="Gender" )
        self.Student_table.heading('contact', text="Contact" )
        self.Student_table.heading('dob', text="D.O.B" )
        self.Student_table.heading('address', text="Address" )

        self.Student_table['show']='headings'

        self.Student_table.column("roll",width=80)
        self.Student_table.column("name",width=150)
        self.Student_table.column("email",width=150)
        self.Student_table.column("gender",width=150)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("address",width=200)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind('<ButtonRelease-1>',self.get_cursor)

        self.fetch_data()


    def add_students(self):
        if   self.Roll_No_var.get()=="" or self.name_var.get()=="":
                messagebox.showerror("Error","All fields required")
        else:        
               con=pymysql.connect(host='localhost',user='root',password='',database='stm')
               cur=con.cursor()
               cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                               self.name_var.get(), 
                                                                               self.email_var.get(),
                                                                               self.gender_var.get(),
                                                                               self.contact_var.get(),
                                                                               self.dob_var.get(),
                                                                               self.txt_address.get('1.0',END)
                                                                               ))                                                        
               con.commit()
               self.fetch_data()
               self.clear()
               con.close()
    def fetch_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()   
        cur.execute("select *from students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()                
    def clear(self):
        self.Roll_No_var.set('')
        self.name_var.set('')
        self.email_var.set('') 
        self.dob_var.set('') 
        self.contact_var.set('') 
        self.gender_var.set('') 
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        content=self.Student_table.item(cursor_row)
        row=content['values']  
        self.Roll_No_var.set(row[0])  
        self.name_var.set(row[1]) 
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[6])


    def update_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                               self.name_var.get(), 
                                                                               self.email_var.get(),
                                                                               self.gender_var.get(),
                                                                               self.contact_var.get(),
                                                                               self.dob_var.get(),
                                                                               self.txt_address.get('1.0',END),
                                                                               self.Roll_No_var.get()
                                                                               ))                                                        
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        

    def delete_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()   
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        self.fetch_data()
        self.clear()
        con.close() 
        

    def search_data(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='stm')
        cur=con.cursor()   
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close() 







root=Tk()
ob=Student(root)
root.mainloop()
