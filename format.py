import Javan as j
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from datetime import date
from datetime import datetime
import time

win=tk.Tk()
win.title("نرم افزارانبارداری جوان")
win.resizable(False, False)

window_height = 750
window_width = 1528

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

canvas = tk.Canvas(width=750, height=1528, bg='#FFA500')
canvas.pack(expand=tk.YES, fill=tk.BOTH)
logo = tk.PhotoImage(file='s.png')
canvas.create_image(0, 0,image=logo, anchor=tk.NW)

tk.Label(win,text=':تاریخ',bg='#000080',width=10,height=4,font="#2526").place(x=1360,y=580)
lbdate = tk.Label(win,text=date.today(),bg='#FFA500',width=10,height=1,font="#2526")
lbdate.place(x=1242,y=580)

def timeLable():
    time_lable = tk.Label(win,text=time.strftime("%H:%M:%S  "),font="#2526",anchor=tk.E,bg='#FFA500',width=10,height=2)
    time_lable.place(x=1242,y=623)
    win.after(1000,timeLable)
win.after(1000,timeLable)

lbtext = tk.Label(win,text="نرم افزارانبارداری جوان",font="#4545",bg="#FFA500") 
lbtext.place(x=20,y=700)

menubar=tk.Menu(win, bd=5, background="#20232A")
menubar.configure(background="blue")
win.config(menu=menubar)

tarif =  tk.Menu(tearoff=0)
people = tk.Menu(tearoff=0)
gozatesh = tk.Menu(tearoff=0)
sayeramliat = tk.Menu(tearoff=0)
setting = tk.Menu(tearoff=0)
help_me = tk.Menu(tearoff=0)
darbare = tk.Menu(tearoff=0)

def creat_list(class_name,win_name,row,column):
    s = class_name.read_file()
    val = tk.StringVar(value=s)
    lst = tk.Listbox(win_name,listvariable=val,justify='right')
    lst.grid(row=row,column=column)
    return lst,s

def creat_Combobox(class_name,win_name,row,column):
    s = class_name.read_file()
    val = tk.StringVar()
    lst = ttk.Combobox(win_name,textvariable=val,justify='right')

    lst['values'] = s
   
    lst['state'] = 'readonly'
    lst.grid(row=row,column=column)
    return lst,s

def form_kala():
    win_kala = tk.Toplevel()
    win_kala.title("تعریف کالا")
    win_kala.geometry("500x300+520+280")
    win_kala.configure(bg='#FFA500')
        
    tk.Label(win_kala,text="نام کالا",bg="#FFA500").grid(row=0,column=0)
    entname = tk.Entry(win_kala)
    entname.grid(row=0,column=1)
    
    tk.Label(win_kala,text="کد کالا",bg="#FFA500").place(x=210,y=0)
    entcode_kala = tk.Entry(win_kala)#
    entcode_kala.place(x=265,y=2)
    
    tk.Label(win_kala,text="واحد اول",bg="#FFA500").grid(row=2,column=0)
    entunit_1 = tk.Entry(win_kala)
    entunit_1.grid(row=2,column=1)
    
    tk.Label(win_kala,text="واحد دوم",bg="#FFA500").place(x=210,y=20)
    entunit_2 = tk.Entry(win_kala)#
    entunit_2.place(x=265,y=22)
    
    tk.Label(win_kala,text="نسبت واحد",bg="#FFA500").grid(row=4,column=0)
    entn_unit = tk.Entry(win_kala)
    entn_unit.grid(row=4,column=1)
    
    tk.Label(win_kala,text="نوع",bg="#FFA500").place(x=210,y=40)
    enttype_kala = tk.Entry(win_kala)#
    enttype_kala.place(x=265,y=42)
    
    tk.Label(win_kala,text="شرح کالا",bg="#FFA500").grid(row=6,column=0)
    entdescription = tk.Entry(win_kala)
    entdescription.grid(row=6,column=1)
        
    tk.Label(win_kala,text="تعداد",bg="#FFA500").place(x=210,y=60)
    entcount = tk.Entry(win_kala)
    entcount.place(x=265,y=62)
    
    def back():
        win_kala.destroy()

    back = tk.Button(win_kala,text="بازگشت",command=back,font="#2526")
    back.place(x=240,y=200)
    
    def save():
        name = entname.get()
        count = int(entcount.get())
        unit_1 = entunit_1.get()
        unit_2 = entunit_2.get()
        type_kala = enttype_kala.get()
        description = entdescription.get()
        try:
            code_kala = int(entcode_kala.get())
            n_unit = int(entn_unit.get())
            
            kala = j.Kala(name,code_kala,unit_1,unit_2,n_unit,type_kala,description,count)
            kala.save()
            tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
            win_kala.destroy()
        except:
            tk.messagebox.showinfo('خطا','ثبت با خطا مواجه شد')

    save = tk.Button(win_kala,text="ذخیره",command=save,font="#2526")
    save.place(x=183,y=200)
    


def edit_kala():
    win_kala = tk.Toplevel()
    win_kala.title("ویرایش کالا")
    win_kala.geometry("500x300+520+280")
    win_kala.configure(bg='#FFA500')
    
    tk.Label(win_kala,text="لیست کالا ها",bg="#FFA500").grid(row=0,column=0)
    list_k,s = creat_list(j.Kala, win_kala, 1, 0)
    
    tk.Label(win_kala,text="نام کالا",bg="#FFA500").place(x=320,y=20)
    
    txtname = tk.StringVar(value='###')
    entname = tk.Entry(win_kala,justify='right',textvariable=txtname) 
    entname.place(x=185,y=20)
    
    tk.Label(win_kala,text="کد کالا",bg="#FFA500").place(x=320,y=40)
    
    txtcode_kala = tk.StringVar(value='###')
    entcode_kala=tk.Entry(win_kala,justify='right',textvariable=txtcode_kala)
    entcode_kala.place(x=185,y=40)
    
    tk.Label(win_kala,text="واحد اول",bg="#FFA500").place(x=320,y=60)
    
    txtunit_1 = tk.StringVar(value='###')
    entunit_1 = tk.Entry(win_kala,justify='right',textvariable=txtunit_1)
    entunit_1.place(x=185,y=60)
    
    tk.Label(win_kala,text="واحد دوم",bg='#FFA500').place(x=320,y=80)
    
    txtunit_2 = tk.StringVar(value='###')
    entunit_2 = tk.Entry(win_kala,justify='right',textvariable=txtunit_2)
    entunit_2.place(x=185,y=80)
    
    tk.Label(win_kala,text="نسبت واحد",bg='#FFA500').place(x=320,y=100)
    
    txtn_unit = tk.StringVar(value='###')
    entn_unit = tk.Entry(win_kala,justify='right',textvariable=txtn_unit)
    entn_unit.place(x=185,y=100)
    
    tk.Label(win_kala,text=" تعداد",bg='#FFA500').place(x=320,y=120)
    
    txtcount = tk.StringVar(value='###')
    entcount = tk.Entry(win_kala,justify='right',textvariable=txtcount)
    entcount.place(x=185,y=120)
    
    tk.Label(win_kala,text="نوع",bg='#FFA500').place(x=320,y=140)
    
    txttype_kala = tk.StringVar(value='###')
    enttype_kala = tk.Entry(win_kala,justify='right',textvariable=txttype_kala)
    enttype_kala.place(x=185,y=140)
    
    tk.Label(win_kala,text="شرح کالا",bg='#FFA500').place(x=320,y=160)
    
    txtdescription = tk.StringVar(value='###')
    entdescription = tk.Entry(win_kala,justify='right',textvariable=txtdescription)
    entdescription.place(x=185,y=160)
    
    item=(0,)
    
    def back():
        win_kala.destroy()

    back = tk.Button(win_kala,text="بازگشت",command=back,font="#2526")
    back.place(x=261,y=230)
    
    def save_edit():
        name = entname.get()
        unit_1 = entunit_1.get()
        unit_2 = entunit_2.get()
        type_kala = enttype_kala.get()
        description = entdescription.get()
        try:
            code_kala = int(entcode_kala.get())
            n_unit = int(entn_unit.get())
            count = int(entcount.get())
            kala = j.Kala(name,code_kala,unit_1,unit_2,n_unit,type_kala,description,count)
            kala.save()
            tk.messagebox.showinfo('پیام موفقیت','ویرایش با موفقیت انجام شد')
            win_kala.destroy()
        except:
            tk.messagebox.showinfo('خطا','ثبت با خطا مواجه شد')

        
    save = tk.Button(win_kala,text="ویرایش",command=save_edit,font="#2526")
    save.place(x=200,y=230)
    
    def flistselect(event):
        global item
        try:
            new_item = list_k.curselection()
            
            if new_item:
                item=new_item
                txtname.set(s[item[0]].name)
                txtcode_kala.set(s[item[0]].code_kala)
                txtunit_1.set(s[item[0]].unit_1)
                txtunit_2.set(s[item[0]].unit_2)
                txtn_unit.set(s[item[0]].n_unit)
                txtcount.set(s[item[0]].count)
                txttype_kala.set(s[item[0]].type_kala)
                txtdescription.set(s[item[0]].description)  
        except:
            pass
        
    list_k.bind('<<ListboxSelect>>',flistselect)  

