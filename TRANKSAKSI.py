import os
import json
from pathlib import Path
from CRUD.READ import tampilkan_game
import inquirer
from time import sleep

from INPUT_HANDLING import input_number_handling, input_string_handling


def masuk_keranjang(id_game,id_akun,data_user,data_game):
    user = data_user[id_akun]
    keranjang_user = user["keranjang"]
    
    keranjang_user.append(id_game)
    user.update({"keranjang":keranjang_user})
    data_user.update({id_akun:user})
    
    print("===================== Game Telah Berhasil Ditambahkan di Keranjangmu! =====================")
    
    
    

def beli_game(id_akun_saat_ini):
    
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    path_user_json = folderSekarang / "DATA" / "DATA_USER.json"
    path_game_json = folderSekarang / "DATA" / "DATA_GAME.json"
    
    with open(path_user_json, "r") as file:
        data_user = json.load(file)
        
    
    user = data_user[id_akun_saat_ini]
    saldo_user = user["saldo"]
    koleksi_game_user = user["koleksi_game"]
        
    with open(path_game_json, "r") as file:
        data_game = json.load(file)
        
    
        
    tampilkan_game()
    
    pilih_game = input_string_handling("\nMasukan Judul Game yang ingin dibeli")
    
    game_ditemukan = False
    
    
    for id,game in data_game.items():
        
        if game["judul_game"].upper() == pilih_game.upper():
            game_ditemukan = True
            
            judul_game = game["judul_game"]
            harga_game = game["harga"]
            
            game_terjual = game["total_terjual"]
            pendapatan_game = game["total_pendapatan"]
            
            if id in koleksi_game_user:
                os.system("cls || clear")
                print(f"\nAnda sudah memiliki Game {judul_game}, silahkan beli game yang lain\n")
                beli_game(id_akun_saat_ini)
                break
            else:
                
                    
                
                
                    print(f"Anda membeli Game {judul_game} dengan harga {harga_game:,}")
                    pilih_menu = [inquirer.List(
                            "Menu",
                            message="Konfirmasi Pembayaran ??",
                            choices=[
                                "1. Ya",
                                "2. Batal"]
                            )
                            ]
                    menu_dipilih = inquirer.prompt(pilih_menu)["Menu"]

                    match menu_dipilih:
                        case "1. Ya":
                        
                            while True:
                                saldo_user-= harga_game 



                                if saldo_user < 0:
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
                                            while True:
                                                top_up(id_akun_saat_ini)

                                                with open(path_user_json, "r") as file:
                                                    data_user = json.load(file)

                                                saldo_user = data_user[id_akun_saat_ini]["saldo"]
                                                if saldo_user >= harga_game:
                                                    break
                                                
                                                else:
                                                    print("saldo anda masih tidak cukup, silahkan top up lagi")
                                                    continue
                                                
                                        case "2. Kembali":
                                            break
                                else:
                                    koleksi_game_user.append(id)
                                    user.update({"koleksi_game":koleksi_game_user,
                                                 "saldo":saldo_user
                                                 })
                                    data_user.update({id_akun_saat_ini:user})

                                    game_terjual+=1
                                    pendapatan_game+=harga_game
                                    game.update({"total_terjual":game_terjual,
                                                 "total_pendapatan":pendapatan_game})


                                    with open(path_user_json, "w") as newValue: 
                                        json.dump(data_user, newValue, indent=4)

                                    with open(path_game_json, "w") as newValue: 
                                        json.dump(data_game, newValue, indent=4)

                                    print(f"\nPembayaran Berhasil, Game {judul_game} Telah masuk ke KoleksiAnda\n")
                                    print(f"Saldo anda saat ini: {saldo_user:,}")
                                    break
    if not game_ditemukan:
        os.system("cls || clear")
        print("Judul Game tidak ditemukan, silahkan input ulang\n")
        beli_game(id_akun_saat_ini)
        
    else:
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

            case "2. Kembali ke Menu":
                pass
                
        
        
        
        

def top_up(id_akun_saat_ini):
    
    
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    path_json = folderSekarang / "DATA" / "DATA_USER.json"
    
    with open(path_json, "r") as file:
        data_user = json.load(file)
    
    print("=================== MENU TOP UP ===================\n")
    
    nominal = input_number_handling("Masukan Nominal Top Up")
    
    
    
    akun_saat_ini = data_user[id_akun_saat_ini]
    saldo_akun = akun_saat_ini["saldo"]
     
    percobaan = 5
    while True:
        pin = input_number_handling("Masukan PIN anda: ")
        if pin == akun_saat_ini["PIN"]:
            saldo_akun += nominal
            
            akun_saat_ini.update({"saldo":saldo_akun})
            
            with open(path_json, "w") as newValue: 
                json.dump(data_user, newValue, indent=4)
    

            print("\n==================Top Up Berhasil!=================\n")
            print(f"saldo anda saat ini: Rp. {saldo_akun:,}")
            break
        else:
            percobaan-=1
            print(f"Username atau password salah. Sisa percobaan: {percobaan}")
            
            if percobaan == 0:
                print("Terlalu Banyak Mencoba, Silahkan Kembali ke menu Utama")
                break
                