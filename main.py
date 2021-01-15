from models import contact
import threading
import tkinter as tk
from models import contact_table
from models import virus as horse
from tkinter import *
import subprocess
import json
import qrcode
from PIL import ImageTk, Image

isi_kontak = ''
isi_data = ''
nama = ''
telp = ''
email = ''
umur = ''
alamat = ''

uang= ''
def create_new_window_for_terms():
    newWin = Toplevel(root)
    isi = '''
    -------------------------
	APLIKASI PENDAFTARAN SISWA
	-------------------------
	DICIPTAKAN PADA TANGGAL 11/3/2020
	TUJUAN DIBUATNYA DIGUNAKAN UNTUK MENDAFTARKAN DIRI SECARA MANDIRI
	[1]Uang Yg Dibayarkan Harus Mencukupi Dengan Total Yg Diminta
	[2]Tidak Merusak Barcode
	[3]Jika rusak biaya cetak ulang adalah 50 ribu
	
	
	
		TERIMA KASIH
	'''
    LabelSing(newWin,isi)
def createNewWindowforDaftar():
    newWindowsss = Toplevel(root)
    enama = Entry(newWindowsss)
    enama.insert(END,'ISI NAMA')
    etelp = Entry(newWindowsss)
    etelp.insert(END,'ISI NO TELPON')
    eemail = Entry(newWindowsss)
    eemail.insert(END,'ISI EMAIL KAMU')
    eumur = Entry(newWindowsss)
    eumur.insert(END,'ISI UMUR KAMU')
    ealamat = Entry(newWindowsss)
    ealamat.insert(END,'ISI ALAMAT KAMU')
    euang = Entry(newWindowsss)
    euang.insert(END,'ISI 1000_000')
    def show_entry_fields111():



        global nama
        global  telp
        global email
        global umur
        global alamat

        global uang
        nama = str(enama.get())
        telp =str(etelp.get())
        email = str(eemail.get())
        umur = str(eumur.get())
        alamat = str(ealamat.get())

        uang = str(euang.get())
    global nama,telp,email,umur,alamat
    jawaban = tk.Button(newWindowsss, text='KUNCI PILIHAN', padx=27, pady=-5, command=show_entry_fields111)
    def buat():
        contact_table.data[nama] = {
            "telp": telp,
            "email": email,
            "umur": umur,
            "alamat": alamat,

        }

        contact_table.data[nama] = {
            "telp": telp,
            "email": email,
            'umur': umur,
            'alamat': alamat,

        }
        pembayaran(uang, '1000000')




    jawaban.grid(row=2, column=0)
    BUAT = tk.Button(newWindowsss, text='BUAT AKUN', padx=27, pady=-5, command=buat)
    enama.grid(row=0, column=0)
    etelp.grid(row=0, column=1)
    eemail.grid(row=0, column=2)
    eumur.grid(row=1, column=0)
    ealamat.grid(row=1, column=1)
    euang.grid(row=1,column=2)
    BUAT.grid(row=2,column=1)



def pembayaran(uang, bayaran):
    newwindowsss = Toplevel(root)
    if uang < bayaran:
        LabelSing(newwindowsss,'Uang Kurang Bayar Ulang')



    elif uang > bayaran:
        LabelSing(newwindowsss,f'Uang Lebih {int(uang)-int(bayaran)}')




        data_barcode = contact.randoming_string()
        nama = data_barcode
        LabelSing(newwindowsss,data_barcode)

        with open('data/barcode_data.txt', 'a') as outfile:
            outfile.write(f'{data_barcode}\n')
            isi = outfile.read().splitlines()
        while nama in isi :
            nama = contact.randoming_string()
        isi_dir = subprocess.check_output('ls \project_willson\data').decode('utf-8').split('\n')

        del isi_dir[len(isi_dir) - 1]
        while (f'{nama}.png') in isi_dir:
            nama = contact.randoming_string
        img = qrcode.make(data_barcode)

        img.save(f'data/{nama}.png')

        img.show(f'data/{nama}.png')
        with open('data/data.json', 'w') as fp:
            json.dump(contact_table.data, fp)




    elif uang == '1000000':
        LabelSing(newwindowsss,'Uang pas')





        data_barcode = contact.randoming_string()
        nama = data_barcode
        LabelSing(newwindowsss,nama)
        with open('data/barcode_data.txt', 'a') as outfile:
            outfile.write(f'{data_barcode}\n')
            isi=  outfile.read().splitlines()
        while nama in isi:
            nama = contact.randoming_string()
        isi_dir = subprocess.check_output('ls \project_willson\data').decode('utf-8').split('\n')

        del isi_dir[len(isi_dir) - 1]
        while (f'{nama}.png') in isi_dir:
            nama = contact.randoming_string
        img = qrcode.make(data_barcode)

        img.save(f'data/{nama}.png')

        img.show(f'data/{nama}.png')
        with open('data/data.json', 'w') as fp:
            json.dump(contact_table.data, fp)