def delete_kala():
    win_kala=tk.Toplevel()
    win_kala.title("حدف کالا")
    win_kala.geometry('500x300+400+200')
    win_kala.configure(bg='#FFA500')
    tk.Label(win_kala,text="لیست کالا ها",bg='#FFA500').grid(row=0,column=0)
    list_k,s=creat_list(j.Kala, win_kala, 1, 0)
        
    tk.Label(win_kala,text=":نام کالا",bg="#FFA500").place(x=250,y=20)
    lbname = tk.Label(win_kala,text='###',bg='#FFA500')
    lbname.place(x=150,y=20)
    
    tk.Label(win_kala,text=":کد کالا",bg="#FFA500").place(x=250,y=40)
    lbcode_kala = tk.Label(win_kala,text='###',bg='#FFA500')#
    lbcode_kala.place(x=150,y=40)
    
    tk.Label(win_kala,text=":واحد اول",bg="#FFA500").place(x=250,y=60)
    lbunit_1 = tk.Label(win_kala,text='###',bg='#FFA500')
    lbunit_1.place(x=150,y=60)
    
    tk.Label(win_kala,text=":واحد دوم",bg="#FFA500").place(x=250,y=80)
    lbunit_2 = tk.Label(win_kala,text='###',bg='#FFA500')#
    lbunit_2.place(x=150,y=80)
    
    tk.Label(win_kala,text=":نسبت واحد",bg="#FFA500").place(x=250,y=100)
    lbn_unit = tk.Label(win_kala,text='###',bg='#FFA500')
    lbn_unit.place(x=150,y=100)
    
    tk.Label(win_kala,text=":تعداد",bg="#FFA500").place(x=250,y=120)
    lbcount = tk.Label(win_kala,text='###',bg='#FFA500')
    lbcount.place(x=150,y=120)
    
    tk.Label(win_kala,text=":نوع",bg="#FFA500").place(x=250,y=140)
    lbtype_kala = tk.Label(win_kala,text='###',bg='#FFA500')#
    lbtype_kala.place(x=150,y=140)
    
    tk.Label(win_kala,text=":شرح کالا",bg="#FFA500").place(x=250,y=160)
    lbdescription = tk.Label(win_kala,text='###',bg='#FFA500')
    lbdescription.place(x=150,y=160)
    item=-1
    
    def delete():
        try:
            
            global item
            s[item[0]].delete()
            tk.messagebox.showinfo('پیام موفقیت','حذف با موفقیت انجام شد')
            win_kala.destroy()
        except:
            tk.messagebox.showerror('خطا','حذف با خطا مواجعه شد')
            win_kala.destroy()
    
    delete = tk.Button(win_kala,text="  حذف ",command=delete,font="#2526")
    delete.place(x=198,y=200)

    def back():
        win_kala.destroy()

    back = tk.Button(win_kala,text="بازگشت",command=back,font="#2526")
    back.place(x=268,y=200)
    
    def flistselect(event):
        global item
        item = list_k.curselection()
        
        lbname.config(text=s[item[0]].name)
        lbcode_kala.config(text=s[item[0]].code_kala)
        lbunit_1.config(text=s[item[0]].unit_1)
        lbunit_2.config(text=s[item[0]].unit_2)
        lbn_unit.config(text=s[item[0]].n_unit)
        lbcount.config(text=s[item[0]].count)
        lbtype_kala.config(text=s[item[0]].type_kala)
        lbdescription.config(text=s[item[0]].description)

        
    list_k.bind('<<ListboxSelect>>',flistselect)
    
submenu = Menu(tarif, tearoff=0)
submenu.add_command(label="تعریف کالا",accelerator="F1",command=form_kala)
form_kala = tk.Button(win,text="تعریف کالا",command=form_kala,bg='#FFA500',width=13,height=2,font="#2526")
form_kala.place(x=1380,y=3)

submenu.add_command(label="ویرایش کالا",accelerator="Crtl+E",command=edit_kala)
submenu.add_command(label="حدف کالا",command=delete_kala)
tarif.add_cascade(label="       کالا",menu=submenu)
tarif.add_separator()

def form_people():
    win_people = tk.Toplevel()
    win_people.title("تعریف مشتری")
    win_people.geometry("420x280+520+280")
    win_people.configure(bg='#FFA500')
    
    tk.Label(win_people,text="نام",bg="#FFA500").grid(row=0,column=0)
    entferst_name = tk.Entry(win_people)
    entferst_name.grid(row=0,column=1)
    
    tk.Label(win_people,text="نام خانوادگی",bg="#FFA500").place(x=210,y=0)
    entlast_name = tk.Entry(win_people)
    entlast_name.place(x=280,y=0)
    
    tk.Label(win_people,text="قرارداد",bg="#FFA500").grid(row=2,column=0)
    entcontract = tk.Entry(win_people)
    entcontract.grid(row=2,column=1)
    
    tk.Label(win_people,text="تلفن ثابت",bg="#FFA500").place(x=220,y=20)
    enttel_1 = tk.Entry(win_people)
    enttel_1.place(x=280,y=20)
    
    tk.Label(win_people,text="تلفن شخصی",bg="#FFA500").grid(row=4,column=0)
    enttel_2 = tk.Entry(win_people)
    enttel_2.grid(row=4,column=1)
    
    tk.Label(win_people,text="آدرس",bg="#FFA500").place(x=228,y=40)
    entaddres = tk.Entry(win_people)
    entaddres.place(x=280,y=40)
    
    tk.Label(win_people,text="کد اشتراک",bg="#FFA500").grid(row=6,column=0)
    entcode = tk.Entry(win_people)
    entcode.grid(row=6,column=1)
    
    def back():
        win_people.destroy()

    back = tk.Button(win_people,text="بازگشت",command=back,font="#2526")
    back.place(x=246,y=200)
    
    def save():
        ferst_name = entferst_name.get()
        last_name = entlast_name.get()
        addres = entaddres.get()
        contract = entcontract.get()
        try:
            tel_1 = int(enttel_1.get())
            tel_2 = int(enttel_2.get())
            code = int(entcode.get())
            customer = j.Customer(ferst_name,last_name,tel_1,tel_2,addres,contract,code)
            customer.save()
            tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
            win_people.destroy()
        except:
            tk.messagebox.showinfo('خطا','این فیلد باید عدد باشد')
        
    save = tk.Button(win_people,text="ذخیره",command=save,font="#2526")
    save.place(x=190,y=200)


def edit_people():
    win_people = tk.Toplevel()
    win_people.title("ویرایش مشتری")
    win_people.geometry("400x270+520+280")
    win_people.configure(bg='#FFA500')
    tk.Label(win_people,text="لیست مشتری",bg="#FFA500").grid(row=0,column=0)
    list_cus,s = creat_list(j.Customer, win_people, 1, 0)
    
    tk.Label(win_people,text="نام ",bg="#FFA500").place(x=320,y=20)
    
    txtferst_name = tk.StringVar(value='###')
    entferst_name = tk.Entry(win_people,justify='right',textvariable=txtferst_name) 
    entferst_name.place(x=185,y=20)
    
    tk.Label(win_people,text="نام خانوادگی",bg="#FFA500").place(x=320,y=40)
    
    txtlast_name = tk.StringVar(value='###')
    entlast_name = tk.Entry(win_people,justify='right',textvariable=txtlast_name)
    entlast_name.place(x=185,y=40)
    
    tk.Label(win_people,text="قرارداد",bg="#FFA500").place(x=320,y=60)
    
    txtcontract = tk.StringVar(value='###')
    entcontract = tk.Entry(win_people,justify='right',textvariable=txtcontract)
    entcontract.place(x=185,y=60)
    
    tk.Label(win_people,text="تلفن ثابت",bg='#FFA500').place(x=320,y=80)
    
    txttel_1 = tk.StringVar(value='###')
    enttel_1 = tk.Entry(win_people,justify='right',textvariable=txttel_1)
    enttel_1.place(x=185,y=80)
    
    tk.Label(win_people,text="تلفن شخصی",bg='#FFA500').place(x=320,y=100)
    
    txttel_2 = tk.StringVar(value='###')
    enttel_2 = tk.Entry(win_people,justify='right',textvariable=txttel_2)
    enttel_2.place(x=185,y=100)
    
    tk.Label(win_people,text="آدرس",bg='#FFA500').place(x=320,y=120)
    
    txtaddres = tk.StringVar(value='###')
    entaddres = tk.Entry(win_people,justify='right',textvariable=txtaddres)
    entaddres.place(x=185,y=120)
    
    tk.Label(win_people,text=" کد اشتراک",bg='#FFA500').place(x=320,y=140)
    
    txtcode = tk.StringVar(value='###')
    entcode = tk.Entry(win_people,justify='right',textvariable=txtcode)
    entcode.place(x=185,y=140)
    item=(0,)
    
    def back():
        win_people.destroy()

    back = tk.Button(win_people,text="بازگشت",command=back,font="#2526")
    back.place(x=260,y=210)
    
    def save_edit():
        ferst_name = entferst_name.get()
        last_name = entlast_name.get()
        addres = entaddres.get()
        contract = entcontract.get()
        try:
            code = int(entcode.get())
            tel_1 = int(enttel_1.get())
            tel_2 = int(enttel_2.get())
            
            customer = j.Customer(ferst_name,last_name,tel_1,tel_2,addres,contract,code)
            customer.save()
            tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
            win_people.destroy()
        except:
            tk.messagebox.showinfo('خطا','ثبت با خطا مواجه شد')
        
    save = tk.Button(win_people,text="ویرایش",command=save_edit,font="#2526")
    save.place(x=198,y=210)
    
    def flistselect(event):
        global item
        try:
            new_item = list_cus.curselection()
            
            if new_item:
                item=new_item
                txtferst_name.set(s[item[0]].ferst_name)
                txtlast_name.set(s[item[0]].last_name)
                txtcontract.set(s[item[0]].conteract)
                txttel_1.set(s[item[0]].tel_1)
                txttel_2.set(s[item[0]].tel_2)
                txtaddres.set(s[item[0]].addres)
                txtcode.set(s[item[0]].code)
        except:
           pass
        
    list_cus.bind('<<ListboxSelect>>',flistselect)    


