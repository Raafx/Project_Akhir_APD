import datetime
import json
import inquirer
from pathlib import Path
import sys

lokasi = Path(__file__).resolve()
folderFile = lokasi.parent
folderMain = folderFile.parent

sys.path.append(str(folderMain))

from INPUT_HANDLING import input_number_handling, input_string_handling, input_date_handling

def tambah_game():
    lokasiFile = Path(__file__).resolve()
    folderSekarang = lokasiFile.parent
    folderUtama = folderSekarang.parent
    path_json = folderUtama / "DATA" / "DATA_GAME.json"

    checkDup = 0
    with open(path_json, "r") as file :
        game = json.load(file)

    try :
     Nama_game = input_string_handling("masukkan nama game")

     for key in game:
         if Nama_game in game[key]["judul_game"] :
            checkDup += 1

     if checkDup > 0 :
        raise ValueError("game sudah ada")
     
    except ValueError as err :
       print(f"input error : {err}")
       return

    tanggal = input_date_handling("tanggal rilis (yyyy-mm-dd) : ") 
    harga = input_number_handling("masukkan harga")
       
    genre = input("masukkan genre : ")
    
    list_genre = genre.split(",")
    list_genre = [item for item in list_genre if item and not item.isspace()]
    if len(list_genre)< 1 :
       print("genre tidak boleh kosong")
       return

    
    gameBaru = {
       "judul_game" : Nama_game,
       "tahun_rilis" : tanggal,
       "harga" : harga,
       "genre" : list_genre,
       "total_terjual" : 0,
       "total_pendapatan" : 0
    }
    urutan = len(game) + 1
    game[f"A{urutan:03d}"] = gameBaru

    with open(path_json, "w") as newValue :
       json.dump(game, newValue, indent=4)
    
    print("game berhasil dimasukkan")
    lanjut = [inquirer.List(
       "menu",
       message="mau lanjut tambah game?",
       choices=[
          "1. Ya",
          "2. Tidak"]

      )
    ]
    pilihan = inquirer.prompt(lanjut)["menu"][0]

    if pilihan == "1" :
       tambah_game()

    elif pilihan == "2" :
       return "keluar dari fitur tambah game"