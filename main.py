import inquirer
import os
import prettytable
import time



from CRUD.CREATE import tambah_game
from CRUD.READ import tampilkan_game
from CRUD.UPDATE import ubah_data_game
from CRUD.DELETE import hapus_game

from MENU import menu_crud_admin,menu_multi_login,menu_user,menu_autentikasi_user
from AUTENTIKASI import admin_login,user_login,user_regist

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

# Program Utama

if __name__ == "__main__":
    while True:
        
        menu_dipilih = menu_multi_login()
        if menu_dipilih == "1":
            admin_login()
            
        elif menu_dipilih == "2":
            menu_autentikasi_dipilih = menu_autentikasi_user()
            
            if menu_autentikasi_dipilih == "1":
                user_login()
            else:
                user_regist()
                
        else: 
            break
        
        
    print("=========PROGRAM BERAKHIR=========")
            
        
    
    