def delete_people():
    win_people = tk.Toplevel()
    win_people.title("حدف مشتری")
    win_people.geometry('380x300+400+200')
    win_people.configure(bg='#FFA500')
    
    tk.Label(win_people,text="لیست مشتری ها ",bg='#FFA500').grid(row=0,column=0)
    list_cut,s=creat_list(j.Customer, win_people, 1, 0)
    
    tk.Label(win_people,text="  :نام ",bg="#FFA500").place(x=280,y=20)
    lbferst_name = tk.Label(win_people,bg="#FFA500")
    lbferst_name.place(x=150,y=20)
    
    tk.Label(win_people,text=":نام خانوادگی",bg="#FFA500").place(x=280,y=40)
    lblast_name = tk.Label(win_people,bg="#FFA500")
    lblast_name.place(x=150,y=40)
    
    tk.Label(win_people,text=":کد اشتراک",bg="#FFA500").place(x=280,y=60)
    lbcode = tk.Label(win_people,bg="#FFA500")
    lbcode.place(x=150,y=60)
    
    tk.Label(win_people,text=":تلفن ثابت",bg="#FFA500").place(x=280,y=80)
    lbtel_1 = tk.Label(win_people,bg="#FFA500")
    lbtel_1.place(x=150,y=80)
    
    tk.Label(win_people,text=":تلفن شخصی",bg="#FFA500").place(x=280,y=100)
    lbtel_2 = tk.Label(win_people,bg="#FFA500")
    lbtel_2.place(x=150,y=100)
    
    tk.Label(win_people,text=":آدرس",bg="#FFA500").place(x=280,y=120)
    lbaddres = tk.Label(win_people,bg="#FFA500")
    lbaddres.place(x=130,y=120)
    
    tk.Label(win_people,text=":قرارداد",bg="#FFA500").place(x=280,y=140)
    lbconteract = tk.Label(win_people,bg="#FFA500")
    lbconteract.place(x=150,y=140)
    item=-1
    
    def delete():
        try:
            
            global item
            s[item[0]].delete()
            tk.messagebox.showinfo('پیام موفقیت','حذف با موفقیت انجام شد')
            win_people.destroy()
        except:
            tk.messagebox.showerror('خطا','حذف با خطا مواجعه شد')
            win_people.destroy()
    
    save = tk.Button(win_people,text='حذف',command=delete, font="#2526")
    save.place(x=189,y=190)

    def back():
        win_people.destroy()

    back = tk.Button(win_people,text="بازگشت",command=back,font="#2526")
    back.place(x=240,y=190)
    
    def flistselect(event):
        global item
        item = list_cut.curselection()
        
        lbferst_name.config(text=s[item[0]].ferst_name)
        lblast_name.config(text=s[item[0]].last_name)
        lbconteract.config(text=s[item[0]].conteract)
        lbtel_1.config(text=s[item[0]].tel_1)
        lbtel_2.config(text=s[item[0]].tel_2)
        lbaddres.config(text=s[item[0]].addres)
        lbcode.config(text=s[item[0]].code)

    list_cut.bind('<<ListboxSelect>>',flistselect)  
    
submenu = Menu(tarif, tearoff=0)
submenu.add_command(label="تعریف اشخاص",accelerator="F2",command=form_people)
form_people = tk.Button(win,text="تعریف مشتری",command=form_people,bg='#FFA500',width=13,height=2,font="#2526")
form_people.place(x=1380,y=58)

submenu.add_command(label="ویرایش اشخاص",command=edit_people)
submenu.add_command(label="حدف اشخاص",command=delete_people)
tarif.add_cascade(label="       اشخاص",menu=submenu)
tarif.add_separator()


def form_store():
    win_store = tk.Toplevel()
    win_store.title("تعریف انبار")
    win_store.geometry("400x270+520+280")
    win_store.configure(bg='#FFA500')
    
    tk.Label(win_store,text="نام انبار",bg='#FFA500').grid(row=0,column=0)
    entname = tk.Entry(win_store)
    entname.grid(row=0,column=1)
    
    tk.Label(win_store,text="شماره انبار",bg='#FFA500').place(x=205,y=0)
    entcode_store = tk.Entry(win_store)
    entcode_store.place(x=265,y=0)
    
    tk.Label(win_store,text="آدرس",bg='#FFA500').grid(row=2,column=0)
    entaddres_store = tk.Entry(win_store)
    entaddres_store.grid(row=2,column=1)
    
    tk.Label(win_store,text="تلفن",bg='#FFA500').place(x=225,y=20)
    enttel_store = tk.Entry(win_store)
    enttel_store.place(x=265,y=20)
    
    tk.Label(win_store,text="نوع کالا",bg='#FFA500').grid(row=4,column=0)
    enttype_store = tk.Entry(win_store)
    enttype_store.grid(row=4,column=1)
    
    def back():
        win_store.destroy()
        
    back = tk.Button(win_store,text="بازگشت",command=back,font="#2526")
    back.place(x=253,y=190)
    
    def save():
        name = entname.get()
        addres_store = entaddres_store.get() 
        type_store = enttype_store.get()
        try:
            code_store = int(entcode_store.get())
            tel_store = int(enttel_store.get())
            
            store = j.Store(name, code_store, addres_store, tel_store, type_store)
            store.save()
            tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
            win_store.destroy()
        except:
            tk.messagebox.showerror('خطا','ثبت با خطا مواجعه شد')

    save = tk.Button(win_store,text="ذخیره",command=save,font="#2526")
    save.place(x=200,y=190)
    

def edit_store():
    win_store = tk.Toplevel()
    win_store.title("ویرایش انبار")
    win_store.geometry('500x300+400+200')
    win_store.configure(bg='#EA4CED')
    tk.Label(win_store,text="لیست انبار ها",bg='#FFA500').grid(row=0,column=0)
    list_s,s=creat_list(j.Store, win_store, 1, 0)
    
    tk.Label(win_store,text="نام انبار",bg="#FFA500").place(x=320,y=20)
    
    txtname = tk.StringVar(value='###')
    entname = tk.Entry(win_store,justify='right',textvariable=txtname) 
    entname.place(x=185,y=20)
    
    tk.Label(win_store,text="کد انبار",bg="#FFA500").place(x=320,y=40)
    
    txtcode_store = tk.StringVar(value='###')
    entcode_store = tk.Entry(win_store,justify='right',textvariable=txtcode_store)
    entcode_store.place(x=185,y=40)
    
    tk.Label(win_store,text="آدرس",bg="#FFA500").place(x=320,y=60)
    
    txtaddres_store = tk.StringVar(value='###')
    entaddres_store = tk.Entry(win_store,justify='right',textvariable=txtaddres_store)
    entaddres_store.place(x=185,y=60)
    
    tk.Label(win_store,text="تلفن ثابت",bg='#FFA500').place(x=320,y=80)
    
    txttel_store = tk.StringVar(value='###')
    enttel_store = tk.Entry(win_store,justify='right',textvariable=txttel_store)
    enttel_store.place(x=185,y=80)
    
    tk.Label(win_store,text="نوع کالای انبار",bg='#FFA500').place(x=320,y=100)
    
    txttype_store = tk.StringVar(value='###')
    enttype_store = tk.Entry(win_store,justify='right',textvariable=txttype_store)
    enttype_store.place(x=185,y=100)
    item=(0,)
    
    def back():
        win_store.destroy()
              
    back = tk.Button(win_store,text="بازگشت",command=back,font="#2526")
    back.place(x=253,y=190)
    
    def save():
        name = entname.get()
        addres_store = entaddres_store.get() 
        type_store = enttype_store.get()
        try:
            code_store = int(entcode_store.get())
            tel_store = int(enttel_store.get())
            
            store = j.Store(name, code_store, addres_store, tel_store, type_store)
            store.save()
            tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
            win_store.destroy()
        except:
            tk.messagebox.showerror('خطا','ثبت با خطا مواجعه شد')

    save = tk.Button(win_store,text="ویرایش",command=save,font="#2526")
    save.place(x=200,y=190)

    def flistselect(event):
        global item
        try:
            new_item = list_s.curselection()
            if new_item:
                item = new_item
                txtname.set(s[item[0]].name)
                txtcode_store.set(s[item[0]].code_store)
                txtaddres_store.set(s[item[0]].addres_store)
                txttel_store.set(s[item[0]].tel_store)
                txttype_store.set(s[item[0]].type_store)
        except:
           pass

    list_s.bind('<<ListboxSelect>>',flistselect)
    
