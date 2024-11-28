"การพัฒนาระบบคลังสินค้าของร้านคาเฟ่ ANDY Coffee and Friends"

โปรเจกต์นี้พัฒนาขึ้นเมื่อชั้นปีที่ 2 ช่วงเดือนมกราคม 2024 ในชุดวิชา DA

1.ติดตั้ง Python
https://www.python.org/downloads/

2.ติดตั้ง Pycharm (Community Edition สำหรับใช้งานฟรี)
https://www.jetbrains.com/pycharm/download/?section=windows
 
3.ติดตั้ง Appserv (หรือหากใช้เครื่องมืออื่น กรุณตั้งรหัสตามข้อ 4 )
https://www.appserv.org/en/download/

4.เข้า localhost (phpMyAdmin กรุณาใช้รหัสเข้าฐานข้อมูลตามนี้)
User : root
Password : 12345678
(หากรหัสไม่ตรง กรุณาเปลี่ยนรหัสใน phpmyadmin หรือหากต้องการใช้รหัสของตนเอง ต้องไปเปลี่ยนในโค้ด 24 จุด)

5.สร้างฐานข้อมูลชื่อ andy_dspro

6.import ไฟล์ andy_dspro.sql ที่อยู่ในโฟลเดอร์ Database

7.ติดตั้งฟอนต์ที่อยู่ในโฟล์เดอร์ Fonts

8.เปิดโฟลเดอร์ Python และเปิดไฟล์ Capstone Project Andy.py บน PyCharm

9.ติดตั้ง Python Packages ดังนี้
-pymysql
-pillow

10.รันโค้ด ใส่ข้อมูลผู้ใช้เพื่อเข้าโปรแกรมดังนี้ (แก้ไขได้ข้อมูล users ในโค้ด เริ่มที่ line 9)
user : admin 
password : andy 


