from tkinter import *
import tkinter as tk
from tkinter import ttk, Toplevel, Entry, messagebox, Button, END
import pymysql
from operator import itemgetter
from PIL import Image, ImageTk

# ตัวแปร global เพื่อเก็บข้อมูลผู้ใช้
users = {
    "admin": "andy",
}

def authenticate_user(event=None):
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        open_main_program()
    else:
        messagebox.showerror("Login", "Username or Password is incorrect.")

def open_main_program():
    login_window.destroy()

    # เรียกใช้โปรแกรมหลัก
    main_program()
################################################################################################
def main_program():

    def GetValue(event):  # รอรับเหตุการณ์คลิกเมาส์ที่ ลิสต์บ๊อค จากหน้าจอหลัก สำหรับการแก้ไขข้อมูล
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)

        selected_item = listBox.selection()

        if selected_item:
            row_id = selected_item[0]
            select = listBox.item(row_id)

            # ตรวจสอบว่า 'values' มีอยู่ใน select หรือไม่
            if 'values' in select:
                values = select['values']
                e1.insert(0, values[0])  # ใช้คีย์ที่ถูกสร้างจากคอลัมน์แรก
                e2.insert(0, values[1])
                e3.insert(0, values[2])
                e4.insert(0, values[3])
            else:
                messagebox.showinfo("Error", "No values found in selected item")
        else:
            messagebox.showinfo("Error", "No item selected")

    def add():  # ฟังก์ชันสำหรับเพิ่มข้อมูล
        andy_id = e1.get()
        andy_name = e2.get()
        andy_price = int(e3.get())
        andy_type = e4.get()

        db = pymysql.connect(host='localhost', db='andy_dspro', user='root',
                             passwd='12345678')  # เชื่อมต่อฐานข้อมูล
        cursor = db.cursor()

        try:
            sqlString = "INSERT INTO andy_menu (andy_id,andy_name,andy_price,andy_type) VALUES ('%s','%s', %d,'%s')" % (
                andy_id, andy_name, andy_price, andy_type)
            cursor.execute(sqlString)
            db.commit()
            messagebox.showinfo("ANDY MENU", "Added Successfully...")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)

            e1.focus_set()
        except Exception as e:
            print(e)
            db.rollback()
            db.close()

    def update():
        andy_id = e1.get()
        andy_name = e2.get()
        andy_price = int(e3.get())
        andy_type = e4.get()
        db = pymysql.connect(host='localhost', db='andy_dspro', user='root',
                             passwd='12345678')  # เชื่อมต่อฐานข้อมูล
        cursor = db.cursor()

        try:
            sqlString = "Update  andy_menu set andy_name='%s', andy_price=%d, andy_type='%s' where andy_id='%s'" % (
                andy_name, andy_price, andy_type, andy_id)
            cursor.execute(sqlString)
            db.commit()
            lastid = cursor.lastrowid
            messagebox.showinfo("ANDY MENU", " Updated successfully...")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)

            e1.focus_set()

        except Exception as e:

            print(e)
            db.rollback()
            db.close()

    def delete():  # ฟังก์ชันสำหรับลบข้อมูล
        andy_id = e1.get()

        db = pymysql.connect(host='localhost', db='andy_dspro', user='root',
                             passwd='12345678')  # เชื่อมต่อฐานข้อมูล
        cursor = db.cursor()

        try:
            sqlString = "delete from andy_menu where andy_id = '%s'" % (andy_id)
            cursor.execute(sqlString)
            db.commit()
            lastid = cursor.lastrowid
            messagebox.showinfo("ANDY MENU", "Deleted successfully...")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e1.focus_set()

        except Exception as e:
            print(e)
            db.rollback()
            db.close()

    # แก้ไขฟังก์ชัน sort_by_column
    def sort_by_column(column):
        db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
        cursor = db.cursor()
        sqlString = "SELECT * FROM andy_menu"
        cursor.execute(sqlString)
        records = cursor.fetchall()
        db.close()

        # เคลียร์ข้อมูลใน ListBox
        for item in listBox.get_children():
            listBox.delete(item)

        # แสดงข้อมูลใหม่ลงใน ListBox โดยเรียงตามคอลัมน์ที่ผู้ใช้เลือก
        if column == 'andy_name':
            # ถ้าผู้ใช้เลือกเรียงตามชื่อเมนู
            sorted_records = sorted(records, key=lambda x: x[1])  # เรียงตามคอลัมน์ 'andy_name'

        else:
            # ถ้าไม่ใช่การเรียงตามชื่อเมนูให้เรียงตามคอลัมน์ที่ผู้ใช้เลือกเดิม
            sorted_records = sorted(records, key=lambda x: x[2])  # เรียงตามคอลัมน์ 'andy_price'

        for i, (andy_id, andy_name, andy_price, andy_type) in enumerate(sorted_records, start=1):
            listBox.insert("", "end", values=(andy_id, andy_name, andy_price, andy_type))

    def show():
        db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
        cursor = db.cursor()
        sqlString = "SELECT * FROM andy_menu"
        cursor.execute(sqlString)
        records = cursor.fetchall()

        # เคลียร์ข้อมูลใน ListBox
        for item in listBox.get_children():
            listBox.delete(item)

        # แสดงข้อมูลใหม่ลงใน ListBox
        for i, (andy_id, andy_name, andy_price, andy_type) in enumerate(sorted(records, key=itemgetter(0)), start=1):
            listBox.insert("", "end", values=(andy_id, andy_name, andy_price, andy_type))

        db.close()

    root = Tk()
    root.title("ANDY Coffee and Friends")
    root.geometry("1200x600")
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6

    tk.Label(root, text="ANDY", fg="Blue", font=("HACKED", 50)).place(x=450, y=20)
    tk.Label(root, text="MENU", fg="Red", font=("HACKED", 50)).place(x=600, y=20)
    #a=0.00
    tk.Label(root, text="Menu ID : ").place(x=100, y=110)
    tk.Label(root, text="Menu Name : ").place(x=100, y=140)
    tk.Label(root, text="Menu Price : ").place(x=100, y=170)
    tk.Label(root, text="Menu Type : ").place(x=100, y=200)
    #a = a.calculate_sale_sum()
    #tk.Label(root, text=f"ยอดขาย:" ,a).place(x=100, y=120)

    e1 = Entry(root)
    e1.place(x=200, y=110)

    e2 = Entry(root)
    e2.place(x=200, y=140)

    e3 = Entry(root)
    e3.place(x=200, y=170)

    e4 = Entry(root)
    e4.place(x=200, y=200)

    # ปุ่มสำหรับรอรับเหตุการ คลิกแล้วทำงานโดยการเรียกฟังก์ชันตามปุ่มที่กำหนด
    Button(root, text="<< Add >>", command=add, height=3, width=13, foreground='#006600').place(x=350, y=105)
    Button(root, text="<< Update >>", command=update, height=3, width=13, foreground='blue').place(x=350, y=165)
    Button(root, text="<< Delete >>", command=delete, height=3, width=13, foreground='red').place(x=460, y=105)

    # และในปุ่ม Sort by Name ให้เรียกใช้ sort_by_column ดังนี้
    Button(root, text="<< Sort by Name >>", command=lambda: sort_by_column('andy_name'), height=1, width=34,
           bg="#ccffff", foreground='#000000', ).place(x=350, y=250)

    # สร้าง ttk.Style
    style = ttk.Style()
    style.configure("Treeview.Heading", bg="red", foreground='#FF0000', font=('', 14, 'bold'))
    # ข้อมูลที่ถูกเรียกขขึ้นมาแสดงผลบนลิสต์บ๊อคจากตารางฐานข้อมูล
    cols = ('รหัสเมนู', 'ชื่อเมนู', 'ราคา (บาท)', 'ประเภท')
    listBox = ttk.Treeview(root, columns=cols, show='headings')
    # ข้อมูลที่ถูกเรียกขขึ้นมาแสดงผลบนลิสต์บ๊อค
    for col in cols:
        listBox.heading(col, text=col, anchor='center')
        listBox.column(col, anchor='center')  # ตั้งค่าคอลัมน์ให้อยู่ในตำแหน่งกลาง
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=100, y=280, width=1000)

    show()

    listBox.bind('<Double-Button-1>', GetValue)  # รอรับเหตุการณ์ที่ผู้ใช้คลิกที่ข้อมูลบน ลิสต์บ๊อค

    def open_sale_window():

        global listBox_sale
        global selected_sale_id
        global sum_label
        global total_sale_sum

        def calculate_sale_sum():
            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT SUM(sale_price * sale_count) FROM andy_sale"
            cursor.execute(sqlString)
            total_sale_sum_tuple = cursor.fetchone()
            total_sale_sum = total_sale_sum_tuple[0] if total_sale_sum_tuple is not None else 0
            db.close()
            return total_sale_sum

        def clear_entries():
            e1_sale.delete(0, END)
            e2_sale.delete(0, END)
            e3_sale.delete(0, END)


        def show_sale_records():
            global total_sale_sum
            total_sale_sum = calculate_sale_sum()
            sum_label.config(text=f"รวมยอดขาย: {total_sale_sum:.2f}", foreground="#00cc00", font=("", 30))
            sum_label.place(x=400, y=120)

            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT * FROM andy_sale"
            cursor.execute(sqlString)
            records = cursor.fetchall()

            for item in listBox_sale.get_children():
                listBox_sale.delete(item)

            for i, record in enumerate(sorted(records, key=itemgetter(0)), start=1):
                sale_id, sale_price, sale_count = record
                listBox_sale.insert("", "end", values=(sale_id, f'%.2f' % sale_price, sale_count))

            db.close()

            clear_entries()

        sale_window = tk.Toplevel(root)
        sale_window.title("Sale - ANDY Coffee and Friends")
        sale_window.geometry("800x600")

        e2_sale = tk.Entry(sale_window)
        e3_sale = tk.Entry(sale_window)

        tk.Label(sale_window, text="Menu ID : ").place(x=100, y=120)
        tk.Label(sale_window, text="Menu Price: ").place(x=100, y=150)
        tk.Label(sale_window, text="Menu Count : ").place(x=100, y=180)

        e1_sale = tk.Entry(sale_window)
        e1_sale.place(x=200, y=120)

        e2_sale = tk.Entry(sale_window)
        e2_sale.place(x=200, y=150)

        e3_sale = tk.Entry(sale_window)
        e3_sale.place(x=200, y=180)

        listBox_sale = ttk.Treeview(sale_window, columns=('Sale ID', 'Sale Price', 'Sale Count'), show='headings')
        listBox_sale.heading('Sale ID', text='รหัสเมนู', anchor='center')
        listBox_sale.column('Sale ID', anchor='center')
        listBox_sale.heading('Sale Price', text='ราคา (บาท)', anchor='center')
        listBox_sale.column('Sale Price', anchor='center')
        listBox_sale.heading('Sale Count', text='จำนวน', anchor='center')
        listBox_sale.column('Sale Count', anchor='center')
        listBox_sale.grid(row=1, column=0, columnspan=2)
        listBox_sale.place(x=100, y=300)

        sum_label = tk.Label(sale_window, text="")
        sum_label.place(x=200, y=220)

        tk.Label(sale_window, text="ANDY", fg="Blue", font=("HACKED", 50)).place(x=260, y=20)
        tk.Label(sale_window, text="SALE", fg="Red", font=("HACKED", 50)).place(x=410, y=20)

        show_sale_records()

        def on_sale_select(event):
            global selected_sale_id
            selected_item = listBox_sale.selection()
            if selected_item:
                item = listBox_sale.item(selected_item)
                selected_sale_id = item['values'][0]

                e1_sale.delete(0, END)
                e1_sale.insert(0, selected_sale_id)

                db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
                cursor = db.cursor()
                sqlString = f"SELECT sale_price, sale_count FROM andy_sale WHERE sale_id = '{selected_sale_id}'"
                cursor.execute(sqlString)
                record = cursor.fetchone()

                if record:
                    sale_price, sale_count = record
                    e2_sale.delete(0, END)
                    e2_sale.insert(0, f'%.2f' % sale_price)
                    e3_sale.delete(0, END)
                    e3_sale.insert(0, sale_count)

                db.close()

        def add_sale():
            sale_id = e1_sale.get()
            sale_count_str = e3_sale.get()

            if sale_count_str:
                sale_count = int(sale_count_str)
            else:
                sale_count = 0

            sale_price = float(e2_sale.get())

            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()

            try:
                sqlString = "INSERT INTO andy_sale (sale_id, sale_count, sale_price) VALUES (%s, %s, %s)"
                cursor.execute(sqlString, (sale_id, sale_count, f'%.2f' % sale_price))
                db.commit()
                messagebox.showinfo("Sale", "Sale added successfully...")
                e1_sale.delete(0, END)
                e2_sale.delete(0, END)
                e3_sale.delete(0, END)
                show_sale_records()

                e1_sale.focus_set()
            except Exception as e:
                print(e)
                db.rollback()
            finally:
                db.close()

        def update_sale():
            sale_id = e1_sale.get()
            sale_price = float(e2_sale.get())

            sale_count_str = e3_sale.get()
            if sale_count_str:
                sale_count = int(sale_count_str)
            else:
                sale_count = 0

            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()

            try:
                sqlString = "UPDATE andy_sale SET sale_price=%s, sale_count=%s WHERE sale_id=%s"
                cursor.execute(sqlString, (f'%.2f' % sale_price, sale_count, sale_id))
                db.commit()
                messagebox.showinfo("Sale", "Sale updated successfully...")
                show_sale_records()
            except Exception as e:
                print(e)
                db.rollback()
            finally:
                db.close()

        def delete_sale():
            sale_id = e1_sale.get()

            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()

            try:
                sqlString = "DELETE FROM andy_sale WHERE sale_id=%s"
                cursor.execute(sqlString, sale_id)
                db.commit()
                messagebox.showinfo("Sale", "Sale deleted successfully...")
                e1_sale.delete(0, END)
                e2_sale.delete(0, END)
                e3_sale.delete(0, END)
                show_sale_records()

                e1_sale.focus_set()
            except Exception as e:
                print(e)
                db.rollback()
            finally:
                db.close()

        def sort_by_count():
            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT * FROM andy_sale ORDER BY sale_count DESC"
            cursor.execute(sqlString)
            records = cursor.fetchall()

            for item in listBox_sale.get_children():
                listBox_sale.delete(item)

            for i, record in enumerate(records, start=1):
                sale_id, sale_price, sale_count = record
                listBox_sale.insert("", "end", values=(sale_id, f'%.2f' % sale_price, sale_count))

            db.close()

        def sort_by_price():
            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT * FROM andy_sale ORDER BY sale_price DESC"
            cursor.execute(sqlString)
            records = cursor.fetchall()

            for item in listBox_sale.get_children():
                listBox_sale.delete(item)

            for i, record in enumerate(records, start=1):
                sale_id, sale_price, sale_count = record
                listBox_sale.insert("", "end", values=(sale_id, f'%.2f' %  sale_price, sale_count))

            db.close()

        def sort_by_id():
            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT * FROM andy_sale "
            cursor.execute(sqlString)
            records = cursor.fetchall()
            db.close()

            for item in listBox_sale.get_children():
                listBox_sale.delete(item)

            sorted_records = sorted(records, key=lambda x: (x[0].isdigit(), x[0]))

            for i, record in enumerate(sorted_records, start=1):
                sale_id, sale_price, sale_count = record
                listBox_sale.insert("", "end", values=(sale_id, f'%.2f' % sale_price, sale_count))

        listBox_sale.bind("<ButtonRelease-1>", on_sale_select)

        tk.Button(sale_window, text="<< Sort by Count >>", command=sort_by_count, height=1, width=27, bg="#ccffff",
                  foreground='#000000').place(
            x=504, y=270)
        tk.Button(sale_window, text="<< Sort by Price >>", command=sort_by_price, height=1, width=27, bg="#ccffff",
                  foreground='#000000').place(
            x=300, y=270)
        tk.Button(sale_window, text="<< Sort by ID >>", command=sort_by_id, height=1, width=27, bg="#ccffff",
                  foreground='#000000').place(
            x=100, y=270)

        tk.Button(sale_window, text="<< Add Sale >>", command=add_sale, height=3, width=14, foreground='#006600').place(
            x=100, y=210)
        tk.Button(sale_window, text="<< Update Sale >>", command=update_sale, height=3, width=14,
                  foreground='blue').place(
            x=210, y=210)
        tk.Button(sale_window, text="<< Delete Sale >>", command=delete_sale, height=3, width=14,
                  foreground='red').place(
            x=320, y=210)
        tk.Button(sale_window, text="<< Refresh Sale >>", command=show_sale_records, height=3, width=14,
                  foreground='purple').place(x=430, y=210)

    Button(root, text="<< Sale >>", foreground='#FF0099', command=open_sale_window, height=5, width=14,
           font=("", 12, "bold")).place(x=580, y=110)

    # สร้างหน้าต่าง Stock
    def open_stock_window():
        global total_stock_sum
        def clear_entries():
            e1_stock.delete(0, END)
            e2_stock.delete(0, END)
            e3_stock.delete(0, END)
            e4_stock.delete(0, END)
            e5_stock.delete(0, END)
            e6_stock.delete(0, END)

        stock_window = Toplevel(root)
        stock_window.title("Stock - ANDY Coffee and Friends")
        stock_window.geometry("1300x520")
        tk.Label(stock_window, text="Stock ID: ").place(x=50, y=30)
        tk.Label(stock_window, text="Stock Name: ").place(x=50, y=60)
        tk.Label(stock_window, text="Stock Count: ").place(x=50, y=90)
        tk.Label(stock_window, text="Stock Price: ").place(x=50, y=120)
        tk.Label(stock_window, text="Stock Purchase: ").place(x=50, y=150)
        tk.Label(stock_window, text="Stock Exp: ").place(x=50, y=180)

        tk.Label(stock_window, text="ANDY", fg="Blue", font=("HACKED", 50)).place(x=500, y=20)
        tk.Label(stock_window, text="STOCK", fg="Red", font=("HACKED", 50)).place(x=650, y=20)

        e1_stock = Entry(stock_window)
        e1_stock.place(x=150, y=30)

        e2_stock = Entry(stock_window)
        e2_stock.place(x=150, y=60)

        e3_stock = Entry(stock_window)
        e3_stock.place(x=150, y=90)

        e4_stock = Entry(stock_window)
        e4_stock.place(x=150, y=120)

        e5_stock = Entry(stock_window)
        e5_stock.place(x=150, y=150)

        e6_stock = Entry(stock_window)
        e6_stock.place(x=150, y=180)

        cols_stock = ('รหัสสินค้า', 'รายการสินค้า', 'จำนวน', 'ราคาต่อหน่วย (บาท)', 'วันที่ซื้อสินค้า', 'วันหมดอายุ')

        listBox_stock = ttk.Treeview(stock_window, columns=cols_stock, show='headings')
        for col_stock in cols_stock:
            listBox_stock.heading(col_stock, text=col_stock, anchor='center')
            listBox_stock.column(col_stock, anchor='center')
            listBox_stock.grid(row=1, column=0, columnspan=2)
            listBox_stock.place(x=50, y=250)

        # เพิ่มฟังก์ชัน on_select
        def on_select(event):
            selected_row = listBox_stock.selection()
            if selected_row:
                values = listBox_stock.item(selected_row)['values']
                e1_stock.delete(0, END)
                e2_stock.delete(0, END)
                e3_stock.delete(0, END)
                e4_stock.delete(0, END)
                e5_stock.delete(0, END)
                e6_stock.delete(0, END)

                e1_stock.insert(0, values[0])
                e2_stock.insert(0, values[1])
                e3_stock.insert(0, values[2])
                e4_stock.insert(0, values[3])
                e5_stock.insert(0, values[4])
                e6_stock.insert(0, values[5])

        # ผูกฟังก์ชัน on_select กับการเลือกใน listBox_stock
        listBox_stock.bind('<<TreeviewSelect>>', on_select)

        def calculate_stock_sum():
            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT SUM(stock_price * stock_count) FROM andy_stock"
            cursor.execute(sqlString)
            total_stock_sum_tuple = cursor.fetchone()
            total_stock_sum = total_stock_sum_tuple[0] if total_stock_sum_tuple is not None else 0
            db.close()
            return total_stock_sum

        def show_stock_records():
            global total_stock_sum
            total_stock_sum = calculate_stock_sum()
            sum_label.config(text=f"รวมราคาสินค้า: {total_stock_sum:.2f}", foreground="#00cc00", font=("", 30))
            sum_label.place(x=480, y=100)

            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT * FROM andy_stock"
            cursor.execute(sqlString)
            records_stock = cursor.fetchall()

            for item_stock in listBox_stock.get_children():
                listBox_stock.delete(item_stock)

            for i_stock, (stock_id, stock_name, stock_count, stock_price, stock_buy, stock_exp) in enumerate(
                    records_stock,
                    start=1):
                listBox_stock.insert("", "end", values=(
                    stock_id, stock_name, stock_count, f'%.2f' % stock_price, stock_buy, stock_exp))

            db.close()
            clear_entries()

        sum_label = tk.Label(stock_window, text="")
        sum_label.place(x=350, y=100)
        show_stock_records()

        def add_stock():
            stock_id = e1_stock.get()
            stock_name = e2_stock.get()
            stock_count = int(e3_stock.get())
            stock_price = float(e4_stock.get())
            stock_buy = e5_stock.get()
            stock_exp = e6_stock.get()

            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()

            try:
                sqlString = "INSERT INTO andy_stock (stock_id, stock_name, stock_count, stock_price, stock_buy, stock_exp) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sqlString, (stock_id, stock_name, stock_count, stock_price, stock_buy, stock_exp))
                db.commit()
                messagebox.showinfo("Stock", "Stock added successfully...")
                e1_stock.delete(0, END)
                e2_stock.delete(0, END)
                e3_stock.delete(0, END)
                e4_stock.delete(0, END)
                e5_stock.delete(0, END)
                e6_stock.delete(0, END)
                show_stock_records()
                e1_stock.focus_set()
            except Exception as e_stock:
                print(e_stock)
                db.rollback()
            finally:
                db.close()

        def update_stock():
            stock_id = e1_stock.get()
            stock_name = e2_stock.get()
            stock_count = int(e3_stock.get())
            stock_price = float(e4_stock.get())
            stock_buy = e5_stock.get()
            stock_exp = e6_stock.get()

            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()

            try:
                sqlString = "UPDATE andy_stock SET stock_name=%s, stock_count=%s, stock_price=%s, stock_buy=%s, stock_exp=%s WHERE stock_id=%s"
                cursor.execute(sqlString, (stock_name, stock_count, stock_price, stock_buy, stock_exp, stock_id))
                db.commit()
                messagebox.showinfo("Stock", "Stock updated successfully...")
                show_stock_records()
                clear_entries()
            except Exception as e_stock:
                print(e_stock)
                db.rollback()
            finally:
                db.close()

        def delete_stock():
            stock_id = e1_stock.get()

            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()

            try:
                sqlString = "DELETE FROM andy_stock WHERE stock_id=%s"
                cursor.execute(sqlString, stock_id)
                db.commit()
                messagebox.showinfo("Stock", "Stock deleted successfully...")
                clear_entries()
                show_stock_records()
                e1_stock.focus_set()
            except Exception as e_stock:
                print(e_stock)
                db.rollback()
            finally:
                db.close()

        def clear_entries():
            e1_stock.delete(0, END)
            e2_stock.delete(0, END)
            e3_stock.delete(0, END)
            e4_stock.delete(0, END)
            e5_stock.delete(0, END)
            e6_stock.delete(0, END)

        def sort_by_purchase_date():
            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT * FROM andy_stock ORDER BY stock_buy ASC"  # เรียงตามวันที่ซื้อ (ASC: จากน้อยไปมาก,DESC: จากมากไปน้อย)
            cursor.execute(sqlString)
            records_stock = cursor.fetchall()

            for item_stock in listBox_stock.get_children():
                listBox_stock.delete(item_stock)

            for i_stock, (
                    stock_id, stock_name, stock_count, stock_price, stock_buy, stock_exp) in enumerate(
                records_stock,
                start=1):
                listBox_stock.insert("", "end", values=(
                    stock_id, stock_name, stock_count, f'%.2f' % stock_price, stock_buy, stock_exp))

            db.close()
            clear_entries()

        def sort_by_expiry_date():
            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT * FROM andy_stock ORDER BY stock_exp ASC"  # เรียงตามวันที่ซื้อ (ASC: จากน้อยไปมาก,DESC: จากมากไปน้อย)
            cursor.execute(sqlString)
            records_stock = cursor.fetchall()

            for item_stock in listBox_stock.get_children():
                listBox_stock.delete(item_stock)

            for i_stock, (
                    stock_id, stock_name, stock_count, stock_price, stock_buy, stock_exp) in enumerate(
                records_stock,
                start=1):
                listBox_stock.insert("", "end", values=(
                    stock_id, stock_name, stock_count, f'%.2f' % stock_price, stock_buy, stock_exp))

            db.close()
            clear_entries()

        Button(stock_window, text="<< Add Stock >>", command=add_stock, height=3, width=14, foreground='#006600').place(
            x=430, y=160)
        Button(stock_window, text="<< Update Stock >>", command=update_stock, height=3, width=14,
               foreground='Blue').place(x=540, y=160)
        Button(stock_window, text="<< Delete Stock >>", command=delete_stock, height=3, width=14,
               foreground='Red').place(x=650, y=160)
        Button(stock_window, text="<< Refresh Stock >>", command=show_stock_records, height=3, width=14,
               foreground='Purple').place(x=760, y=160)
        Button(stock_window, text="<< Sort by Purchase Date >>", command=sort_by_purchase_date, height=1, width=27,
               bg="#ccffff",
               foreground='#000000').place(x=850, y=220)
        Button(stock_window, text="<< Sort by Expiry Date >>", command=sort_by_expiry_date, height=1, width=27,
               bg="#ccffff",
               foreground='#000000').place(
            x=1053, y=220)

    # เพิ่มปุ่มเรียกหน้าต่าง Stock
    Button(root, text="<< Stock >>", foreground='#FF0099', command=open_stock_window, height=5, width=14,
           font=("", 12, "bold")).place(x=735, y=110)

    def refresh_list():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        # เคลียร์ลิสต์บ๊อค
        for item in listBox.get_children():
            listBox.delete(item)
        # แสดงข้อมูลใหม่
        show()

    # เพิ่มปุ่มรีเฟรช
    Button(root, text="<< Refresh >>", command=refresh_list, height=3, width=13, foreground='purple').place(x=460,
                                                                                                            y=165)



    sort_button = Button(root, text="<< Sort by Price >>", command=lambda: sort_by_column(2), height=1, width=34,
                         bg="#ccffff", foreground='#000000')
    sort_button.place(x=600, y=250)

    # ฟังก์ชัน sort_by_type
    def sort_by_type():
        # รับค่าประเภทที่ต้องการเรียง
        selected_type = e4.get()

        # ถ้าไม่ได้ระบุประเภทให้แสดงข้อความแจ้งเตือน
        if not selected_type:
            messagebox.showinfo("Error", "Please enter a type for sorting")
            return

        # เชื่อมต่อกับฐานข้อมูล
        db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
        cursor = db.cursor()

        # คำสั่ง SQL สำหรับดึงข้อมูลทั้งหมดจากตาราง andy_menu ที่มีประเภทตรงกับที่ระบุ
        sqlString = f"SELECT * FROM andy_menu WHERE andy_type = '{selected_type}'"
        cursor.execute(sqlString)
        records = cursor.fetchall()

        # เคลียร์ข้อมูลใน ListBox
        for item in listBox.get_children():
            listBox.delete(item)

        # แสดงข้อมูลใหม่ลงใน ListBox
        for i, (andy_id, andy_name, andy_price, andy_type) in enumerate(records, start=1):
            listBox.insert("", "end", values=(andy_id, andy_name, andy_price, andy_type))

        # ปิดการเชื่อมต่อกับฐานข้อมูล
        db.close()

    Button(root, text="<< Sort by Type >>", command=sort_by_type, height=1, width=34, bg="#ccffff",
           foreground='#000000').place(x=850, y=250)

    def sort_by_id():
        db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
        cursor = db.cursor()
        sqlString = "SELECT * FROM andy_menu"
        cursor.execute(sqlString)
        records = cursor.fetchall()
        db.close()

        # เคลียร์ข้อมูลใน ListBox
        for item in listBox.get_children():
            listBox.delete(item)

        # แสดงข้อมูลใหม่ลงใน ListBox โดยเรียงตาม andy_id
        sorted_records = sorted(records, key=lambda x: (x[0].isdigit(), x[0]))

        for i, (andy_id, andy_name, andy_price, andy_type) in enumerate(sorted_records, start=1):
            listBox.insert("", "end", values=(andy_id, andy_name, andy_price, andy_type))

    # เพิ่มปุ่ม Sort By ID และเชื่อมกับฟังก์ชัน sort_by_id
    Button(root, text="<< Sort By ID >>", command=sort_by_id, height=1, width=34, bg="#ccffff",
           foreground='#000000').place(x=100, y=250)