def delete_store():
    win_store = tk.Toplevel()
    win_store.title("حدف انبار")
    win_store.geometry('400x300+400+200')
    win_store.configure(bg='#FFA500')
    tk.Label(win_store,text="لیست انبارها",bg='#FFA500').grid(row=0,column=0)
    list_p,s=creat_list(j.Store, win_store, 1, 0)
    
    tk.Label(win_store,text=":نام",bg="#FFA500").place(x=290,y=20)
    lbname = tk.Label(win_store,bg="#FFA500")
    lbname.place(x=150,y=20)
    
    tk.Label(win_store,text=":کد انبار",bg="#FFA500").place(x=290,y=40)
    lbcode_store = tk.Label(win_store,bg="#FFA500")
    lbcode_store.place(x=150,y=40)
    
    tk.Label(win_store,text=":آدرس انبار",bg="#FFA500").place(x=290,y=60)
    lbaddres_store = tk.Label(win_store,bg="#FFA500")
    lbaddres_store.place(x=150,y=60)
    
    tk.Label(win_store,text=":تلفن ثابت",bg="#FFA500").place(x=290,y=80)
    lbtel_store = tk.Label(win_store,bg="#FFA500")
    lbtel_store.place(x=150,y=80)
    
    tk.Label(win_store,text=":نوع کالای انبار",bg="#FFA500").place(x=290,y=100)
    lbtype_store = tk.Label(win_store,bg="#FFA500")
    lbtype_store.place(x=150,y=100)
    
    item=-1
    
    def delete():
        try:
            
            global item
            s[item[0]].delete()
            tk.messagebox.showinfo('پیام موفقیت','حذف با موفقیت انجام شد')
            win_store.destroy()
        except:
            tk.messagebox.showerror('خطا','حذف با خطا مواجعه شد')
            win_store.destroy()
    
    save = tk.Button(win_store,text='حذف',command=delete,font="#2526")
    save.place(x=200,y=190)

    def back():
        win_store.destroy()

    back = tk.Button(win_store,text="بازگشت",command=back,font="#2526")
    back.place(x=250,y=190)
    
    def flistselect(event):
        global item
        item = list_p.curselection()
        
        lbname.config(text=s[item[0]].name)
        lbcode_store.config(text=s[item[0]].code_store)
        lbaddres_store.config(text=s[item[0]].addres_store)
        lbtel_store.config(text=s[item[0]].tel_store)
        lbtype_store.config(text=s[item[0]].type_store)

    def new_func():
        return 0

    list_p.bind('<<ListboxSelect>>',flistselect)      

submenu = Menu(tarif, tearoff=0)
submenu.add_command(label=" نعریف انبار",accelerator="Ctrl+Q",command=form_store)
form_store = tk.Button(win,text="تعریف انبار",command=form_store,bg='#FFA500',width=13,height=2,font="#2526")
form_store.place(x=1380,y=113)

submenu.add_command(label="ویرایش انبار",command=edit_store)
submenu.add_command(label="حدف انبار",command=delete_store)
tarif.add_cascade(label="       انبار",menu=submenu)

def lst_customer():
    win_cardex = tk.Toplevel()
    win_cardex.title("لیست مشتری")
    win_cardex.geometry("500x250+420+225")
    win_cardex.configure(bg='#FFA500')
    tk.Label(win_cardex,text="لیست مشتری ها ",bg='#FFA500').grid(row=0,column=0)
    list_p,s=creat_list(j.Customer, win_cardex, 1, 0)
    
    tk.Label(win_cardex,text=":نام",bg="#FFA500").place(x=290,y=20)
    lbferst_name = tk.Label(win_cardex,bg="#FFA500")
    lbferst_name.place(x=200,y=20)
    
    tk.Label(win_cardex,text=":نام خانوادگی",bg="#FFA500").place(x=290,y=40)
    lblast_name = tk.Label(win_cardex,bg="#FFA500")
    lblast_name.place(x=200,y=40)
    
    tk.Label(win_cardex,text=":کد اشتراک",bg="#FFA500").place(x=290,y=60)
    lbcode = tk.Label(win_cardex,bg="#FFA500")
    lbcode.place(x=200,y=60)
    
    tk.Label(win_cardex,text=":تلفن ثابت",bg="#FFA500").place(x=290,y=80)
    lbtel_1 = tk.Label(win_cardex,bg="#FFA500")
    lbtel_1.place(x=200,y=80)
    
    tk.Label(win_cardex,text=":تلفن شخصی",bg="#FFA500").place(x=290,y=100)
    lbtel_2 = tk.Label(win_cardex,bg="#FFA500")
    lbtel_2.place(x=200,y=100)
    
    tk.Label(win_cardex,text=":آدرس",bg="#FFA500").place(x=290,y=120)
    lbaddres = tk.Label(win_cardex,bg="#FFA500")
    lbaddres.place(x=200,y=120)
    
    tk.Label(win_cardex,text=":قرارداد",bg="#FFA500").place(x=290,y=140)
    lbcontract = tk.Label(win_cardex,bg="#FFA500")
    lbcontract.place(x=200,y=140)

    def flistselect(event):
        global item
        item = list_p.curselection()
        
        lbferst_name.config(text=s[item[0]].ferst_name)
        lblast_name.config(text=s[item[0]].last_name)
        lbtel_1.config(text=s[item[0]].tel_1)
        lbtel_2.config(text=s[item[0]].tel_2)
        lbaddres.config(text=s[item[0]].addres)
        lbcontract.config(text=s[item[0]].conteract)
        lbcode.config(text=s[item[0]].code)
        
    list_p.bind('<<ListboxSelect>>',flistselect) 
       
    def back():
        win_cardex.destroy()

    back = tk.Button(win_cardex,text="بازگشت",command=back,font="#2526")
    back.place(x=240,y=200)
    
people.add_command(label="لیست مشتری ها ",accelerator="Ctrl+C",command=lst_customer)
# people.add_separator()

