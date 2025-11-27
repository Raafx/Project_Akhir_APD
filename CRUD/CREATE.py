import datetime
import json
import inquirer
from pathlib import Path
import re
import sys

lokasi = Path(__file__).resolve()
folderFile = lokasi.parent
folderMain = folderFile.parent

sys.path.append(str(folderMain))

from INPUT_HANDLING import input_number_handling, input_string_handling, input_date_handling

def buat_id(game_id) :
   max_nomor_id = 0
   pola = r'^A(\d+)$'

   for used_id in game_id :
      match = re.match(pola, used_id)

      if match :
         nomor_id = int(match.group(1))

         if nomor_id > max_nomor_id :
            max_nomor_id = nomor_id
   
   nomor_baru = max_nomor_id + 1
   id_baru = f"A{nomor_baru:03d}"
   return id_baru

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

    tanggal = input_date_handling("tanggal rilis (yyyy-mm-dd)") 
    harga = input_number_handling("masukkan harga")
       
    genre = input("masukkan genre : ")
    
    list_genre = genre.split(",")
    list_genre = [item for item in list_genre if item and not item.isspace()]
    if len(list_genre)< 1 :
       print("genre tidak boleh kosong")
       return

    
    gameBaru = {
       "judul_game" : Nama_game,
       "tahun_rilis" : tanggal.isoformat(),
       "harga" : harga,
       "genre" : list_genre,
       "total_terjual" : 0,
       "total_pendapatan" : 0
    }
    
    id_game_terpakai = [id_game for id_game in game]
    id_baru = buat_id(id_game_terpakai)
    game[id_baru] = gameBaru

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

tambah_game()