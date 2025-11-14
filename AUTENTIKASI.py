from MENU import menu_crud_admin,menu_user

import json
from pathlib import Path

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
    max_percobaan = 5 

    percobaan = 0 

    while percobaan < max_percobaan:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        for akun in list_akun_admin:
            if username == akun["username"] and password == akun["password"]:
                print(f"Selamat datang yang mulia, {username} , Anda berhasil login sebagai admin.")
                menu_crud_admin()
                percobaan = max_percobaan 
                break
        
                
        else:
            percobaan += 1
            print(f"Username atau password salah. Sisa percobaan: {max_percobaan - percobaan}")
            if percobaan == max_percobaan:
                print("Sudah sampai max percobaan. coba lagi nanti.")
                break
                
             
def cek_username(data_username):
    
    
    username = input("Buat Username Anda")
    for key,value in data_username.items():
        print(value["username"])
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
        
        try:
            pin = input(input_message)
            if len(pin) >= 4 and len(pin) <= 6:
                return int(pin)
            else:
                raise ValueError
            
        except ValueError:
            print("Masukan Angka 4-6 Digit!!")
            continue
            
        

def user_regist():
    
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    path_json = folderSekarang / "DATA" / "DATA_USER.json"
    
    with open(path_json, "r") as file:
        data_user = json.load(file)
        
    user_id = f"U{len(data_user)+1:03d}"
    
    username = cek_username(data_user) 
    password = input("Buat PAssword Anda: ")
    pin_user = buat_pin("Buat PIN anda 4-6 Digit: ")
    saldo = 0
    koleksi_game = []
    
    user_baru = {
        "username": username,
        "password": password,
        "PIN": pin_user,
        "saldo":saldo,
        "koleksi_game":koleksi_game
    }
        
    data_user.update({user_id:user_baru})
    
    
    with open(path_json, "w") as newValue:
        json.dump(data_user,newValue,indent=4)
        
    print("Akun Anda Berhasil Dibuat!")
    
    menu_user(user_id)
    
    
    # while True:
    #     username = input("Masukan Username Anda: ")

def user_login():
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    path_json = folderSekarang / "DATA" / "DATA_USER.json"
    
    with open(path_json, "r") as file:
        data_user = json.load(file)
        
    percobaan = 0
    max_percobaan = 5
    while percobaan < max_percobaan:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        for id,akun in data_user.items():
            if username == akun["username"] and password == akun["password"]:
                print(f"Selamat datang {username} , Anda berhasil login.")
                menu_user(id)
                percobaan = max_percobaan 
                break
        
                
        else:
            percobaan += 1
            print(f"Username atau password salah. Sisa percobaan: {max_percobaan - percobaan}")
            if percobaan == max_percobaan:
                print("Sudah sampai max percobaan. coba lagi nanti.")
                break
        
        
    
    