def factor_buy():
    win_factor = tk.Toplevel()
    win_factor.title("فاکتور خرید")
    win_factor.geometry("1220x600+200+120")#000080
    win_factor.configure(bg='#000080')
    tk.Label(win_factor,text='مشتریان',bg='#000080',font="#2526").grid(row=0,column=0)
    ist_cust,s_cust = creat_Combobox(j.Customer, win_factor, 1, 0)
    
    tk.Label(win_factor,text='انبار ها',bg='#000080',font="#2526").grid(row=0,column=2)
    ist_store,s_str = creat_Combobox(j.Store, win_factor, 1, 2)
    
    tk.Label(win_factor,text='کاربر',bg='#000080',font="#2526").grid(row=0,column=4)
    ist_us,s_user = creat_Combobox(j.User, win_factor, 1, 4)
    
    tk.Label(win_factor,text='کالا ها',bg='#000080',font="#2526").grid(row=0,column=6)
    list_kl,s_kala = creat_list(j.Kala, win_factor, 1, 6)
    
    tk.Label(win_factor,text='تعداد کالا',bg='#000080',font="#2132").place(x=630,y=20)
    entcount=tk.Entry(win_factor)
    entcount.place(x=600,y=50)
    
    tk.Label(win_factor,text=':نام مشتری').place(x=1000,y=30)
    lbname_customer = tk.Label(win_factor,text='###')
    lbname_customer.place(x=850,y=30)
    
    tk.Label(win_factor,text=':فامیل مشتری').place(x=1000,y=54)
    lbfamil_customer = tk.Label(win_factor,text='###')
    lbfamil_customer.place(x=850,y=54)
    
    tk.Label(win_factor,text=':کد اشتراک').place(x=1000,y=74)
    lbcode_customer = tk.Label(win_factor,text='###')
    lbcode_customer.place(x=850,y=74)
    
    tk.Label(win_factor,text=':تلفن شخصی').place(x=1000,y=94)
    lbtel_customer = tk.Label(win_factor,text='###')
    lbtel_customer.place(x=850,y=94)
    
    tk.Label(win_factor,text=':آدرس مشتری').place(x=1000,y=114)
    lbaddres_customer = tk.Label(win_factor,text='###')
    lbaddres_customer.place(x=850,y=114)
    
    tk.Label(win_factor,text='  :تاریخ',bg='#000080',font="#1111").place(x=1150,y=176)
    lbdate = tk.Label(win_factor,text=date.today(),bg='#FFA500')
    lbdate.place(x=1086,y=180)
     
    def fainal():
        tk.messagebox.showinfo('پیام موفقیت','ثبت نهایی با موفقیت انجام شد')
        win_factor.destroy()
        
    bnt_fanalsve=tk.Button(win_factor,text='ثبت نهایی',command=fainal,bg='#FFA500',font="#2528")
    bnt_fanalsve.place(x=1000,y=500)

    def radif():
        for i in range(1,50):
            yield i
    r = radif()
            
    def add_kala():
        try:
            item = list_kl.curselection()
            #print(s_kala[item[0]])
            count = entcount.get()
            # tree.insert('', tk.END,values=[s_kala[item[0]].name,s_kala[item[0]].code_kala,count,s_kala[item[0]].unit_1,s_kala[item[0]].n_unitو])
            tree.insert('', tk.END,values=[s_kala[item[0]].n_unit,s_kala[item[0]].unit_1,count,s_kala[item[0]].name,s_kala[item[0]].code_kala,next(r)])
            
        except:
            tk.messagebox.showerror('خطا','کالا انتخاب نشده است')
        
        lst_buy = []
        if fainal:
            n_unit = n_unit.get()
            unit_1 = unit_1.get()
            count = count.get()
            name = name.get()
            code_kala = code_kala.get()
            lst_buy.insert([[n_unit,unit_1,count,name,code_kala]])
            lst_buy = j.Factor_bay()
            lst_buy.save()
            
    bntadd_kala = tk.Button(win_factor,text='اضافه کردن کالا',bg='#FFA500',command=add_kala,font="#2528")
    bntadd_kala.place(x=600,y=80)

    colums=("n_unit","unit_2","count","name","code_kala","num")
    tree=ttk.Treeview(win_factor,columns=colums,show='headings')
    tree.place(x=10,y=250)
    tree.heading("n_unit",text="نسبت واحد")
    tree.heading("unit_2",text="واحد")
    tree.heading("count",text="تعداد")
    tree.heading("num",text="ردیف")
    tree.heading("code_kala",text="کد کالا")
    tree.heading("name",text="نام کالا")
    
    def flistboxselect(event):
        item=ist_cust.current()
       
        lbname_customer.config(text=s_cust[item].ferst_name)
        lbfamil_customer.config(text=s_cust[item].last_name)
        lbcode_customer.config(text=s_cust[item].code)
        lbtel_customer.config(text=s_cust[item].tel_2)
        lbaddres_customer.config(text=s_cust[item].addres)
        
        
    ist_cust.bind('<<ComboboxSelected>>',flistboxselect)

    def back():
        win_factor.destroy()

    back = tk.Button(win_factor,text="بازگشت",command=back,bg='#FFA500',font="2528")
    back.place(x=930,y=500)
               

def factor_sell():
    win_factor = tk.Toplevel()
    win_factor.title("فاکتور خرید")
    win_factor.geometry("1220x600+200+120")
    win_factor.configure(bg='#000080')
        
    tk.Label(win_factor,text='مشتریان',bg='#000080',font="#2526").grid(row=0,column=0)
    ist_cust,s_cust = creat_Combobox(j.Customer, win_factor, 1, 0)
    
    tk.Label(win_factor,text='انبار ها',bg='#000080',font="#2526").grid(row=0,column=2)
    ist_store,s_str = creat_Combobox(j.Store, win_factor, 1, 2)
    
    tk.Label(win_factor,text='کاربر',bg='#000080',font="#2526").grid(row=0,column=4)
    ist_us,s_user = creat_Combobox(j.User, win_factor, 1, 4)
    
    tk.Label(win_factor,text='کالا ها',bg='#000080',font="#2526").grid(row=0,column=6)
    list_kl,s_kala = creat_list(j.Kala, win_factor, 1, 6)
    
    tk.Label(win_factor,text='تعداد کالا',bg='#000080',font="#2526").place(x=630,y=20)
    entcount=tk.Entry(win_factor)
    entcount.place(x=600,y=50)
    
    tk.Label(win_factor,text=':نام مشتری').place(x=1000,y=30)
    lbname_customer = tk.Label(win_factor,text='###')
    lbname_customer.place(x=850,y=30)
    
    tk.Label(win_factor,text=':فامیل مشتری').place(x=1000,y=54)
    lbfamil_customer = tk.Label(win_factor,text='###')
    lbfamil_customer.place(x=850,y=54)
    
    tk.Label(win_factor,text=':کد اشتراک').place(x=1000,y=74)
    lbcode_customer = tk.Label(win_factor,text='###')
    lbcode_customer.place(x=850,y=74)
    
    tk.Label(win_factor,text=':تلفن شخصی').place(x=1000,y=94)
    lbtel_customer = tk.Label(win_factor,text='###')
    lbtel_customer.place(x=850,y=94)
    
    tk.Label(win_factor,text=':آدرس مشتری').place(x=1000,y=114)
    lbaddres_customer = tk.Label(win_factor,text='###')
    lbaddres_customer.place(x=850,y=114)
     
    tk.Label(win_factor,text='  :تاریخ',bg='#000080',font="#2526").place(x=1150,y=176)
    lbdate = tk.Label(win_factor,text=date.today(),bg='#FFA500')
    lbdate.place(x=1086,y=180)
    
    def radif():
        for i in range(1,50):
            yield i
    r1 = radif()
    
    def fainal():
        tk.messagebox.showinfo('پیام موفقیت','ثبت نهایی با موفقیت انجام شد')
        win_factor.destroy()
        
    bnt_fanalsve=tk.Button(win_factor,text='ثبت نهایی',command=fainal,bg='#FFA500',font="#2526")
    bnt_fanalsve.place(x=1000,y=500)
          
    def add_kala():
        try:
            item = list_kl.curselection()
            #print(s_kala[item[0]])
            count = entcount.get()
            tree.insert('', tk.END,values=[s_kala[item[0]].n_unit,s_kala[item[0]].unit_1,count,s_kala[item[0]].name,s_kala[item[0]].code_kala,next(r1)])
            
        except:
            tk.messagebox.showerror('خطا','کالا انتخاب نشده است')
            
    bntadd_kala = tk.Button(win_factor,text='اضافه کردن کالا',bg='#FFA500',command=add_kala,font="#2526")
    bntadd_kala.place(x=600,y=80)
    
    colums=("n_unit","unit_2","count","name","code_kala","num")
    tree=ttk.Treeview(win_factor,columns=colums,show='headings')
    tree.place(x=10,y=250)
    tree.heading("n_unit",text="نسبت واحد")
    tree.heading("unit_2",text="واحد")
    tree.heading("count",text="تعداد")
    tree.heading("num",text="ردیف")
    tree.heading("code_kala",text="کد کالا")
    tree.heading("name",text="نام کالا")
    
    def flistboxselect(event):
        item=ist_cust.current()
       
        lbname_customer.config(text=s_cust[item].ferst_name)
        lbfamil_customer.config(text=s_cust[item].last_name)
        lbcode_customer.config(text=s_cust[item].code)
        lbtel_customer.config(text=s_cust[item].tel_2)
        lbaddres_customer.config(text=s_cust[item].addres)
        
    ist_cust.bind('<<ComboboxSelected>>',flistboxselect)

    def back():
        win_factor.destroy()

    back = tk.Button(win_factor,text="بازگشت",command=back,bg='#FFA500',font="#2526")
    back.place(x=930,y=500)

submenu = Menu(sayeramliat, tearoff=0)
submenu.add_command(label="فاکتور خرید",accelerator="F5",command=factor_buy)
factor_buy = tk.Button(win,text="فاکتور خرید",command=factor_buy,bg='#000080',width=13,height=2,font="#2526")
factor_buy.place(x=1380,y=168)

submenu.add_command(label="فاکتور فروش",accelerator="F6",command=factor_sell)
factor_sell = tk.Button(win,text="فاکتور فروش",command=factor_sell,bg='#000080',width=13,height=2,font="#2526")
factor_sell.place(x=1380,y=223)