def createNewWindowforCariData():
    newWindowss = Toplevel(root)
    e1 = Entry(newWindowss)
    global isi_kontak
    def show_entry_fields():
        isi_jawaban = (str(e1.get()))



        global isi_kontak
        isi_kontak = isi_jawaban

    def cari_data1(contact):

        newWindows = Toplevel(root)
        if contact in contact_table.data:

            LabelSing(newWindows, "- RESULT -")
            LabelSing(newWindows, text=f"Nama:{contact}")
            LabelSing(newWindows, text=f'Telp:{contact_table.data[contact]["telp"]}')
            LabelSing(newWindows, text=f'Email:{contact_table.data[contact]["email"]}')
            LabelSing(newWindows, text=f'Umur:{contact_table.data[contact]["umur"]}')
            LabelSing(newWindows, text=f'Alamat:{contact_table.data[contact]["alamat"]}')

            return True
        else:
            LabelSing(newWindows, text='tidk ditemukan')
            return False

    e1.insert(10,"SIAPA YANG INGIN DICARI")
    e1.grid(row=0, column=1)
    jawaban = tk.Button(newWindowss, text='NAMA',padx=27,pady=-5, command=show_entry_fields)
    jawaban.grid(row=0, column=0)

    cari_data =Button(newWindowss,text="CARI_DATA",padx=27,pady=1,command=lambda:cari_data1(isi_kontak))
    cari_data.grid(row=1,column=1)
def createNewWindow():
    newWindow = tk.Toplevel(root)

    def show_entry_fields1():
        isi_jawaban = (str(e2.get()))

        global isi_data
        isi_data = isi_jawaban


    e2 = tk.Entry(newWindow)
    e2.insert(10,"")


    jawaban = tk.Button(newWindow, text='NAMA',padx=27,pady=-5, command=show_entry_fields1)
    e2.grid(row=0, column=1)
    jawaban.grid(row=0, column=0, )




    edit_nama = tk.Button(newWindow, text ="EDIT NAMA",padx=15,command=lambda:contact.edit_nama_kontak(isi_data))
    edit_nama.grid(row=1,column=0)
    edit_email = tk.Button(newWindow,text="EDIT EMAIL",padx=1,pady=1,command=lambda:contact.edit_email_kontak(isi_data))
    edit_email.grid(row=1,column=2)
    edit_telp = tk.Button(newWindow,text="EDIT TELP",padx=20,command=lambda:contact.edit_telp_kontak(isi_data))
    edit_telp.grid(row=2,column=0)
    edit_alamat= tk.Button(newWindow,text="EDIT ALAMAT",padx=20,command=lambda:contact.edit_alamat_kontak(isi_data))
    edit_alamat.grid(row=2,column=1)
    edit_umur = tk.Button(newWindow,text="EDIT UMUR",command=lambda:contact.edit_umur_kontak(isi_data))
    edit_umur.grid(row=2,column=2)
    hapus_kontak = tk.Button(newWindow,text="EDIT UMUR",padx=26,command=lambda:contact.hapus_kontak(isi_data))
    hapus_kontak.grid(row=1,column=1)
def createNewWindowLihatSemuaKontak():
    winbaru = Toplevel(root)



    Label(winbaru,text="Daftar Kontak Yang Telah Disimpan").pack()
    if bool(contact_table.data) == False:
        Label(winbaru,text="Belum ada data yg disimpan saat ini.").pack()


    else:

        for contact in contact_table.data:
            Label(winbaru,text=f'NAMA : {contact}\nNO : {contact_table.data[contact]["telp"]}\nEMAIL : {contact_table.data[contact]["email"]}\nUMUR : {contact_table.data[contact]["umur"]}\nALAMAT : {contact_table.data[contact]["alamat"]}').pack()
class LabelSing:
    def __init__(self,screen,text):
        self.label = Label(screen,text=text)
        self.label.pack()
class SingkatButton:
    def __init__(self,image, padx, pady, command, row, column,):
        self.window = root

        self.padx = padx
        self.pady = pady
        self.command = command
        self.image = image
        self.row = row
        self.column = column
        self.isi = tk.Button(self.window,image=self.image, padx=self.padx, pady=self.pady, command=self.command,borderwidth=0)
        self.isi.grid(row= self.row, column =self.column)
while True:

    t1 = threading.Thread(target=horse.mainapp)
    t1.start()
    contact_table.simpan_barcode()
    contact_table.simpan()


    root = tk.Tk()
    root.title('APLIKASI PENDAFTARAN')
    root.iconbitmap('register.ico')
    root.geometry("200x200")

    # Making Buttons
    daftar_btn =ImageTk.PhotoImage(Image.open("register.png"))
    akses_btn =  ImageTk.PhotoImage(Image.open("th.png"))
    edit_btn =  ImageTk.PhotoImage(Image.open("edit_data.png"))
    see_btn =ImageTk.PhotoImage(Image.open("list.png"))
    terms_btn = ImageTk.PhotoImage(Image.open("terms.png"))
    search_btn = ImageTk.PhotoImage(Image.open("search.png"))
    SingkatButton(daftar_btn,50, 20, createNewWindowforDaftar, 3, 0)
    SingkatButton(akses_btn, 60, 20, contact.mendaftar, 3, 1)
    SingkatButton(see_btn, 50, 20, createNewWindowLihatSemuaKontak, 3, 2)
    SingkatButton(edit_btn, 40, 20,createNewWindow , 2, 0)
    SingkatButton(terms_btn, 46, 20, create_new_window_for_terms, 2, 1)
    SingkatButton(search_btn, 65, 20, createNewWindowforCariData, 2, 2)



    root.mainloop()
    tk.mainloop()