########################################

    def open_profit_window():
        global total_sale_sum, total_stock_sum
        profit_window = Toplevel(root)
        profit_window.title("Calculate Profit")
        profit_window.geometry("300x300")

        tk.Label(profit_window, text="Sales: ").place(x=50, y=30)
        tk.Label(profit_window, text="Stock: ").place(x=50, y=60)

        e1_sale = Entry(profit_window)
        e1_sale.insert(0, f'%.2f' % total_sale_sum)
        e1_sale.config(state='readonly')
        e1_sale.place(x=100, y=30)

        e2_sale = Entry(profit_window)
        e2_sale.insert(0, f'%.2f' % total_stock_sum)
        e2_sale.config(state='readonly')
        e2_sale.place(x=100, y=60)

        def calculate_profit():
            global total_sale_sum, total_stock_sum

            # ตรวจสอบว่าข้อมูลที่รับเข้ามาเป็นตัวเลขหรือไม่
            try:
                total_sale_sum = float(e1_sale.get())
                total_stock_sum = float(e2_sale.get())
            except ValueError:
                total_sale_sum = 0
                total_stock_sum = 0

            profit = total_sale_sum - total_stock_sum

            # แสดงผลลัพธ์
            result_label.config(text=f"Profit: {profit:.2f}", font=("", 20), foreground="#006600")

        result_label = tk.Label(profit_window, text="")
        result_label.place(x=100, y=120)

        # ฟังก์ชันสำหรับดึงข้อมูล Sale จากฐานข้อมูล
        def fetch_sales_from_database():
            db = pymysql.connect(host='localhost', db='andy_dspro', user='root', passwd='12345678')
            cursor = db.cursor()
            sqlString = "SELECT * FROM andy_sale"
            cursor.execute(sqlString)
            records = cursor.fetchall()
            db.close()
            return records

        def print_report():
            global total_sale_sum, total_stock_sum

            try:
                total_sale_sum = float(e1_sale.get())
                total_stock_sum = float(e2_sale.get())
            except ValueError:
                total_sale_sum = 0
                total_stock_sum = 0

            profit = total_sale_sum - total_stock_sum

            # ดึงข้อมูล Sale จากฐานข้อมูล
            sales_data = fetch_sales_from_database()

            report_window = tk.Toplevel(root)
            report_window.title("Report - ANDY Coffee and Friends")

            tree = ttk.Treeview(report_window, columns=('Sale ID', 'Price', 'Count'), show='headings')
            tree.heading('Sale ID', text='Sale ID')
            tree.heading('Price', text='Price')
            tree.heading('Count', text='Count')

            tree.grid(row=0, column=0, sticky='nsew')

            # แสดงข้อมูลในตาราง
            for sale_record in sales_data:
                tree.insert("", "end", values=(sale_record[0], f'{sale_record[1]:.2f}', sale_record[2]))

            tk.Label(report_window, text=f"Total Sales: {total_sale_sum:.2f}").grid(row=1, column=0, pady=5)
            tk.Label(report_window, text=f"Total Stock: {total_stock_sum:.2f}").grid(row=2, column=0, pady=5)
            tk.Label(report_window, text=f"Profit: {profit:.2f}").grid(row=3, column=0, pady=5)

            tk.Button(report_window, text="Close", command=report_window.destroy).grid(row=4, column=0, pady=10)




        Button(profit_window, text="Calculate Profit", command=calculate_profit).place(x=100, y=90)
        Button(profit_window, text="Print Report", command=print_report).place(x=100, y=170)



    Button(root, text="<< Calculate Profit >>\n [ กรุณาเปิด Sale และ Stock ก่อน ] ", command=open_profit_window, foreground='Green',height=5, width=20,

           font=("TH SarabunPSK", 12, "bold")).place(x=890, y=110)






    # ยืนยันการปิดโปรแกรม
    def on_closing():
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            root.destroy()

    # ตั้งค่าให้ root รองรับกดปุ่ม ESC
    root.bind('<Escape>', lambda event: on_closing())

    # ในส่วนที่สร้างหน้าต่าง root
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