sayeramliat.add_cascade(label="       فاکتور ",menu=submenu)
sayeramliat.add_separator()


def handeling_store():
    win_kala=tk.Toplevel()
    win_kala.title(" انبارگردانی")
    win_kala.geometry('500x300+400+200')
    win_kala.configure(bg='#FFA500')
    tk.Label(win_kala,text="لیست کالا ها",bg='#FFA500').grid(row=0,column=0)
    list_k,s=creat_list(j.Kala, win_kala, 1, 0)
        
    tk.Label(win_kala,text=":نام کالا",bg="#FFA500").place(x=250,y=20)
    lbname = tk.Label(win_kala,text='###',bg='#FFA500')
    lbname.place(x=150,y=20)
    
    tk.Label(win_kala,text=":واحد اول",bg="#FFA500").place(x=250,y=50)
    lbunit_1 = tk.Label(win_kala,text='###',bg='#FFA500')
    lbunit_1.place(x=150,y=50)

    tk.Label(win_kala,text=":نسبت واحد",bg="#FFA500").place(x=250,y=80)
    lbn_unit = tk.Label(win_kala,text='###',bg='#FFA500')
    lbn_unit.place(x=150,y=80)
    
    tk.Label(win_kala,text=":تعداد(واحد اول)",bg="#FFA500").place(x=250,y=110)
    lbcount = tk.Label(win_kala,text='###',bg='#FFA500')
    lbcount.place(x=150,y=110)
    
    tk.Label(win_kala,text=":شرح کالا",bg="#FFA500").place(x=250,y=140)
    lbdescription = tk.Label(win_kala,text='###',bg='#FFA500')
    lbdescription.place(x=150,y=140)
    
    tk.Label(win_kala,text='           ').place(x=450,y=10)
    tk.Label(win_kala,text=':تاریخ',bg='#FFA500',font="#1111",width=5,height=1).place(x=430,y=10)
    lbdate = tk.Label(win_kala,text=date.today(),bg='#000080',width=9,height=1)
    lbdate.place(x=360,y=15)
    item=-1
    
    def back():
        win_kala.destroy()

    back = tk.Button(win_kala,text="بازگشت",command=back,font="#2526")
    back.place(x=250,y=200)
    
    def flistselect(event):
        global item
        item = list_k.curselection()
        
        lbname.config(text=s[item[0]].name)
        lbunit_1.config(text=s[item[0]].unit_1)
        lbn_unit.config(text=s[item[0]].n_unit)
        lbcount.config(text=s[item[0]].count)
        lbdescription.config(text=s[item[0]].description)

        
    list_k.bind('<<ListboxSelect>>',flistselect)

sayeramliat.add_command(label=" انبارگردانی",accelerator="Ctrl+F",command=handeling_store)
handeling_store = tk.Button(win,text="انبارگردانی",command=handeling_store,bg='#FFA500',width=13,height=2,font="#2526")
handeling_store.place(x=1380,y=278)

def lst_store():
    win_lst_store = tk.Toplevel()
    win_lst_store.title("لیست انبارها")
    win_lst_store.geometry("500x400+420+225")
    win_lst_store.configure(bg='#FFA500')
    
    tk.Label(win_lst_store,text="لیست مشتری ها ",bg='#FFA500').grid(row=0,column=0)
    list_s,s = creat_list(j.Store, win_lst_store, 1, 0)
    
    tk.Label(win_lst_store,text=":نام انبار",bg='#FFA500').place(x=280,y=20)
    lbname = tk.Label(win_lst_store,text='###',bg='#FFA500')
    lbname.place(x=160,y=20)
    
    tk.Label(win_lst_store,text=":شماره انبار",bg='#FFA500').place(x=280,y=40)
    lbcode_store = tk.Label(win_lst_store,text='###',bg='#FFA500')
    lbcode_store.place(x=160,y=40)
    
    tk.Label(win_lst_store,text=":آدرس",bg='#FFA500').place(x=280,y=60)
    lbaddres_store=tk.Label(win_lst_store,text='###',bg='#FFA500')
    lbaddres_store.place(x=160,y=60)
    
    tk.Label(win_lst_store,text=":تلفن",bg='#FFA500').place(x=280,y=80)
    lbtel_store=tk.Label(win_lst_store,text='###',bg='#FFA500')
    lbtel_store.place(x=160,y=80)
    
    tk.Label(win_lst_store,text=":نوع کالا",bg='#FFA500').place(x=280,y=100)
    lbtype_store=tk.Label(win_lst_store,text='###',bg='#FFA500')
    lbtype_store.place(x=160,y=100)

    def flistselect(event):
        global item
        item=list_s.curselection()
        
        lbname.config(text=s[item[0]].name)
        lbcode_store.config(text=s[item[0]].code_store)
        lbaddres_store.config(text=s[item[0]].addres_store)
        lbtel_store.config(text=s[item[0]].tel_store)
        lbtype_store.config(text=s[item[0]].type_store)
        
    list_s.bind('<<ListboxSelect>>',flistselect)
       
    def back():
        win_lst_store.destroy()

    back = tk.Button(win_lst_store,text="بازگشت",command=back,font="#2526")
    back.place(x=240,y=200)

    
gozatesh.add_command(label="       لیست انبارها",accelerator="Ctrl+X",command=lst_store)
gozatesh.add_separator()

def lst_buy():
    win_lst_buy = tk.Toplevel()
    win_lst_buy.title("لیست رسید ها")
    win_lst_buy.geometry("750x500+420+225")
    win_lst_buy.configure(bg='#FFA500')
    
    tk.Label(win_lst_buy,text="لیست رسید ها ",bg='#FFA500').grid(row=0,column=0)
    list_s,s = creat_list(j.Factor_bay, win_lst_buy, 1, 0)
    
    tk.Label(win_lst_buy,text="نام مشتری",bg='#FFA500').place(x=280,y=20)
    lbferst_name = tk.Label(win_lst_buy,text='###',bg='#FFA500')
    lbferst_name.place(x=200,y=20)
    
    tk.Label(win_lst_buy,text="نام خانوادگی مشتری",bg='#FFA500').place(x=280,y=40)
    lblast_name = tk.Label(win_lst_buy,text='###',bg='#FFA500')
    lblast_name.place(x=200,y=40)
    
    tk.Label(win_lst_buy,text="کد اشتراک",bg='#FFA500').place(x=280,y=60)
    lbcode =tk.Label(win_lst_buy,text='###',bg='#FFA500')
    lbcode.place(x=200,y=60)
    
    tk.Label(win_lst_buy,text="آدرس",bg='#FFA500').place(x=280,y=80)
    lbaddres = tk.Label(win_lst_buy,text='###',bg='#EA4CED')
    lbaddres.place(x=200,y=80)
    
    tk.Label(win_lst_buy,text="تاریخ",bg='#FFA500').place(x=280,y=100)
    lbdate = tk.Label(win_lst_buy,text="date.today()",bg='#FFA500')
    lbdate.place(x=200,y=100)

    def flistselect(event):
        global item
        item=list_s.curselection()
        
        lblast_name.config(text=s[item[0]].last_name)
        lbferst_name.config(text=s[item[0]].ferst_name)
        lbcode.config(text=s[item[0]].code)
        lbaddres.config(text=s[item[0]].addres)
        lbdate.config(text=s[item[0]].date)
        
    list_s.bind('<<ListboxSelect>>',flistselect)
       
    def back():
        win_lst_buy.destroy()

    back = tk.Button(win_lst_buy,text="بازگشت",command=back,font="#2526")
    back.place(x=240,y=200)

        
gozatesh.add_command(label="     لیست رسیدها",accelerator="Ctrl+B",command=lst_buy)
lst_buy = tk.Button(win,text="لیست رسیدها",command=lst_buy,bg='#FFA500',width=13,height=2,font="#2526")
lst_buy.place(x=1380,y=333)
gozatesh.add_separator()

def lst_sell():
    win_cardex = tk.Toplevel()
    win_cardex.title("لیست حواله ها")
    win_cardex.geometry("750x500+420+225")
    
    
    list_s = j.sell.read_file()
    val_sell = tk.StringVar(value=list_s)
    lst_sell = tk.Listbox(win_cardex,listvariable=val_sell,width=100,height=30)
    lst_sell.place(x=30,y=0)

gozatesh.add_command(label="    لیست حواله ها",accelerator="Ctrl+A",command=lst_sell)
lst_sell = tk.Button(win,text="لیست حواله ها",command=lst_sell,bg='#FFA500',width=13,height=2,font="#2526")
lst_sell.place(x=1380,y=388)
gozatesh.add_separator()

