#pembatas_dan_deskripsi_kode
###### Login
import time
import os
print "========================================="
def username():
    def user1():
        user = raw_input("Username : ")
        if user == "neox":
            time.sleep(1)
            password = raw_input("Password : ")
            if password == "newbie":
                time.sleep(2)
                print "Sukses Login"
                time.sleep(1)
            else:
                time.sleep(2)
                print "Gagal Login"
                username()
        else:
            time.sleep(2)
            print "Username Salah! --Mengulang"
            username()
    user1()
username()
os.system('clear')

def logo():
    print """
    ____       ____     ____       ____
   |    \     |    |   |    \     |    |
   |     \    |    |   |     \    |    |
   |      \   |    |   |      \   |    |
   |       \  |    |   |       \  |    |
   |        \ |    |   |        \ |    |
   |         \|    |   |         \|    |
   |    |\         |   |    |\         |
   |    | \        |   |    | \        |
   |    |  \       |   |    |  \       |
   |    |   \      |   |    |   \      |
   |    |    \     |   |    |    \     |
   |____|     \____|   |____|     \____| 
   
   ==============CyberTeam==============
   ================[ID]=================
"""
logo()
###### Intro Coder

print" "
print "Pulsa Gratis All Operator"
time.sleep(1)
print "Author : NeOX_NXCT"
time.sleep(1)
print "Team   : NN_Cyber_Team[ID]"
time.sleep(1)
print "Note   : Gunakan Selayaknya Yaa"
time.sleep(2)
print " "

###### Nama Yang Menggunakan

nama = raw_input("Nama Ente ? > ");
print " "
time.sleep(1)
print "Hallo",nama,"bangsat yang suka gratisan"
print " "

###### Daftar Provider

lanjutkan = raw_input("Lanjutken? y/n > ");
if lanjutkan == "y" or lanjutkan == "Y":
    def mulai_per():
        os.system('clear')
        logo()
        print """
01) Pulsa Tri
02) Pulsa Telkomsel
03) Pulsa XL
04) Pulsa Indosat
05) Pulsa Smartfren
"""

###### Daftar Nominal Pulsa

       
        def pulsa():
            pulsa = raw_input("Pilih > ")
            if pulsa == "01" or pulsa == "1":
                os.system('clear')
                logo()
                print """
01) Pulsa Tri 5.000
02) Pulsa Tri 10.000
03) Pulsa Tri 20.000
04) Pulsa Tri 50.000
05) Pulsa Tri 100.000
00) Awal
"""

###### Isi kode nominal

                
                tri = raw_input("Pilih > ")
                if tri == "01" or tri == "1":
                    os.system('clear')
                    logo()
                    print "Menghubungi Server"
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(3)
                    nomor = raw_input("Nomor Ente> ");
                    print "Memproses pengiriman pulsa ->",nomor
                    time.sleep(2)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "." 
                    time.sleep(1)
                    print "pengiriman ke nomor",nomor,"sukses"
                    time.sleep(5)
                    print "."
                    time.sleep(1)
                    print "TAPI BOONG HAHAHA"
                    time.sleep(3)
                    print "KALO MAU PULSA YA KERJA ANJENG!!!"
                    time.sleep(3)
                    print "JAMAN SEKARANG GA ADA YANG GRATISAN BANGSAD!!!"
                    time.sleep(3)

###### Tanya lanjut

                    balik = raw_input("Lanjutken ? y/n > ")
                    if balik == "y" or balik == "Y":
                        mulai_per()
                    else:
                        print "Auto Exit!!! "
                        pulsa()
                        exit()
                        
###### Isi kofe nominal
                       
                elif tri == "02" or tri == "2":
                    print "Menghubungi Server"
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(3)
                    nomor = raw_input("Nomor Ente> ");
                    print "Memproses pengiriman pulsa ->",nomor
                    time.sleep(2)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "." 
                    time.sleep(1)
                    print "Pengiriman ke nomor",nomor,"sukses"
                    time.sleep(5)
                    print "."
                    time.sleep(1)
                    print "TAPI BOONG HAHAHA"
                    time.sleep(3)
                    print "KALO MAU PULSA YA KERJA ANJENG!!!"
                    time.sleep(3)
                    print "JAMAN SEKARANG GA ADA YANG GRATISAN BANGSAD!!!"
                    time.sleep(3)

###### Tanya lanjut

                    balik = raw_input("Lanjutken ? y/n > ")
                    if balik == "y" or balik == "Y":
                        mulai_per()
                    else:
                        print "Auto Exit!!! "
                        exit()
                        
###### Isi kode nominal
      
                if tri == "03" or tri == "3":
                    print "Menghubungi Server"
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(3)
                    nomor = raw_input("Nomor Ente> ");
                    print "Memproses pengiriman pulsa ke nomor", nomor
                    time.sleep(2)
                    print "."
                    time.sleep(1)
                    print "."
                    time.sleep(1)
                    print "." 
                    time.sleep(1)
                    print "Sukses"
                    time.sleep(5)
                    print "."
                    time.sleep(1)
                    print "TAPI BOONG HAHAHA"
                    time.sleep(3)
                    print "KALO MAU PULSA YA KERJA ANJENG!!!"
                    time.sleep(3)
                    print "JAMAN SEKARANG GA ADA YANG GRATISAN BANGSAD!!!"
                    time.sleep(3)
                    balik = raw_input("Lanjutken ? y/n > ")
                    if balik == "y" or balik == "Y":
                        mulai_per()
                    else:
                        print "Auto Exit!!! "
                        exit()
                        
                time.sleep(2)
            elif pulsa == "02" or pulsa == "2":
                print """
01) Pulsa Telkomsel 5.000
02) Pulsa Telkomsel 10.000
03) Pulsa Telkomsel 20.000
04) Pulsa Telkomsel 50.000
05) Pulsa Telkomsel 100.000
00) Awal
"""
            elif pulsa == "03" or pulsa == "3":
                print """
01) Pulsa XL 5.000
02) Pulsa XL 10.000
03) Pulsa XL 20.000
04) Pulsa XL 50.000
05) Pulsa XL 100.000
00) Awal
"""
            elif pulsa == "04" or pulsa == "4":
                print """
01) Pulsa Indosat 5.000
02) Pulsa Indosat 10.000
03) Pulsa Indosat 20.000
04) Pulsa Indosat 50.000
05) Pulsa Indosat 100.000
00) Awal
"""
            elif pulsa == "05" or pulsa == "5":
                print """
01) Pulsa Smartfren 5.000
02) Pulsa Smartfren 10.000
03) Pulsa Smartfren 20.000
04) Pulsa Smartfren 50.000
05) Pulsa Smartfren 100.000
00) Awal
"""
                
            else:
                print ("Salah masukin dancok")
                mulai_per()
        pulsa()   
    mulai_per()
    
    