################################################################################################

# สร้างหน้าต่าง login
login_window = tk.Tk()
login_window.title("ANDY Login")
login_window.geometry("500x600")

# เพิ่มโลโก้
logo_image = Image.open("andylogo.png")  # แทนที่ path/to/your/logo.png ด้วยที่อยู่ของไฟล์รูปภาพของคุณ
logo_image = logo_image.resize((200, 200))  # ปรับขนาดรูปภาพตามต้องการ
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = Label(login_window, image=logo_photo)
logo_label.pack()

# เพิ่มข้อความ "ANDY" และ "Login"
label_andy = Label(login_window, text="ANDY", fg="Blue", font=("HACKED", 50))
label_andy.pack()

label_login = Label(login_window, text="Login", fg="Red", font=("HACKED", 50))
label_login.pack()

# สร้างองค์ประกอบ GUI
label_username = tk.Label(login_window, text="Username:", font=("PrintAble4U", 16, "bold"))
label_username.pack(pady=5)


entry_username = tk.Entry(login_window, font=("PrintAble4U", 16))
entry_username.pack(pady=5)
entry_username.bind("<Return>", authenticate_user)

label_password = tk.Label(login_window, text="Password:", font=("PrintAble4U", 16, "bold"))
label_password.pack(pady=5)

entry_password = tk.Entry(login_window, show="*", font=("PrintAble4U", 16))
entry_password.pack(pady=5)
entry_password.bind("<Return>", authenticate_user)

btn_login = tk.Button(login_window, text="Login", command=authenticate_user, font=("PrintAble4U", 16, "bold"))
btn_login.pack(pady=10)


# ให้โปรแกรมทำงานตลอดเวลา
login_window.mainloop()