def cardex_kala():
    win_cardex_kala = tk.Toplevel()
    win_cardex_kala.title("کاردکس موجودی کالا")
    win_cardex_kala.geometry("500x300+420+225")
    win_cardex_kala.configure(bg='#FFA500')
    tk.Label(win_cardex_kala,text="لیست کالا ها",bg='#FFA500').grid(row=0,column=0)
    list_k,s = creat_list(j.Kala, win_cardex_kala, 1, 0)
        
    tk.Label(win_cardex_kala,text="نام کالا",bg="#FFA500").place(x=250,y=20)
    lbname = tk.Label(win_cardex_kala,text='###',bg='#FFA500')
    lbname.place(x=150,y=20)
    
    tk.Label(win_cardex_kala,text="کد کالا",bg="#FFA500").place(x=250,y=40)
    lbcode_kala = tk.Label(win_cardex_kala,text='###',bg='#FFA500')#
    lbcode_kala.place(x=150,y=40)
    
    tk.Label(win_cardex_kala,text="واحد اول",bg="#FFA500").place(x=250,y=60)
    lbunit_1 = tk.Label(win_cardex_kala,text='###',bg='#FFA500')
    lbunit_1.place(x=150,y=60)
    
    tk.Label(win_cardex_kala,text="واحد دوم",bg="#FFA500").place(x=250,y=80)
    lbunit_2 = tk.Label(win_cardex_kala,text='###',bg='#FFA500')#
    lbunit_2.place(x=150,y=80)
    
    tk.Label(win_cardex_kala,text="نسبت واحد",bg="#FFA500").place(x=250,y=100)
    lbn_unit = tk.Label(win_cardex_kala,text='###',bg='#FFA500')
    lbn_unit.place(x=150,y=100)
    
    tk.Label(win_cardex_kala,text="نوع",bg="#FFA500").place(x=250,y=120)
    lbtype_kala = tk.Label(win_cardex_kala,text='###',bg='#FFA500')#
    lbtype_kala.place(x=150,y=120)
    
    tk.Label(win_cardex_kala,text="تعداد",bg="#FFA500").place(x=250,y=140)
    lbcount = tk.Label(win_cardex_kala,text='###',bg='#FFA500')#
    lbcount.place(x=150,y=140)
    
    tk.Label(win_cardex_kala,text="شرح کالا",bg="#FFA500").place(x=250,y=160)
    lbdescription = tk.Label(win_cardex_kala,text='###',bg='#FFA500')
    lbdescription.place(x=150,y=160)
    item=-1
    
    def back():
        win_cardex_kala.destroy()

    back = tk.Button(win_cardex_kala,text="بازگشت",command=back,font="#2526")
    back.place(x=240,y=200)
    
    def flistselect(event):
        global item
        item = list_k.curselection()
        
        lbname.config(text=s[item[0]].name)
        lbcode_kala.config(text=s[item[0]].code_kala)
        lbunit_1.config(text=s[item[0]].unit_1)
        lbunit_2.config(text=s[item[0]].unit_2)
        lbn_unit.config(text=s[item[0]].n_unit)
        lbtype_kala.config(text=s[item[0]].type_kala)
        lbcount.config(text=s[item[0]].count)
        lbdescription.config(text=s[item[0]].description)
        
    list_k.bind('<<ListboxSelect>>',flistselect)
 
gozatesh.add_command(label="کاردکس موجودی کالا",accelerator="Ctrl+D",command=cardex_kala)
cardex_kala = tk.Button(win,text="کاردکس موجودی کالا",command=cardex_kala,bg='#FFA500',width=13,height=2,font="#2526")
cardex_kala.place(x=1380,y=443)

def user_panel():
    win_user = tk.Toplevel()
    win_user.title("پنل کاربری")
    win_user.geometry("420x260+420+225")
    win_user.configure(bg='#FFA500')
    
    tk.Label(win_user,text="انتخاب کاربر",bg='#FFA500').grid(row=0,column=0)
    list_u,s = creat_list(j.User, win_user, 1, 0)
    
    tk.Label(win_user,text="نام ",bg="#FFA500").place(x=250,y=20)
    lbferst_name = tk.Label(win_user,text='###',bg='#FFA500')
    lbferst_name.place(x=150,y=20)
    
    tk.Label(win_user,text="نام خانوادگی",bg="#FFA500").place(x=250,y=40)
    lblast_name = tk.Label(win_user,text='###',bg='#FFA500')#
    lblast_name.place(x=150,y=40)
    
    tk.Label(win_user,text="تلفن ثابت",bg="#FFA500").place(x=250,y=60)
    lbtel_1 = tk.Label(win_user,text='###',bg='#FFA500')
    lbtel_1.place(x=150,y=60)
    
    tk.Label(win_user,text="تلفن شخصی",bg="#FFA500").place(x=250,y=80)
    lbtel_2 = tk.Label(win_user,text='###',bg='#FFA500')#
    lbtel_2.place(x=150,y=80)
    
    tk.Label(win_user,text="شیفت",bg="#FFA500").place(x=250,y=100)
    lbshift = tk.Label(win_user,text='###',bg='#FFA500')
    lbshift.place(x=150,y=100)
    
    item=-1
    def back():
        win_user.destroy()

    back = tk.Button(win_user,text="بازگشت",command=back,font="#2526")
    back.place(x=240,y=150)
    
    def flistselect(event):
        global item
        item = list_u.curselection()
        
        lbferst_name.config(text=s[item[0]].ferst_name)
        lblast_name.config(text=s[item[0]].last_name)
        lbtel_1.config(text=s[item[0]].tel_1)
        lbtel_2.config(text=s[item[0]].tel_2)
        lbshift.config(text=s[item[0]].shift)

        
    list_u.bind('<<ListboxSelect>>',flistselect)
        

setting.add_command(label="        پنل کاربری",accelerator="F6",command=user_panel)
user_panel = tk.Button(win,text="پنل کاربری",command=user_panel,bg='#FFA500',width=13,height=2,font="#2526")
user_panel.place(x=1380,y=498)
setting.add_separator()

def  form_user():
    win_user = tk.Toplevel()
    win_user.title("ساخت کاربر جدید")
    win_user.geometry("500x300+520+280")
    win_user.configure(bg='#FFA500')
    
    tk.Label(win_user,text="نام",bg='#FFA500').grid(row=0,column=0)
    entferst_name = tk.Entry(win_user)
    entferst_name.grid(row=0,column=1)
    
    tk.Label(win_user,text="نام خانوادگی",bg='#FFA500').place(x=200,y=0)
    entlast_name = tk.Entry(win_user)
    entlast_name.place(x=270,y=0)
    
    tk.Label(win_user,text="تلفن ثابت",bg='#FFA500').grid(row=2,column=0)
    enttel_1 = tk.Entry(win_user)
    enttel_1.grid(row=2,column=1)
    
    tk.Label(win_user,text="تلفن شخصی",bg='#FFA500').place(x=200,y=20)
    enttel_2 = tk.Entry(win_user)
    enttel_2.place(x=270,y=20)
    
    tk.Label(win_user,text="آدرس",bg='#FFA500').grid(row=4,column=0)
    entaddres = tk.Entry(win_user)
    entaddres.grid(row=4,column=1)
    
    tk.Label(win_user,text="شیفت",bg='#FFA500').place(x=210,y=40)
    entshift = tk.Entry(win_user)
    entshift.place(x=270,y=40)
    
    tk.Label(win_user,text="نام کاربری",bg='#FFA500').grid(row=6,column=0)
    entusername = tk.Entry(win_user)
    entusername.grid(row=6,column=1)
    
    tk.Label(win_user,text="رمزعبور",bg='#FFA500').place(x=210,y=60)
    entpassword = tk.Entry(win_user)
    entpassword.place(x=270,y=60)
    def showchar(event):
        print(event.keysym)

    def back():
        win_user.destroy()

    back = tk.Button(win_user,text="بازگشت",command=back,font="#2526")
    back.place(x=380,y=250)
    
    def save():
        ferst_name = entferst_name.get()
        last_name = entlast_name.get()
        addres = entaddres.get()  
        shift = entshift.get()
        username = entusername.get()
        password = entpassword.get()
        try:    
            tel_1 = int(enttel_1.get())
            tel_2 = int(enttel_2.get())

            user = j.User(ferst_name,last_name,tel_1,tel_2,addres,shift,username,password)
            user.save()
            tk.messagebox.showinfo('پیام موفقیت','ثبت با موفقیت انجام شد')
            win_user.destroy()
        except:
            tk.messagebox.showinfo('خطا','این فیلد باید عدد باشد')  
 
    save = tk.Button(win_user,text="دخیره",command=save,font="#2526")
    save.place(x=300,y=250)

