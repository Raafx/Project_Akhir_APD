import inquirer
import os

from CRUD.CREATE import tambah_game
from CRUD.READ import tampilkan_game, tampilkan_info_akun
from CRUD.UPDATE import ubah_data_game
from CRUD.DELETE import hapus_game

from TRANKSAKSI import beli_game,top_up



def menu_multi_login():

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
    return menu_dipilih["Menu"]
    
    

def menu_crud_admin():
    while True:
        os.system("cls || clear")
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
        menu_dipilih = inquirer.prompt(pilih_menu)["Menu"]
        print("======================================================")


        match menu_dipilih:
            case "1. Tambah Game (Create)":
                os.system("cls || clear")
                tambah_game()
                
            case "2. Tampilkan Data Game (Read)":
                os.system("cls || clear")
                tampilkan_game()
                input("Input apa saja untuk kembali: ")
                
            case "3. Ubah Data Game (Update)":
                os.system("cls || clear")
                ubah_data_game()
                
            case "4. Hapus Data Game (Delete)":
                os.system("cls || clear")
                hapus_game()
                
            case "5. Keluar":
                break


        
    
    

def menu_user(akun_saat_ini):
    while True:
        
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
        menu_dipilih = inquirer.prompt(pilih_menu)["Menu"]
        print("======================================================\n")
        match menu_dipilih:
            case "1. Beli Game":
                beli_game(akun_saat_ini)
                
            case "2. Info Akun":
                tampilkan_info_akun(akun_saat_ini)
                input("Input apa saja untuk kembali: ")
            
            case "3. Top Up":
                top_up(akun_saat_ini)
                
            case "4. Log Out":
                break


def menu_autentikasi_user():
    os.system("cls || clear")
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
    menu_dipilih = inquirer.prompt(pilih_menu)["Menu"]
    return menu_dipilih
        
        
            
        




