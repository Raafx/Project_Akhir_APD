import inquirer
import os

from CRUD.CREATE import tambah_game
from CRUD.READ import tampilkan_game
from CRUD.UPDATE import ubah_data_game
from CRUD.DELETE import hapus_game


def menu_multi_login():
    os.system("cls || clear")
    print("================(Selamat Datang di KukuStation)================\n")
    pilih_menu = [inquirer.List(
        "Menu",
        message="Pilih Role Anda",
        choices=[
            "1. Admin",
            "2. User",
            "3. Keluar"]
        )
                  ]
    
    menu_dipilih = inquirer.prompt(pilih_menu)
    return menu_dipilih["Menu"][0]
    
    

def menu_crud_admin():
    print("========= KUKUSTATION: JUAL BELI GAME ===========\n")
    print("Anda Login sebagai Admin, Silahkan pilih menu dibawah:")
    print("\n======================================================")
    pilih_menu = [inquirer.List(
            "Menu",
            message="Pilih Menu",
            choices=[
                "1. Tambah Game (Create)",
                "2. Tampilkan Data Game (Read)",
                "3. Ubah Data Game (Update)",
                "4. Hapus Data Game (Delete)",
                "5. Keluar"]
            )
        ]
    menu_dipilih = inquirer.prompt(pilih_menu)
    print("======================================================")
    
    while True:
        
        if menu_dipilih == "1":
            tambah_game()
            
        elif menu_dipilih == "2":
            tampilkan_game()
            
        elif menu_dipilih == "3":
            ubah_data_game()
            
        elif menu_dipilih == "4":
            hapus_game()
            
        elif menu_dipilih == "5":
            break
    
    

def menu_user():
    print("========= KUKUSTATION: JUAL BELI GAME ===========\n")
    print("Anda Login sebagai User, Silahkan pilih menu dibawah:")
    pilih_menu = [inquirer.List(
            "Menu",
            message="Pilih Menu",
            choices=[
                "1. Beli Game",
                "2. Info Akun",
                "3. Top Up",
                "4. Log Out",
                ]
            )
        ]
    menu_dipilih = inquirer.prompt(pilih_menu)
    print("======================================================\n")
    if menu_dipilih == "1":
        pass
        
    elif menu_dipilih == "2":
        pass
        
    elif menu_dipilih == "3":
        pass
        
    elif menu_dipilih == "4":
        pass

def menu_autentikasi_user():
    
    pilih_menu = [inquirer.List(
            "Menu",
            message="Pilih Menu",
            choices=[
                "1. Login",
                "2. Buat Akun Baru",
                "3. Kembali",
                ]
            )
        ]
    menu_dipilih = inquirer.prompt(pilih_menu)
    return menu_dipilih
        

def menu_akun_user():
    pass



