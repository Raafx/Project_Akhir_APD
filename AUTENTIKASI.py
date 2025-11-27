from MENU import menu_crud_admin,menu_user,menu_multi_login

import json
from pathlib import Path
import os
import inquirer

from time import sleep

from INPUT_HANDLING import input_number_handling, input_string_handling

list_akun_admin = [
    {
    "username":"Rafi",
    "password":"admin034"
    },
    {
    "username":"Bakil",
    "password":"admin044"
    },
    {
    "username":"Ozora",
    "password":"admin034"
    }
                   ]



def admin_login():
    os.system("cls || clear")
    max_percobaan = 5 

    percobaan = 0 
    print("======== Silahkan Masukan Usernam dan Passowrd yang sesuai ========\n")
    while percobaan < max_percobaan:
        username = input_string_handling("Masukkan username")
        password = input_string_handling("Masukkan password")

        for akun in list_akun_admin:
            if username == akun["username"] and password == akun["password"]:
                menu_crud_admin(username)
                percobaan = max_percobaan 
                break
        
                
        else:
            percobaan += 1
            os.system("cls || clear")
            print(f"Username atau password salah. Sisa percobaan: {max_percobaan - percobaan}\n")
            if percobaan == max_percobaan:
                print("\nAnda Sudah mencapai Batas percobaan. Silahkan Kembali ke Menu Login.\n")
                input("Tekan enter untuk kembali: ")
                break
                
             
def cek_username(data_username):
    
    username = input_string_handling("buat username anda")
    for key,value in data_username.items():
        
        if username == value["username"]:
            print("Username Sudah ada, silahkan buat username lain\n")
            username_sudah_ada = True
            break
        else:
            username_sudah_ada = False
            
    if username_sudah_ada:
        cek_username(data_username)
    else:
        return username
    
                  
            
def buat_pin(input_message):
    while True:
        
        
        pin = input_number_handling(input_message)
        if len(str(pin)) >= 4 and len(str(pin)) <= 6:
            return pin
        else:
            print("Pin harus berjumlah 4-6 Digit!")
            
        
            
        

def user_regist():
    os.system("cls || clear")
    
    print("================ Silahkan buat Akun KukuStation Anda ================\n")
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    path_json = folderSekarang / "DATA" / "DATA_USER.json"
    
    with open(path_json, "r") as file:
        data_user = json.load(file)
        
    user_id = f"U{len(data_user)+1:03d}"
    
    username = cek_username(data_user) 
    password = input_string_handling("buat Password anda")

    pin_user = buat_pin("Buat PIN anda 4-6 Digit: ")
    saldo = 0
    koleksi_game = []
    keranjang = []
    
    user_baru = {
        "username": username,
        "password": password,
        "PIN": pin_user,
        "saldo":saldo,
        "keranjang":keranjang,
        "koleksi_game":koleksi_game
    }
        
    data_user.update({user_id:user_baru})
    
    
    with open(path_json, "w") as newValue:
        json.dump(data_user,newValue,indent=4)
        
    
    os.system("cls || clear")
    print("============== Selamat, Akun Anda Berhasil Dibuat! ==============\n")
    
    pilih_menu = [inquirer.List(
            "Menu",
            message="Ingin Lanjut ke Menu Utama?",
            choices=[
                "1. Ya",
                "2. Kembali ke Menu Login"]
            )
            ]
    menu_dipilih = inquirer.prompt(pilih_menu)["Menu"]
    match menu_dipilih:
        case "1. Ya":
            menu_user(user_id,username)
        case "2. Kembali ke Menu Login":
            menu_multi_login()
            
    
    
    


def user_login():
    os.system("cls || clear")
    
    print("======== Silahkan Masukan Usernam dan Passowrd yang sesuai ========\n")
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    path_json = folderSekarang / "DATA" / "DATA_USER.json"
    
    with open(path_json, "r") as file:
        data_user = json.load(file)
        
    percobaan = 0
    max_percobaan = 5
    while percobaan < max_percobaan:
        username = input_string_handling("Masukkan username: ")
        password = input_string_handling("Masukkan password: ")

        for id,akun in data_user.items():
            if username == akun["username"] and password == akun["password"]:
                menu_user(id,username)
                percobaan = max_percobaan 
                break
        
                
        else:
            os.system("cls || clear")
            percobaan += 1
            print(f"Username atau password salah. Sisa percobaan: {max_percobaan - percobaan}\n")
            if percobaan == max_percobaan:
                print("\nAnda Sudah mencapai Batas percobaan. Silahkan Kembali ke Menu Login.\n")
                input("Tekan enter untuk kembali: ")
                break
        
        
    
    