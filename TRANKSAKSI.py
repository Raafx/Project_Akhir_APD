import os
import json
from pathlib import Path
from CRUD.READ import tampilkan_game
import inquirer



def beli_game(id_akun_saat_ini):
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    path_user_json = folderSekarang / "DATA" / "DATA_USER.json"
    path_game_json = folderSekarang / "DATA" / "DATA_GAME.json"
    
    with open(path_user_json, "r") as file:
        data_user = json.load(file)
        
    
    user = data_user[id_akun_saat_ini]
        
    with open(path_game_json, "r") as file:
        data_game = json.load(file)
        
    tampilkan_game()
    
    pilih_game = input("Masukan Judul Game yang ingin dibeli: ")
    
    
    for id,game in data_game.items():
        if game["judul_game"].upper() == pilih_game.upper():
            for judul_game in user["koleksi_game"]:
                if judul_game == game["judul_game"]:
                    os.system("cls || clear")
                    print(f"\nAnda sudah memiliki Game {judul_game}, silahkan beli game yang lain\n")
                    beli_game(id_akun_saat_ini)
                    break
                else:
                    
                    print(f"Anda membeli Game {game["judul_game"]} dengan harga {game["harga"]}")
                    pembayaran = int(input("Silahkan menginput nominal pembayaran Anda: "))

                    saldo_user = user["saldo"]
                    saldo_user_setelah_bayar = saldo_user-pembayaran

                    if saldo_user_setelah_bayar < 0:
                        pilih_menu = [inquirer.List(
                        "Menu",
                        message="Saldo Anda Tidak Cukup, Ingin Top Up terlebih dahulu?",
                        choices=[
                            "1. Top Up",
                            "2. Kembali"]
                        )
                        ]
                        menu_dipilih = inquirer.prompt(pilih_menu)["Menu"]

                        match menu_dipilih:
                            case "1. Top Up":
                                top_up(id_akun_saat_ini)
                                break
                            case "2. Kembali":
                                break
                    else:

                        user["koleksi_game"].append(game['judul_game'])

                        user.update({"koleksi_game":user["koleksi_game"],
                                     "saldo":saldo_user_setelah_bayar
                                     })

                        with open(path_user_json, "w") as newValue: 
                            json.dump(data_user, newValue, indent=4)

                        print(f"\nPembayaran Berhasil, Game {game['judul_game']} Telah masuk ke Koleksi Anda\n")

                        pilih_menu = [inquirer.List(
                        "Menu",
                        message="Ingin Membeli Game Lain?",
                        choices=[
                            "1. Ya",
                            "2. Kembali ke Menu"]
                        )
                        ]
                        menu_dipilih = inquirer.prompt(pilih_menu)["Menu"]

                        match menu_dipilih:
                            case "1. Ya":
                                beli_game(id_akun_saat_ini)
                                break
                            case "2. Kembali ke Menu":
                                break
        
                
                
                
                
                        
                
                

            
    
    
        
    
        
    

def top_up(id_akun_saat_ini):
    
    
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    path_json = folderSekarang / "DATA" / "DATA_USER.json"
    
    with open(path_json, "r") as file:
        data_user = json.load(file)
    
    print("=================== MENU TOP UP ===================\n")
    
    nominal = int(input("Masukan Nominal Top Up: "))
    
    
    
    akun_saat_ini = data_user[id_akun_saat_ini]
    saldo_akun = akun_saat_ini["saldo"]
     
    percobaan = 0
    while True:
        pin = int(input("Masukan PIN anda: "))
        if pin == akun_saat_ini["PIN"]:
            saldo_akun += nominal
            
            akun_saat_ini.update({"saldo":saldo_akun})
            
            with open(path_json, "w") as newValue: 
                json.dump(data_user, newValue, indent=4)

            print("==================================================\n")    

            print("Top Up Berhasil!")
            print(f"saldo anda saat ini: {saldo_akun}")
            break
        else:
            print("Pin Anda Salah, silahkan coba lagi")
            percobaan+=1
            if percobaan == 5:
                print("Terlalu Banyak Mencoba, Anda akan dibawa kemabli ke Menu Utama")
                


    
    
    
    
    
    