def edit_user():
    win_user = tk.Toplevel()
    win_user.title("ویرایش  کاربر")
    win_user.geometry("400x270+520+280")
    win_user.configure(bg='#FFA500')

    tk.Label(win_user,text="لیست اطلاعات",bg="#FFA500").grid(row=0,column=0)
    list_u,s = creat_list(j.User, win_user, 1, 0)
    
    tk.Label(win_user,text="نام ",bg="#FFA500").place(x=250,y=20)
    
    txtferst_name = tk.StringVar(value='###')
    entfetst_name = tk.Entry(win_user,justify='right',textvariable=txtferst_name)
    entfetst_name.place(x=125,y=20)
    
    tk.Label(win_user,text="نام خانوادگی",bg="#FFA500").place(x=250,y=40)
    
    txtlast_name = tk.StringVar(value='###')
    entlast_name = tk.Entry(win_user,justify='right',textvariable=txtlast_name)
    entlast_name.place(x=125,y=40)
    
    tk.Label(win_user,text="تلفن ثابت",bg="#FFA500").place(x=250,y=60)
    
    txttel_1 = tk.StringVar(value='###')
    enttel_1 = tk.Entry(win_user,justify='right',textvariable=txttel_1)
    enttel_1.place(x=125,y=60)
    
    tk.Label(win_user,text="تلفن شخصی",bg='#FFA500').place(x=250,y=80)
    
    txttel_2 = tk.StringVar(value='###')
    enttel_2 = tk.Entry(win_user,justify='right',textvariable=txttel_2)
    enttel_2.place(x=125,y=80)
    
    tk.Label(win_user,text="آدرس",bg='#FFA500').place(x=250,y=100)
    
    txtaddres = tk.StringVar(value='###')
    entaddres = tk.Entry(win_user,justify='right',textvariable=txtaddres)
    entaddres.place(x=125,y=100)
    
    tk.Label(win_user,text="شیفت",bg='#FFA500').place(x=250,y=120)
    
    txtshift = tk.StringVar(value='###')
    entshift = tk.Entry(win_user,justify='right',textvariable=txtshift)
    entshift.place(x=125,y=120)
    
    tk.Label(win_user,text="نام کاربری",bg='#FFA500').place(x=250,y=140)
    
    txtusername = tk.StringVar(value='###')
    entusername = tk.Entry(win_user,justify='right',textvariable=txtusername)
    entusername.place(x=125,y=140)
    
    tk.Label(win_user,text="رمز عبور",bg='#FFA500').place(x=250,y=160)
    
    txtpassword = tk.StringVar(value='###')
    entpassword = tk.Entry(win_user,justify='right',textvariable=txtpassword)
    entpassword.place(x=125,y=160)
    item=(0,)
    
    def back():
        win_user.destroy()

    back = tk.Button(win_user,text="بازگشت",command=back,font="#2526")
    back.place(x=250,y=200)
    
    def save_edit():
        ferst_name = ferst_name.get()
        last_name = entlast_name.get()
        shift = entshift.get()
        username = entusername.get()
        password = entpassword.get()
        try:
            tel_1 = int(enttel_1.get())
            tel_2 = int(enttel_2.get())
            
        except:
            tk.messagebox.showinfo('خطا','این فیلد باید عدد باشد')
            
        addres = entaddres.get()
 
        customer = j.Customer(ferst_name,last_name,tel_1,tel_2,addres,shift,username,password)
        customer.save()
        win_user.destroy()
        
    save = tk.Button(win_user,text="دخیره",command=save_edit,font="#2526")
    save.place(x=200,y=200)
    
    def flistselect(event):
        global item
        try:
            new_item = list_u.curselection()
            
            if new_item:
                item=new_item
                txtferst_name.set(s[item[0]].ferst_name)
                txtlast_name.set(s[item[0]].last_name)
                txttel_1.set(s[item[0]].tel_1)
                txttel_2.set(s[item[0]].tel_2)
                txtaddres.set(s[item[0]].addres)
                txtusername.set(s[item[0]].username)
                txtpassword.set(s[item[0]].password)
                txtshift.set(s[item[0]].shift)
        except:
            pass
        
    list_u.bind('<<ListboxSelect>>',flistselect)

def delete_user():
    win_user=tk.Toplevel()
    win_user.title("حدف کاربر")
    win_user.geometry('420x240+400+200')
    win_user.configure(bg='#FFA500')
    tk.Label(win_user,text="لیست اطلاعات",bg='#FFA500').grid(row=0,column=0)
    list_u,s=creat_list(j.User, win_user, 1, 0)
    
    tk.Label(win_user,text="نام ",bg="#FFA500").place(x=250,y=20)
    lbferst_name = tk.Label(win_user,text='###',bg='#FFA500')
    lbferst_name.place(x=150,y=20)
    
    tk.Label(win_user,text="نام خانوادگی",bg="#FFA500").place(x=250,y=40)
    lblast_name = tk.Label(win_user,text='###',bg='#FFA500')#
    lblast_name.place(x=150,y=40)
    
    tk.Label(win_user,text="تلفن ثابت",bg="#FFA500").place(x=250,y=60)
    lbtel_1 = tk.Label(win_user,text='###',bg='#FFA500')
    lbtel_1.place(x=150,y=60)
    
    tk.Label(win_user,text="تلفن شخصی",bg="#FFA500").place(x=250,y=80)
    lbtel_2 = tk.Label(win_user,text='###',bg='#FFA500')#
    lbtel_2.place(x=150,y=80)
    
    tk.Label(win_user,text="شیفت",bg="#FFA500").place(x=250,y=100)
    lbshift = tk.Label(win_user,text='###',bg='#FFA500')
    lbshift.place(x=150,y=100)
    
    tk.Label(win_user,text="نام کاربری",bg="#FFA500").place(x=250,y=120)
    lbusername = tk.Label(win_user,text='###',bg='#FFA500')#
    lbusername.place(x=150,y=120)
    
    tk.Label(win_user,text="رمز عبور",bg="#FFA500").place(x=250,y=140)
    lbpassword = tk.Label(win_user,text='###',bg='#FFA500')
    lbpassword.place(x=150,y=140)
    item=-1
    
    def delete():
        try:
            
            global item
            s[item[0]].delete()
            tk.messagebox.showinfo('پیام موفقیت','حذف با موفقیت انجام شد')
            win_user.destroy()
        except:
            tk.messagebox.showerror('خطا','حذف با خطا مواجعه شد')
            win_user.destroy()
    
    save = tk.Button(win_user,text='حذف',command=delete,font="#2526")
    save.place(x=200,y=190)

    def back():
        win_user.destroy()

    back = tk.Button(win_user,text="بازگشت",command=back,font="#2526")
    back.place(x=250,y=190)
    
    def flistselect(event):
        global item
        item = list_u.curselection()
        
        lbferst_name.config(text=s[item[0]].ferst_name)
        lblast_name.config(text=s[item[0]].last_name)
        lbtel_1.config(text=s[item[0]].tel_1)
        lbtel_2.config(text=s[item[0]].tel_2)
        lbusername.config(text=s[item[0]].username)
        lbpassword.config(text=s[item[0]].password)
        lbshift.config(text=s[item[0]].shift)
        
        
    list_u.bind('<<ListboxSelect>>',flistselect)
    
    
submenu = Menu(setting, tearoff=0)
submenu.add_command(label="ساخت پنل کاربری جدید",accelerator="F7",command=form_user)
submenu.add_command(label="ویرایش پنل کاربری",command=edit_user)
submenu.add_command(label="حدف پنل کاربری",command=delete_user)
setting.add_cascade(label="ساخت پنل کاربری",menu=submenu)
#setting.add_separator()
#def theam():
   #pass
#setting.add_command(label="      تنظیمات ظاهری",accelerator="Ctrl+S",command=theam)

def darbare():
    win_darbare = tk.Toplevel()
    win_darbare.title("ارتباز با ما")
    win_darbare.geometry('350x240+400+200')
    win_darbare.configure(bg='#FFA500')

    tk.Label(win_darbare,text="progrmer:",bg="#FFA500").place(x=150,y=70)
    lbshift = tk.Label(win_darbare,text="S.M.J.Tghavi nasab",bg='#FFA500')
    lbshift.place(x=150,y=100)

    tk.Label(win_darbare,text="Email:",bg="#FFA500").place(x=150,y=130)
    lbshift = tk.Label(win_darbare,text="javad138016@gmail.com",bg='#FFA500')
    lbshift.place(x=150,y=150)
    
menubar.add_cascade(label="                                      ارتباط با ما             ",menu=darbare,command=darbare)
menubar.add_cascade(label="                                    راهنمای نرم افزار       ",menu=help_me)
menubar.add_cascade(label="                                    تنظیمات                     ",menu=setting)
menubar.add_cascade(label="                                  گزارشات                 ",menu=gozatesh)
menubar.add_cascade(label="                                  سایرعملیات              ",menu=sayeramliat)
menubar.add_cascade(label="                              اشخاص                   ",menu=people)
menubar.add_cascade(label="                                   تعاریف                    ",menu=tarif)

win.mainloop()